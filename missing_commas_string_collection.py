import sys

from redbaron import AssignmentNode, ListNode, RedBaron, SetNode, StringChainNode, TupleNode

error = 'C101 ElementMissingComma: Implicit string concatenation in collection'

CONTAINER_NODES = (ListNode, TupleNode, SetNode)


def format_error(filename, line, column):
    return f'{filename}:{line}:{column}: {error}'


def check_element(element):
    if isinstance(element, StringChainNode):
        bounding_box = element.absolute_bounding_box
        offending_element = element.value[0]

        yield {
            'line': bounding_box.top_left.line,
            'column': bounding_box.top_left.column + len(offending_element.value),
        }

    elif isinstance(element, CONTAINER_NODES):
        for element in element.value:
            yield from check_element(element)


def statement_missing_comma(statement):
    if isinstance(statement, AssignmentNode):
        statement = statement.value

    if not isinstance(statement, CONTAINER_NODES):
        return

    for element in statement.value:
        yield from check_element(element)


def main(filename):
    with open(filename) as f:
        red = RedBaron(f.read())

    for statement in red:
        for violation in statement_missing_comma(statement):
            print(format_error(filename, **violation))


if __name__ == '__main__':
    main(sys.argv[1])
