given_list = [x for x in range(5)]
print(given_list)

new_list = [var+3 for var in given_list]

print(new_list)

#dict
given_list = [x for x in range(5)]
print(given_list)

#new_list = [var+3 for var in given_list]
new_dict = {var:var + 3 for var in given_list }

print(new_dict)

list1 = [x for x in range(5)]
list2 = ['Mon','Tue','Wed','Thu','Fri']
print(list1)
print(list2)

new_dict =dict(zip(list1, list2))

print(new_dict)

given_set = {x for x in range(5)}
print(given_set)

new_set = {var+3 for var in given_set}

print(new_set)