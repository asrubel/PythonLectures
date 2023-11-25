class ContextClass:

    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")

    def my_method(self):
        print(self)


with ContextClass() as cc:
    cc.my_method()
