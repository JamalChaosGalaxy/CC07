# print("Hello from lesson 5")

# import random

# beta = []

# for _ in range(100):
#     num = random.randint(1, 1000)
#     beta.append(num)

# print (num[: 10])

# skibidi = 234

# if num not in beta:
#     print("Yes, its in")
# else:
#     print("no, its not in")

# import random

# digma = []

# while len(digma) < 10:
#     num = random.randint(1, 10)
#     if num not in digma:
#         digma.append(num)

# print(min(digma))
# print(max(digma))

# total = sum(digma) ## total sum in the list
# length = len(digma) ## returns number of items in the list
# avg = total/length
# print(avg)

# print(sum(digma)/len(digma))


# print(digma.index(4))## finds for an int 4
# print(digma.index("4"))## finds for an string 4

# namelist = ["Olivia", "Liam", "Emma", "Noah", "Ava", "Ethan",
#             "Sophia", "Lucas", "Mia", "Aiden"
#             ]
# heightlist = [160, 165, 158, 170, 162, 168, 159, 172, 164, 166]

# tall = max(heightlist)
# print(tall)
# index = heightlist.index(tall)
# print(namelist[index])

# print(namelist[heightlist.index(max(heightlist))])
# print(namelist[heightlist.index(min(heightlist))])
# print(min(heightlist))

##min, max, in , not, append, insert, pop, del, random, index

##Random- .choice

import random

list_num = [1, 2, 3, 4 , 5, 6 , 7]

list_fruits = ["banana", "strawberry", "pears", "apple"]

print(random.choice(list_fruits))

if 2 in list_num:
    print("yes, 2 is stored")
else:
    print("no,")