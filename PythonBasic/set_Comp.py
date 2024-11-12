# Normal set create with new update value
set1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
new_set = set()

for i in set1:
    new_set.add(i * 2)
print(new_set)
print(type(new_set))

print("-------------------------------------")
# set compression
set2 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
new_set2 = {i * 2 for i in set2}
print(new_set2)
print(type(new_set2))

# set with if conditions
print("-------------------------------------")
set3 = set()
for i in range(10):
    if i % 2 == 0:
        set3.add(i)
print(set3)
print(type(set3))

print("-------------------------------------")
# set comp with if conditions

set4 = {i for i in range(10) if i % 2 == 0}
print(set4)
print(type(set4))

# set comp with 2 times if conditions
print("-------------------------------------")
set5 = {i for i in range(20) if i % 2 == 0 if i % 3 == 0}
print(set5)
print(type(set5))

# set comp with if else
set_ifelse = {i if i % 2 == 0 else i*10000 for i in range(20)}
print("if else output :",set_ifelse)
print(type(set_ifelse))
