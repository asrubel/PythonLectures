# Iterable
my_list = [1, 2, 3, 4]
my_str = "Python"
my_tuple = (1, 2, 3, 4)

for i in my_list:
    print(i)

for l in my_str:
    print(l)

for i in my_tuple:
    print(i)

my_set = {1, 2, 3}
for i in my_set:
    print(i)

my_dict = {"key1": 100, "key2": 200, "key3": 300}
for k in my_dict:
    print(k)
for v in my_dict.values():
    print(v)

for i in my_dict.items():
    print(i)
for k, v in my_dict.items():
    print(k, v)
