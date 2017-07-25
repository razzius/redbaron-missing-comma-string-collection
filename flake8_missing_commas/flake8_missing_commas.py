import ast


class MissingCommasPlugin():
    """Warns when commas missing in a collection causing strings to be implicitly concatenated."""
    name = 'missing-commas'
    version = '0.1.0'

    def __init__(self, tree):
        self.tree = tree

    def run(self):
        import ipdb; ipdb.set_trace()
        # yield (1, 0, 'R101 The off-by-default plugin was enabled',
        #        'UnusedArgumentsPlugin')
        for statement in self.tree.body:
            if isinstance(statement, ast.List):
                yield (
                    statement.col_offset,
                    statement.lineno,
                    'R101 You have a FunctionDef',
                    'UnusedArgumentsPlugin'
                )
