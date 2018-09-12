import sys

from redbaron import (
    AssertNode,
    AssignmentNode,
    AssociativeParenthesisNode,
    CallArgumentNode,
    CallNode,
    ClassNode,
    CommaProxyList,
    DefNode,
    DictitemNode,
    DotProxyList,
    ForNode,
    ListNode,
    ListComprehensionNode,
    RedBaron,
    SetNode,
    StringChainNode,
    TupleNode,
    WithNode
)


error = 'C101 ElementMissingComma: Implicit string concatenation comma-separated expression'

CONTAINER_NODES = (ListNode, TupleNode, SetNode, CallNode)


def is_comma_separated(statement):
    if isinstance(statement, ListComprehensionNode):
        return False  # todo

    return (
        isinstance(statement, CONTAINER_NODES)
        or isinstance(statement.value, (CommaProxyList, DotProxyList))
    )


def format_error(filename, line, column):
    return f'{filename}:{line}:{column}: {error}'


def check_element(element):
    if isinstance(element, (AssociativeParenthesisNode, CallArgumentNode)):
        element = element.value

    if isinstance(element, StringChainNode):
        bounding_box = element.absolute_bounding_box
        offending_element = element.value[0]

        yield {
            'line': bounding_box.top_left.line,
            'column': bounding_box.top_left.column + len(offending_element.value),
        }

    elif isinstance(element, DictitemNode):
        yield from check_element(element.key)

        yield from check_element(element.value)

    elif is_comma_separated(element):
        for element in element.value:
            yield from check_element(element)


def statement_missing_comma(statement):
    if isinstance(statement, (AssignmentNode, AssertNode)):
        statement = statement.value

    if not is_comma_separated(statement):
        return

    for element in statement.value:
        yield from check_element(element)


def iterate_through_nodes(fst):
    for statement in fst:
        if isinstance(statement, ClassNode):
            for line in statement.value:
                if isinstance(line, DefNode):
                    yield from iterate_through_nodes(line)

        elif isinstance(statement, (WithNode, ForNode)):
            yield from iterate_through_nodes(statement.value)

        else:
            yield statement


def main(filename):
    with open(filename) as f:
        red = RedBaron(f.read())

    for statement in iterate_through_nodes(red):
        for violation in statement_missing_comma(statement):
            print(format_error(filename, **violation))


if __name__ == '__main__':
    main(sys.argv[1])
