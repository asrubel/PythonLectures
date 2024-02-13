# 5!
# 5 * 4!
# 5 * 4 * 3!
# 5 * 4 * 3 * 2!
# 5 * 4 * 3 * 2 * 1!
# 5 * 4 * 3 * 2 * 1 * 0!
# 5 * 4 * 3 * 2 * 1 * 1
#
# N! = N * (N - 1)!
import sys


def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)


print(recursive_factorial(10))
print(sys.getrecursionlimit())

print(recursive_factorial(998))
# print(recursive_factorial(999))

sys.setrecursionlimit(2000)
print(recursive_factorial(999))
