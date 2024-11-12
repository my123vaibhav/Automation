num = 153
original = num
rev = 0
rem = 0

while num > 0:
    rem = num % 10
    rev = rev + (rem * rem * rem)
    num = int(num / 10)
print(rev)
