def list_Addition2(num):
    var2 = 0
    for i in num:
        var2 = var2 + i
    return var2


li = [1, 2, 3, [5, 6,[4,4],10], 7, 8, [9, 10], 11]
var1 = 0


def list_Addition():
    global var1
    for num in li:
        if type(num) == list:
            for i in num:
                var1 = var1 + i
        else:
            var1 = var1 + num
    return var1


abc = list_Addition()
print(abc)
