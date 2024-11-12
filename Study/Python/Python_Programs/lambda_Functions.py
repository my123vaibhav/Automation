data1 = lambda x,y:(x*y,x+y)
a, b = data1(10, 20)

print(a)
print(b)

print("--------------------------------")

data2 = lambda x,y=5:(x*y)
print(data2(5))

a = lambda x:x+1
print(a(5))



