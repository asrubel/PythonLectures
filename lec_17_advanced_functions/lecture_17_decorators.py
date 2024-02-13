import time


def out_decorator(some_fun):
    def wrapper(args_for_some_fun):
        print('Before...')
        return some_fun(args_for_some_fun)

    return wrapper


@out_decorator
def my_fun(name):
    print(f"Hello! My name is {name}")


print(my_fun('Oleksii'))


def timer_decorator(fun):
    def wrapper(args_for_fun):
        start = time.time()
        fun(args_for_fun)
        end = time.time()
        print(f"Evaluation time: {end - start}")

    return wrapper


@timer_decorator
def huge_load(n):
    for i in range(n):
        for j in range(n):
            print(i * j)


@timer_decorator
@out_decorator
def small_load(n):
    for i in range(n):
        print(i)


small_load(10)
# huge_load(1000)
