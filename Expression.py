class Expression:

    def __init__(self, expression, local_vars):
        self.expression = expression.strip()
        self.local_vars = local_vars

    def Render(self):

        # Quitting the application, throws 1 if "exit"
        if (self.expression == "exit"):
            return 1

        # If there is no equality sign, checks if the expression is in the scope.
        # If it is, print it, if not - alert the user.
        if not ('=' in self.expression):
            temp = self.local_vars.get(self.expression)
            if not temp == None:
                print(temp)
            else:
                print("There is no variable " + self.expression + " in the scope")
            return self.local_vars

        var_name = self.expression[:self.expression.find('=') - 1]

        # Check if the variable name is a number.
        # If so, raise an error, pass otherwise.
        try:
            temp = int(var_name)
            raise WrongExpression
        except ValueError:
            print("var name is legal")
            pass
        except WrongExpression:
            print("var name can't be integer")
            raise WrongExpression

        # Assume expression assigns integers
        var_cont = self.expression[self.expression.find('=') + 1:].strip()

        print("checking for operations")

        result = 1

        if ('*' in var_cont):
            print("found a multiplication")
            vars = []
            while ('*' in var_cont):
                vars.append(var_cont[:var_cont.find('*') - 1])
                var_cont = var_cont[var_cont.find('*') + 1:]
            print(vars)
            for elem in vars:
                if self.local_vars.get(elem) == None:
                    raise WrongExpression
                else:
                    result = result * self.local_vars.get(elem)

        if (not '*' in self.expression) and (not '+' in self.expression):
            result = int(var_cont)

        if ('=' in self.expression):
            print("creating new variable")
            self.local_vars.update({var_name: result})
            return self.local_vars

        # If nothing was done at the end, return 2.
        return 2
