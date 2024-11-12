str1 = "nishant"
str2=""
for i in range(len(str1)-1,-1,-1):
    str2=str2+str1[i]

print(str2)

# Approach-2
stx2 = str1[::-1]
print("This is reverse string -Approach-2 :", stx2)

stx3 = "".join(reversed(str1))
print("This is reverse string -Approach-2 :", stx3)