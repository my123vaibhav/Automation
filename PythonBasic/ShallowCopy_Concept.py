import copy

# In deep deepcopy concept , original list work as adhard card ,then can't change
# In deep copy any changes to copy of object do not reflect the original object
li = [1, 3, 7, 4, 22]

de_li = li.copy()
print("1D_status of copy li is :", de_li)
print("1D_status of Original list- li is :", li)
de_li[1] = 200
print("1D_status of  copy li is for update :", de_li)
print("1D_status of Original list- li is for update :", li)

de_li.append([32, 23, 55])
print("1D_status of copy li is for appending :", de_li)
print("1D_status of Original list- li is for appending :", li)

li2 = [[20, 40, 50], [11, 55, 33]]
de_li2 = li2.copy()
print("2D_status of copy li2 is :", de_li2)
print("2D_status of Original list- li2 is :", li2)

de_li2[1][1] = 77
print("2D_status of copy li2 is for update :", de_li2)
print("2D_status of Original list- li2 is for update :", li2)
de_li2.append([32, 23, 55])
print("2D_status of copy li2 is for appending :", de_li2)
print("2D_status of Original list- li2 is for appending :", li2)

de_li2.remove([20,40,50])

print("2D_status of copy li2 is for removing :", de_li2)
print("2D_status of Original list- li2 is for removing :", li2)


