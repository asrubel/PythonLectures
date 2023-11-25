def multiply(first, second, *args):
    print(args)
    res = first * second
    for i in args:
        res *= i
    return res


print(multiply(2, 3, 4, 5, 7, 8, 9))
print(multiply(5, 4, 2, 3))
