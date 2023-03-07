from functools import reduce
def multiply(list):
    result = reduce(lambda x, y: x*y, list)
    print(result)
a = [1, 2, 3, 4, 5]
multiply(a)