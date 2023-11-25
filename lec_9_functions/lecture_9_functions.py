def my_fun(par1, par2):
    """My function: adding two numbers"""
    print(par1, par2)
    return par1 + par2


def empty_fun():
    # TODO - Write function body
    pass


print("Hello!", "This is KhAI Python course!", sep="\n", end="\n##############\n")
res1 = my_fun(10, 20)
res2 = my_fun(15, 25)

print(res1)
print(res2)
print(my_fun(20, 40))

empty_fun()
