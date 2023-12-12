my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list)

gen_list = [i for i in range(1, 10)]
print(gen_list)

gen_list = [i ** 2 for i in range(1, 10)]
print(gen_list)

gen_tuple = (i for i in range(1, 10))
print(gen_tuple)
print(next(gen_tuple))
print(next(gen_tuple))
print(next(gen_tuple))
print(next(gen_tuple))
print(next(gen_tuple))
for i in gen_tuple:
    print(i)
print(next(gen_tuple))
