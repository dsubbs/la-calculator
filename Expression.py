class Expression:

    def __init__(self, expression, local_vars):
        self.expression = expression.strip()
        self.local_vars = local_vars

    def listToDo(operation, toList, fromList):
        if (not operation == "*") or (not operation == "/") or (not operation == "+") or (not operation == "-"):
            raise WrongExpression
        while (operation in fromList):
            toList.append(fromList[:fromList.find(operation) - 1])
            var_cont = fromList[fromList.find(operation) + 2:]
            if not (operation in fromList):
                toList.append(fromList)

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

        var_cont = self.expression[self.expression.find('=') + 1:].strip()

        print("checking for operations")

        result = 1

        vars_sum = []
        vars_minus = []

        # Reverse string to search from the end
        var_cont = var_cont[::-1].strip()


        # THERE MUST BE A WAY


        # DEBUGGING
        print(vars)
        # PRINTING VARS THAT ARE MULTIPLIED

        for elem in vars:
            elem = elem[::-1]
            if self.local_vars.get(elem) == None:
                raise WrongExpression
            else:
                result = result + self.local_vars.get(elem)

        if (not '*' in self.expression) and (not '+' in self.expression):
            result = float(var_cont)

        if ('=' in self.expression):
            print("creating new variable")
            self.local_vars.update({var_name: result})
            return self.local_vars

        # If nothing was done at the end, return 2.
        return 2
