def dec_fun(myfunction):
    def wrapper():
        print("Testing Function")
        print("Testing Function2")

        myfunction()

    return wrapper


@dec_fun
def fun1():
    print("This is function1")
    print("This is function2")


fun1()
