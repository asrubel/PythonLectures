empty_tuple = ()
another_tuple = tuple()

print(id(empty_tuple))
print(id(another_tuple))

empty_list = []
another_list = list()

print(id(empty_list))
print(id(another_list))

my_tuple = ('python', 'java', 'kotlin')
print(my_tuple)
print(type(my_tuple))

a, b, c = my_tuple
print(a)
print(b)
print(c)

a = 100
b = 200
print(a, b)
a, b = b, a
# temp = a
# a = b
# b = temp
print(a, b)

print(my_tuple[0])
print(my_tuple[-1])
print(len(my_tuple))

my_list = [1, 2, 3, 4, 5]
empty = tuple(my_list)
print(empty)
for i in empty:
    print(i)
print(empty[0])
