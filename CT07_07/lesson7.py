# # # # # # print("Hello from lesson 7")

# # # # # students = []
# # # # # student1 = ["Eliot", "34528375", "Basketball"]
# # # # # student2 = ["James", "23453665", "Badminton"]
# # # # # student3 = ["Peter", "73465345", "Football"]

# # # # # students.append(student1)
# # # # # students.append(student2)
# # # # # students.append(student3)

# # # # # for student in students:
# # # # #     name, phonenum, cca = student
# # # # #     print("Name: " + name)
# # # # #     print("Phone number: " + phonenum)
# # # # #     print("CCA:" + cca)

# # # # list1 = ["Apple", "Banana", "Cherry"]
# # # # list2 = ["Durian", "Elderberry", "Figs"]

# # # # fruits = list1 + list2
# # # # print(fruits)

# # # list1 = [3.20, 2.65, 1.75]
# # # list2 = [6.15, 5.45, 4.20]

# # # total = list1 + list2
# # # print("Before sort: ", total)
# # # sorted_price = sorted(total)
# # # print("After sort: " ,sorted_price)

# # fruits = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Figs"]
# # # index = 3

# # # left = fruits[:index]
# # # right = fruits[index:]
# # # print(left)
# # # print(right)
# # # print(fruits)
# # # print(len(fruits))

# # # To slice the fruits list into two halves using the midpoint
# # print(fruits[0:3])
# # print(fruits[3:])

# list1 = ["Apple", "Banana", "Cherry", "Durian"]
# list2 = ["Cherry", "Durian", "Elderberry", "Figs"]
# common = []

# for item in list1:
#     for item2 in list2:
#         if item == list2:
#             common.append(item)
#             # break

# print(common)

# list1 = ["Apple", "Banana", "Cherry", "Durian"]
# list2 = ["Cherry", "Durian", "Elderberry", "Figs"]

# unique = []

# merged_list = list1 + list2

# print(merged_list)

# for item in merged_list:
#     if item not in unique:
#         unique.append(item)

# print(unique)


# My method
# for item in list1:
#     for item2 in list2:
#         if item2 not in list1:
#             unique.append(item2)

# list1.append(unique)
# print(unique)

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]


