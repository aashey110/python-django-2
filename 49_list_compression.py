# # items = [1,2,3,4,5,6,7,8,9,10]

# # new_list = [item+1000 for item in items]
# # print(new_list)


# # new_list1 = []
# # for item in items:
# #     new_list1.append(item+1000)

# # print(new_list1)

# items = [1,2,3,4,5,6,7,8,9,10]

# even_item = []
# odd_item = []
# for item in items:
#     if item % 2 == 0:
#         even_item.append(item)
#     else:
#         odd_item.append(item)
# print(f"The even items are: {even_item}")
# print(f"The odd items are: {odd_item}")


data = ['apple', 'ball', 'cat', 'dog', 'ball', 'cat']
new_data = []

# if 'ball' in data:
#     data.remove('ball')
#     print(data)

for item in data:
    if item in new_data:
        pass
    else:
        new_data.append(item)

print(new_data)