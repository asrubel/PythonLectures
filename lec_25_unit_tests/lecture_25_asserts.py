user_input = input("Enter a word: ")
assert user_input != "python"
print("Your input was", user_input)

user_input = input("Enter a word: ")
message = "Wrong word!"
assert user_input != "python", message
print("Your input was", user_input)

try:
    user_input = input("Enter a word: ")
    message = "Wrong word!"
    assert user_input != "python", message
    print("Your input was", user_input)
except AssertionError as error:
    print(error)

x = 3
y = 5
assert (x ** 3 / y ** 2) - 2 * x == 2, "Wrong answer"
print((x ** 3 / y ** 2) - 2 * x)


def test_number(n):
    msg = "A small number"
    assert n > 100, msg
    return n


print(test_number(99))
print(test_number(101))
