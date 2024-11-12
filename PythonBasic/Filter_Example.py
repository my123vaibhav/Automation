mark_list = [1, 2, 4, 5, 6, 78, 22, 34, 54, 65, 77]

result = list(filter(lambda x: x >= 60, mark_list))
for a in result:
    print(a)