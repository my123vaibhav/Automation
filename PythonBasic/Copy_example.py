a = [10, 20, 30]
b = a.copy()
print("A:", a)
print("B:", b)

print("modifying a ")
a[1] = 50
print("A:", a)
print("B:", b)

print("modifying b ")
b[1] = 77
print("A:", a)
print("B:", b)

print("clone concept---------------")

a = [10, 20, 30]
b = a[:]
print("A:", a)
print("B:", b)

print("modifying a ")
a[1] = 50
print("A:", a)
print("B:", b)

print("modifying b ")
b[1] = 77
print("A:", a)
print("B:", b)
