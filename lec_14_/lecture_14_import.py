# import lecture_14_modules
from lecture_14_modules import a, MyClass, my_fun
import package1.module1
import package1.module2
from package2.module1 import Class1
from package2.module2 import Class2


print(__name__)
# print(lecture_14_modules.MyClass())
# print(lecture_14_modules.my_fun(2, 8))
# print(lecture_14_modules.a)

# print(a)
# print(MyClass())
# print(my_fun(10, 5))

# print(package1.module1.my_fun(3))
# print(package1.module2.my_fun(3))

print(Class1())
print(Class2())
