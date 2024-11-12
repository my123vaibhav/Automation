mylist = ["kkc", "skb", "IPL", "RCB", "IPL", "skb", "nmn"]
print("Before the clear the list is :", mylist)

# Approach1
mylist_copy = mylist[::]
print("Approach1", mylist_copy)

mylist_copy = mylist[::-1]
print("Approach2", mylist_copy)