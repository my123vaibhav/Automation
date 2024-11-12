li = [2, 1, 3, 4, 6, 5, 9, 12]

# Ascending order
for i in range(len(li)):
    for j in range(i + 1, len(li)):
        if li[i] > li[j]:
            temp = li[i]
            li[i] = li[j]
            li[j] = temp

for k in range(len(li)):
    print(li[k], end=" ")
# Descending order
print("")
for i in range(len(li)):
    for j in range(i + 1, len(li)):
        if li[i] < li[j]:
            temp = li[i]
            li[i] = li[j]
            li[j] = temp

for k in range(len(li)):
    print(li[k], end=" ")