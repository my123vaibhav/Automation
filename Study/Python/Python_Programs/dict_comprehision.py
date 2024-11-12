dict1 = {}

for n in range(10):
    if n % 2 == 0:
        dict1[n] = n
    else:
        dict1[n] = "Invalid"
print("Dict print without using compression :", dict1)

print("---------------------------")
dict2 = {n: (n if n % 2 == 0 else 'invalid') for n in range(10)}
print("Dict print using compression :", dict2)
