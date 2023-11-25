my_list = ['java', 'kotlin', 'python', 'C++', 'C#']
print(", ".join(my_list))
my_list.append('Dart')
my_list.append('Swift')
my_list.append('Rust')
print(", ".join(my_list))

my_list.extend(['C', 'Pascal', 'Haskell'])
print(my_list)

my_list.remove("Pascal")
print(my_list)
del my_list[0]
print(my_list)

for i in range(5):
    print(my_list.pop())

print(my_list)
print(my_list.pop(0))
print(my_list.pop(1))
print(my_list)

for el in my_list:
    print(el)

that_list = my_list
print(my_list)
print(len(my_list))
empty_list = []
print(len(empty_list))
print(my_list[0])
print(my_list[-1])
print(my_list[-len(my_list)])
print(my_list[8])
my_list[0] = 'Java'
print(my_list)
print(that_list)

letters_list = list('python')
print(letters_list)
print(len(letters_list))
