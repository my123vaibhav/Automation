# Natural Number >1
# Which has only 2 factor 1 and itself
#
# 19 => 1 and 19 =>Prime Number
# 28 => 1,2,3,7,14,28 => Not a prime number

num1 = int(input("Enter the number :"))
count = 0
if num1 > 1:
    for i in range(1, num1 + 1):
        if num1 % i == 0:
            count = count + 1
    if count == 2:
        print("This is a prime number :",num1)
    else:
        print("Number is not prime :",num1)
