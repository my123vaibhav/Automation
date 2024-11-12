def decor(fun):
    def inner():
        print("If : Before enhancing function")
        fun()
        print("If : After enhancing function")

    return inner()


def num():
    print("This is 1")
    print("This is 2")


decor(num)
print("---------------------------------")


# by using @

def decor2(fun2):
    def inner2():
        print("If : Before enhancing function")
        fun2()
        print("If : After enhancing function")

    return inner2()


@decor2
def num2():
    print("This is 1")
    print("This is 2")
    print("This is 3")


num2

print("---------------------------------")


# another example:
def decor3(num):
    def inner():
        a = num()
        add = a + 5
        return add

    return inner


@decor3
def num():
    return 10


print(num())
