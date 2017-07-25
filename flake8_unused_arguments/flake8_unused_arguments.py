import ast


class UnusedArgumentsPlugin():
    """Warns when arguments are unused."""
    name = 'unused-arguments'
    version = '0.1.0'

    def __init__(self, tree):
        self.tree = tree

    def run(self):
        import ipdb; ipdb.set_trace()
        # yield (1, 0, 'R101 The off-by-default plugin was enabled',
        #        'UnusedArgumentsPlugin')
        for statement in self.tree.body:
            if isinstance(statement, ast.FunctionDef):
                yield (
                    statement.col_offset,
                    statement.lineno,
                    'R101 You have a FunctionDef',
                    'UnusedArgumentsPlugin'
                )
