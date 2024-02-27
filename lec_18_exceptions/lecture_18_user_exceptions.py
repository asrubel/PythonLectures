class NegativeResultError(Exception):
    def __init__(self, num):
        self.message = f"The result is negative! Result = {num}"
        super().__init__(self.message)

    def __str__(self):
        # return "Negative number!"
        return self.message


def num_div(x, y):
    if y == 0:
        raise ZeroDivisionError("The second number is zero!")
    elif y < 0:
        # raise Exception(f"The second number is negative! y = {y}")
        raise NegativeResultError
    else:
        return x / y


def try_fun(x, y):
    try:
        res = x / y
        if res < 0:
            raise NegativeResultError
        else:
            print(res)
    except NegativeResultError:
        print("Negative result!")


def exception_example(x, y):
    try:
        if y < 0:
            raise NegativeResultError(y)
        else:
            return x / y
    except NegativeResultError as error:
        print(error)


print(num_div(2, 5))
print(num_div(3, -5))

print(try_fun(2, 5))
print(try_fun(3, -5))

print(exception_example(2, 5))
print(exception_example(3, -5))
