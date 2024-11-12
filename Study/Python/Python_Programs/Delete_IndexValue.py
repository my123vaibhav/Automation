mylist = ["kkc", "skb", "IPL", "RCB", "KKR", "HYD", "nmn"]
n = 2
count = 1
for i in range(len(mylist)-1):
    print(i, mylist[i])
    if mylist[i] == "RCB":
        count = count + 1
        if count == n:
            print("Before delete the list is:",mylist)
            del mylist[i]

print(mylist)

