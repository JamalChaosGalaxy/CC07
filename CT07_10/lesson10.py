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

import turtle

t = turtle.Turtle()
size = 30

def drawSquare(x, y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for i in range(2):
        t.forward(30)
        t.left(90)

while True:
    x = input("Enter x coordinate: ")
    y = input("Enter y coordinate: ")
    size = input("How ")

turtle.mainloop()