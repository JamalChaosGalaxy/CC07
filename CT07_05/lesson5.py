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

import random

digma = []

while len(digma) < 10:
    num = random.randint(1, 10)
    if num not in digma:
        digma.append(num)

print(min(digma))
print(max(digma))

total = sum(digma) ## total sum in the list
length = len(digma) ## returns number of items in the list
avg = total/length
print(avg)

print(sum(digma)/len(digma))


print(digma.index("4"))##
