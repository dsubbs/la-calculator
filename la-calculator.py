import math, os
from Expression import Expression

local_vars = {}

while True:
    try:
        text = input()

        # Render the expression with the temporal scope
        local_vars_temp = local_vars
        expr = Expression(text, local_vars_temp)
        local_vars_temp = expr.Render()

        # Check for traceback codes and render them.
        if local_vars_temp == 1:
            os._exit(1)
        elif local_vars_temp == 2:
            print("Something went wrong with the code.")
            raise WrongExpression
        # If everything went fine, assign the temporal scope to the primary one.
        else:
            local_vars = local_vars_temp

        # DEBUGGING
        print(local_vars)
        # PRINTING SCOPE

    except Exception as exception:

        # DEBUGGING
        print(type(exception).__name__)
        # PRINTING EXCEPTION NAME

        print("Illegal expression, try again")
