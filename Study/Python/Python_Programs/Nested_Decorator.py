def decor1(num):
    def inner():
        b = num()
        multi = b * 5
        return multi

    return inner


def decor(num):
    def inner():
        a = num()
        add = a + 5
        return add

    return inner


def num():
    return 10


num = decor(decor1(num))
print(num())
