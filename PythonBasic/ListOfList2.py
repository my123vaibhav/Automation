li = [1, 2, 3, [5, 6, 10], 7, 8, [9, 10], 11]
var1 = 0


def list_Addition():
    global var1
    for num in li:
        if type(num) == list:
            for i in num:
                var1 = var1 + i
        else:
            var1 = var1 + num


list_Addition()
print(var1)
