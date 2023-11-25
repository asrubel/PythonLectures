print('Python \'3.11\'')
print("Python \"3.11\"")

print('Python "3.11"')
print("Python '3.11'")

my_str = 'Python, version "3.11"'
print(id(my_str))
print(my_str)
new_str = my_str.replace('1', '2')
print(id(new_str))
print(new_str)

print(my_str.lower())
print(my_str.upper())

print(my_str.capitalize())
print(my_str.title())
print(my_str.swapcase())

redundant_str = "    dfgdfg   "
print(redundant_str.lstrip())
print(redundant_str.rstrip())
print(redundant_str.strip())

redundant_str = "isisisdfgdfgisisisis"
print(redundant_str.lstrip('is'))
print(redundant_str.rstrip('is'))
print(redundant_str.strip('is'))

redundant_str = "Mississippi"
print(redundant_str.lstrip('ips'))
print(redundant_str.rstrip('ips'))
print(redundant_str.strip('Mips'))

print("abc" not in "abcdefgh")
print("abcd".startswith("ab"))
print("abcd".endswith("cd"))

some_str = "pythonyth"
print(some_str.find("yth", 5))
print(some_str.index("y"))

print(some_str.count("y"))
print(some_str.count("yth"))

user_input = input()
print(user_input.split())
