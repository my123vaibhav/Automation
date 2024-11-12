from array import *

arr = array('i', [2, 4, 5, 6])
print(arr)
print(type(arr))
for i in arr:
    print(i, end=" ")

print("----------------------------")


def show(ar):
    for i in ar:
        print(i)
    return ar


y = show(arr)
print("getting arrays values in below/code:", y)
for x in y:
    print(x,end=" ")
