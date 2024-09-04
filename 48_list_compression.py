# items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list2 = [item for item in items if item%2 == 0]
# print(list2)


list_item = [1, 2, 3, 4, 5]

# square_of_list = []

# for item in list_item:
#     square_of_list.append(item*item)

# print(square_of_list)

for item in list_item:
    square_item = [item**2 for item in list_item ]

print(square_item)