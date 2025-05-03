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

# import random
# number = random.randint(1, 100)

# while True:
#     guess = int(input("What is your guess number from 1 to 100? "))
#     if guess > number:
#         print("Too big")
#     elif guess < number:
#         print("Too small")
#     else:
#         print("You are correct!")
#         break             

import random     
score = 0
options = ['Rock', 'Paper', 'Scissors']


computermove = random.choice(options)
playermove = str(input("What is your chosen move?"))
if not playermove in options:
    print("Invalid Move")

def determine_winner(computermove, playermove):
    if (playermove == 'Paper' and computermove == 'Rock'):
        print("You win")
    elif(playermove == 'Rock' and computermove == 'Scissors'):
        print("You win")
    elif(playermove == 'Scissors' and computermove == 'Paper'):
        print("You win")
    elif(playermove == 'Paper' and computermove == 'Scissors'):
        print("You lose")
    elif(playermove == 'Rock' and computermove == 'Paper'):
        print("You lose")
    elif(playermove == 'Scissors' and computermove == 'Rock'):
        print("You lose")

determine_winner(computermove, playermove)