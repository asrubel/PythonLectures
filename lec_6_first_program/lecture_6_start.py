a = 10240000000000
b = 10240000000000
c = 10240000000000

print(id(a))
print(id(b))
print(id(c))

my_str = "python"
another_str = "python"

print(id(my_str))
print(id(another_str))

new_str = my_str + " 3.11"
print(id(new_str))

# new_str[0] = "j"
print(new_str[4])

a = 41
b = 2

if a <= 10:
    a = a + 100
    if b > 3:
        a += b
        # a = a + b

elif a <= 20:
    a += 100

elif a <= 30:
    a += 1000

elif a <= 40:
    a += 1_000_000

else:
    a -= a
    # a = a - a
    if b < 3:
        a *= b
        # a = a * b

print(a)
