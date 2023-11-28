print(range(10))
print(type(range(10)))
print(list(range(100)))

for i in range(11):
    print(i)

for i in range(5, 45, 10):
    print(i)

for _ in range(10):
    print("Python")

for i in range(1, 6):
    for j in range(1, 6):
        print(i * j)

c = 1
for i in range(10):
    if i % 2 == 0:
        pass
    else:
        print(i)
    if i % 2 == 1:
        continue
    if i == 7:
        break
    print(i)
