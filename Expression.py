class Expression:

    def __init__(self, expression, local_vars):
        self.expression = expression.strip()
        self.local_vars = local_vars

    def Render(self):
        if not ('=' in self.expression):
            raise WrongExpression

        if ('*' in self.expression):
        # Render the multiplication
            pass

        if ('=' in self.expression):
            var_name = self.expression[:self.expression.find('=') - 1]
            # Assume expression assigns integers
            var_cont = int(self.expression[self.expression.find('=') + 1:])
            self.local_vars.update({var_name: var_cont})
