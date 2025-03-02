# # print("Hello from lesson 6")

# contacts = []
# contact1 = ["John", 98453126, "john@gmail.com"]
# contact2 = ["Adam", 93029102, "adam@gmail.com"]
# contact3 = ["Sylvia", 87894032, "sylvia@gmail.com"]

# contacts.append(contact1)
# contacts.append(contact2)
# contacts.append(contact3)

# for contact in contacts:
#     for i in contact:
#         print(i)

students = [
    ["Olivia", "F"], ["Noah", "M"], ["Emma", "F"],
    ["Liam", "M"], ["Ava", "F"], ["Ethan", "M"],
    ["Sophia", "F"], ["Lucas", "M"], ["Mia", "F"],
    ["Aiden", "M"], ["Isabella", "F"], ["Jackson", "M"],
    ["Amelia", "F"], ["Logan", "M"], ["Lily", "F"]
]
girl = []
boy = []

for student in students:
    name, gender = student
    print("The gender of " + name + " : " + gender)

for student in students:
    name, gender = student
    if gender == "F":
        girl.append(name)
    elif gender == "M":
        boy.append(name)

for name in girl:
    print(name)
for name in boy:
    print(name)

num_boy = len(boy)
num_girl = len(girl)

print(num_girl)
print(num_boy)

print(boy, girl)

for boy in boy:
    print(boy[0])
for girl in girl:
    print(girl[0])

