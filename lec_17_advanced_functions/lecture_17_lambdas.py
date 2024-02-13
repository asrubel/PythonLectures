def power_2(x):
    return 2 ** x


func = lambda x: 2 ** x
print(power_2(4))
print(func(4))

func = lambda x, y: (x + y) / 2
print(func(3, 10))


def my_fun(x):
    if x % 2 == 0:
        return 'even'
    else:
        return 'odd'


my_lambda = lambda x: 'even' if x % 2 == 0 else 'odd'
print(my_fun(5))
print(my_lambda(5))

print((lambda x, y: (x + y) ** 3)(3, 10))


def power_fun(x, n):
    return x ** n


def create_fun(n):
    return lambda x: x ** n


pow_2 = create_fun(2)
pow_3 = create_fun(3)
pow_10 = create_fun(10)

print(pow_2(10))
print(pow_3(10))
print(pow_10(10))


def some_logic(m, f):
    print(f(m))


some_logic(3, pow_2)
some_logic(5, pow_3)
some_logic(7, pow_10)
