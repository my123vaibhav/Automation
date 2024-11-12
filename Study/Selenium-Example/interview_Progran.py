# defining a decorator
def python_decorator(func):
    def wrapper():
        print("Text before calling the function")
        func()
        print("Text after calling the function")

    return wrapper


def tutorials_decorator():
    print("Hello tutorials Point!!!")


tutorials_decorator = python_decorator(tutorials_decorator)
tutorials_decorator()
