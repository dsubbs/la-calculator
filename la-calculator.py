import math, os
from Expression import Expression

local_vars = {}

while True:
    try:
        text = input()

        local_vars_temp = local_vars
        expr = Expression(text, local_vars_temp)
        local_vars_temp = expr.Render()

        # Check for traceback codes and render them.
        if local_vars_temp == 1:
            os._exit(1)
        elif local_vars_temp == 2:
            print("Something went wrong with the code.")
            raise WrongExpression
        else:
            local_vars = local_vars_temp

        print(local_vars)
    except Exception as exception:
        print(type(exception).__name__)
        print("Illegal expression, try again")
