# var1 = 200

# def f():
#     var1 = 500
#     global var2 
#     var2 = 300
#     print("var1: " + str(var1))
#     print("var2: " + str(var2))

# f()
    
# def alert():
#     print("Motion Detected")

# i = 0
# while i < 4:
#     alert()
#     i+=1





# import turtle

# t = turtle.Turtle()

# def square(length):
#     for _ in range(4):
#         t.forward(length)
#         t.left(90)

# def rectangle(width, height):
#     for _ in range(2):
#         t.forward(width)
#         t.left(90)
#         t.forward(height)
#         t.left(90)

# square(20)
# square(50)
# rectangle(40, 60)

# turtle.mainloop()


# def multiply(num1, num2):
#     print(num1 * num2)

# multiply(3, 5)

# import turtle

# t = turtle.Turtle()

# def drawSquare(x, y, size):
#     turtle.penup()
#     turtle.goto(x,y)
#     turtle.pendown()
#     for i in range(4):
#         t.forward(30)
#         t.left(90)

# while True:
#     x = input("Enter x coordinate: ")
#     y = input("Enter y coordinate: ")
#     size = input("How big do you want the square to be: ")
#     drawSquare(int(x), int(y), size)

# turtle.mainloop()

# Return in funcitons

# def add(x, y):
#     return x + y

# sum = add(10, 15)
# print(sum)

# def isElderly(age):
#     if age >= 65:
#         print("You are eligible for the elderly discount.")
#     else:
#         print("You are not eligable for the elderly discount/")

# age = int(input("What is your age? "))  
# isElderly(age)

# def isElderly(age):
#     if age >= 65:
#         return 1
#     return 0

# age = int(input("What is your age? "))  
# if isElderly(int(age)):
#     print("You are eligible for the elderly discount.")
# else:
#     print("You are not eligable for the elderly discount/")


# import turtle

# t = turtle.Turtle()
# size = 30

# def drawSquare(x, y):
#     turtle.penup()
#     turtle.goto(x,y)
#     turtle.pendown()
#     for i in range(4):
#         t.forward(40)
#         t.left(90)

# def turtleCoord(turtle_obj):
#     x = turtle.xcor()
#     y = turtle.ycor()
#     return x,y

# drawSquare(-50,50)
# x,y = turtleCoord(t)
# print("Turtle coordinates: " + str(x) + " , " + str(y))

# turtle.mainloop()

# def whatsappMe(phonenum):
#     return "Whatsapp me at https://wa.me/" + phonenum

# phonenum = input("Enter number: ")
# print(whatsappMe(phonenum))



# import random()

# list = []
# def randgen(num):
#     num = int(input("How many times do you want to shake the hat?"))
#     return num

# randgen(num)
# for i in range(num):
#     randomnumber = random.randint(1, 100)
#     list.append(randomnumber)

# total = len(list)
# big = max(list)
# small = min(list)
# average = sum(list) / len(list)

# print ("Total amount of numbers in the list: " + total)
# print ("Biggest number:  " + big)
# print ("Smallest number: " + small)
# print ("Average: " + average)



# import random

# def randgen():
#     num = int(input("How many times do you want to shake the hat? "))
#     return num

# num = randgen()  # Call the function and store the result in 'num'

# random_numbers = []  # List to store random numbers

# # Generate random numbers and add them to the list
# for i in range(num):
#     randomnumber = random.randint(1, 100)
#     random_numbers.append(randomnumber)

# # Calculate statistics
# total = len(random_numbers)
# big = max(random_numbers)
# small = min(random_numbers)
# average = sum(random_numbers)

# # Print results
# print(f"Total amount of numbers in the list: {total}")
# print(f"Biggest number: {big}")
# print(f"Smallest number: {small}")
# print(f"Average: {average}")

move = ["rock", "paper", "scissors"]
import random


def generate_comp_move():
    comp_move = int(random.randint(move))
    return comp_move

def determine_winner(player_move, comp_move):
    if player_move == comp_move:
        print("Tie")
    elif player_move == "rock" and comp_move == "scissors":
        print("Win")
    elif player_move == "paper" and comp_move == "rock":
        print("Win")
    elif player_move == "scissors" and comp_move == "paper":
        print("Win")
    elif player_move == "rock" and comp_move == "paper":
        print("Lose")
    elif player_move == "paper" and comp_move == "scissors":
        print("Lose")
    elif player_move == "scissors" and comp_move == "rock":
        print("Lose")

while True:
    player_move = str(input("What is your chosen move?"))

    if player_move not in move:
        print("Move is not valid")

    comp_move = generate_comp_move

    # print("Computer's move : " + comp_move)
    # print("Player's move: " + player_move)


    # def determine_winner():
        

