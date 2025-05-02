# import random
# health = 100;

# battles = 0
# i = 0
# print(f"Hero starts on his adventure with Health: ", health)
# while health > 0:
#     damage = random.randint(1,15)
#     health -= damage
#     if health < 0:
#         break
#     print("After finishing monsters, his health is now", health)
#     i += 1
#     battles += 1
        

# print(f"He fought", battles, "battles, and died")

# i = 1
# order = []
# while True:
#     question = input("What would like to order?(Type 'end' if you wish to stop)")
#     order.append(question)
    
#     if question == "end":
#         break

# print("You have ordered the following:")
# for food in order:
#     print(i,".", food)
#     i += 1
    
    
# word = "peanut"
# i = 0
# while i < 10:
# 	print(word[i])


registration_plate = input("What is your resgistration plate?")
Body = registration_plate.split(",")

Numbers = []
Letters = []

for stuff in Body:
    if stuff.isdigit:
        Numbers.append(stuff)
    if stuff.isalpha:
        Letters.a