# def is_palindrome(word):
#     # Remove spaces and convert to lowercase for case-insensitive comparison
#     word = word.replace(" ", "").lower()
    
#     # Check if the word is equal to its reverse
#     if word == word[::-1]:
#         return "Yes"
#     else:
#         return "No"

# # Test the function
# word = input("Enter a word: ")
# print(is_palindrome(word))


# Input Processing

# skill = []
# isCorrect = False

# userInput = input("What has to be broken before you can use it?")
# userInput = userInput.lower
# userInput.split()
# skill.append(userInput)

# for word in skill:
#     if word == "egg":
#         isCorrect = True

# if isCorrect == True:
#     print("Correct! Well done")
# else:
#     print("That's not correct. Try Again")


# Correct answer:
# userInput = input("What must be broken in order to be used?")

# isCorrect = False

# lowercase_userInput = userInput.lower()
# splitted_input = lowercase_userInput.split()

# for word in splitted_input:
#     if word == "egg":
#         isCorrect = True

# if isCorrect:
#     print("Correct!")
# else:
#     print("Wrong")

# Turtle
import turtle
window = turtle.Screen()    

window.setup(600,600)   

window.bgcolor("green") 

pen = turtle.Turtle() 
pen.penup() 

pen.shape("square")
pen.sety(250) 
pen.fillcolor("black")  
for i in range(-290,310,25):
    pen.setx(i)
    pen.stamp()

pen.goto(-300,-250)
pen.color("yellow")
pen.pendown()
pen.seth(0)
pen.forward(600)
pen.hideturtle()

Sally = turtle.Turtle()
Sally.penup()
Sally.seth(90)
Sally.shape("turtle")
Sally.color("red")
Sally.goto(0, -250)
Sally.write("Sally", align="center", font=("Ariel",20))

Bob = turtle.Turtle()
Bob.penup()
Bob.seth(90)
Bob.shape("turtle")
Bob.color("blue")
Bob.goto(-200,-250)
Bob.write("Bob", align="center", font=("Ariel",20))

Keith = turtle.Turtle()
Keith.penup()
Keith.seth(90)
Keith.shape("turtle")
Keith.color("white")
Keith.goto(200,-250)
Keith.write("Keith", align="center", font=("Ariel",20))

guess = input("Guess the winner!")

# pen.speed(10)
# pen.seth(0)

# pen.pendown()

window.mainloop()