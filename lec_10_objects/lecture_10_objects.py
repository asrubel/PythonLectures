class Student:
    name = "Bob"

    def my_method(self):
        print('My method')


class MyClass:
    ...


# Class property
print(Student.name)
student = Student()
print(student.name)
student.my_method()


class Book:
    material = "paper"
    cover = "solid"
    all_books = []


# Using list as property
print(Book.cover)
print(Book.material)
print(Book.all_books)

my_book = Book()
print(my_book.cover)
print(my_book.material)
print(my_book.all_books)

my_book.all_books.append("Clean architecture")
print(my_book.all_books)
print(Book.all_books)

my_book.cover = "soft"
print(my_book.cover)
print(Book.cover)
