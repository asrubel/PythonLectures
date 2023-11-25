file = open("groups.txt", "r")
print(file.read())
print(type(file))

print(file.readline(3))
print(file.readline(3))
print(file.readline(3))
print(file.readline(3))

lines = file.readlines()
print(lines)
for line in lines:
    print(line)

file.close()

my_list = ['Java', 'Kotlin', 'C#', 'JavaScript']
my_file = open("my_text.txt", "w", encoding="utf-8")
for lang in my_list:
    my_file.write(lang + '\n')

my_file.write("\n")
my_file.write("Python\n")
my_file.write("KhAI\n")
my_file.write("D://CT\n")
print(my_file.readlines())
my_file.writelines(lines)

my_file.close()
