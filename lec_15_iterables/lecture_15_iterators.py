# __iter__()
# __next__()

my_list = [1, 2, 3, 4]
my_iterator = iter(my_list)
print(my_iterator)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
# print(next(my_iterator))

for item in my_list:
    print(item)

for item in iter(my_list):
    print(item)

for item in my_iterator:
    print(item)

first_names = ['Oleksandr', 'Hanna', 'Kyrylo']
last_name = ['Shevchenko', 'Ivanova', 'Adamenko', 'Petrenko']
for first, last in zip(first_names, last_name):
    print(first, last)

for no, last_name in enumerate(last_name, start=1):
    print(no, last_name)
