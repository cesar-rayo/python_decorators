import functools


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Running decorator")
        main_dummy = args[0].dummy
        value = main_dummy.do_something()
        print("Inside decorator {}".format(value))
        print("Finish")
        return func(*args, **kwargs)
    return wrapper


def my_decorator2(num_times):
    def decorator2(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(num_times):
                print("{}. Running decorator2".format(i))
                main_dummy = args[0].dummy
                value = main_dummy.do_something()
                print("{}. Inside decorator {}".format(i, value))
                print("{}. Finish".format(i))
            return func(*args, **kwargs)
        return wrapper
    return decorator2


def my_decorator3(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Running decorator3")
        print(args[0].variable)
        print("Finish")
        return func(*args, **kwargs)
    return wrapper
