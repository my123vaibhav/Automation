li = [1, 2, 3, [5, 6, 10], 7, 8, [9, 10], 11]

sum1 = 0
for num in li:
    if type(num) == list:
        for i in num:
            sum1 = sum1 + i
    else:
        sum1 = sum1 + num

print(sum1)
