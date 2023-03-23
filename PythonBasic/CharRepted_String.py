def find_word():
    st = "nishant"
    li = st
    li2 = []
    count = 0
    for i in li:
        if i not in li2:
            li2.append(i)

    for j in range(len(li2)):
        print("This is word name :",li2[j], ": count is :",li.count(li2[j]))


find_word()