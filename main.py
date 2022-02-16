from helpers.decorators import my_decorator, my_decorator2, my_decorator3
from dummy import Dummy


class MainClass:
    variable = "Class variable"

    @my_decorator3
    def __init__(self, value):
        self.dummy = Dummy(value)

    @my_decorator
    def method1(self, value):
        print("Main class method 1 [{}] => {} ".format(self.dummy.do_something(), value))

    @my_decorator2(num_times=3)
    def method2(self, value):
        print("Main class method 2 => {} ".format(value))


if __name__ == "__main__":
    main = MainClass("Dummy Main")
    main.method1("method1")
    print("====================")
    main.method2("method2")
