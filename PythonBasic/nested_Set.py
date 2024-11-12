set_ifelse = {i if i % 2 == 0 else i * 10000 for i in range(20)}
print("if else output :", set_ifelse)
print(type(set_ifelse))

##Nested Set Comprehension in Python:
# set is unorder:
st = {(i, j) for j in range(4, 7) for i in range(6, 8)}
print(st)
print(type(st))
