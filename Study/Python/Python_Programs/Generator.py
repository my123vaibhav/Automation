# Initialize the list
test_list = [1, 3, 6, 10]
# list comprehension
list_comprehension = [x**3 for x in test_list]
# generator expression
test_generator = (x**3 for x in test_list)
print(test_generator)
print(type(test_generator))
print(tuple(test_generator))