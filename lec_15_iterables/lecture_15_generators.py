def multi_number(a, n):
    res = []
    i = 1
    while i <= n:
        res.append(a * i)
        i += 1
    return res


def multi_generator(a, n):
    i = 1
    while i <= n:
        yield a * i
        i += 1


print(multi_number(4, 8))
my_gen = multi_generator(4, 8)
print(my_gen)
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))

for el in my_gen:
    print(el)

print(next(my_gen))
