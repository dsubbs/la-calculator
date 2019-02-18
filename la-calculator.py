import math
from Expression import Expression

local_vars = {}

while True:
    try:
        text = input()
        expr = Expression(text, local_vars)
        expr.Render()
        print(local_vars)
    except:
        print("Illegal expression, try again")
