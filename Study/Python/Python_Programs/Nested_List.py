# Normal for loop
lst1 = []
count = 0
for i in range(6, 8):
    count = count + 1
    for j in range(4, 7):
        lst1.append(i * j)

print(lst1)
print("---------------------------------------------------")
lst2 = [[i * j for j in range(4, 7)] for i in range(6, 8)]
#       inner loop                   outer loop
print(lst2)