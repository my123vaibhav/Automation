add = lambda x=10: (lambda y: x + y)

a = add()
print(a(20))

print("-----------------------------")


# Passing Lambda Function to another Function in Python
def show(a):
    print(a(8))


show(lambda x: x * x)

print("----------------------------")


# Returning Lambda Function from a Function in Python
def add():
    y = 20
    return lambda x: x + y


a = add()
print(a(10))
