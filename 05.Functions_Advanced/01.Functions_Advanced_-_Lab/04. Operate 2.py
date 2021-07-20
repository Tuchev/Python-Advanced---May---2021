from functools import reduce

def operate(operator, *args):
    return reduce(lambda x, y: eval(f"{x} {operator}  {y}"), args)


print(operate("*", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))