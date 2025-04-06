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

import turtle

window = turtle.Screen()    
window.setup(600,600)   

window.bgcolor("green") 
pen = turtle.Turtle() 
pen.penup() 

def square():
    turtle.forward(20)
    turtle.left(90)

window.mainloop()