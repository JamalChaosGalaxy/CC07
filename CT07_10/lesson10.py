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


import turtle

t = turtle.Turtle()

def drawSquare(x, y, size):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for i in range(4):
        t.forward(30)
        t.left(90)

while True:
    x = input("Enter x coordinate: ")
    y = input("Enter y coordinate: ")
    size = input("How big do you want the square to be: ")
    drawSquare(int(x), int(y), size)
    break

def turtleCoord(turtle_obj):
    x = turtle.xcor()
    y = turtle.ycor()
    return x,y

drawSquare(-50,50)

turtle.mainloop()

