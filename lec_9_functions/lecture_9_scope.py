my_var = "Python"


def my_fun():
    global my_var
    my_var = "Java"
    print(my_var)


my_fun()
my_fun()
my_fun()
my_fun()

print(my_var)

# LEGB rule
# Local
# Enclosing
# Global
# Built-in

x = "global"


def outer():
    # x = "enclosing"

    def inner():
        # x = "local"
        print(x)

    inner()
    print(x)


outer()

print(x)
