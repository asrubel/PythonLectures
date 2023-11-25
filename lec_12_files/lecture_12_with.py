with open("my_text.txt", "w") as file:
    file.write("Python!!!")

print("The end")

n = 1_000
files = []

for i in range(n):
    with open("my_text.txt", "r") as f:
        files.append(f)

print(files)

with open("groups.txt", "r") as input_file, \
        open("my_text.txt", "w") as output_file:
    for line in input_file:
        output_file.write(line)
