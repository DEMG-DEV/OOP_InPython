from turtle import Turtle
from random import randint

turtle1 = Turtle()

turtle1.color('red')
turtle1.shape('turtle')

turtle1.penup()
turtle1.goto(-160, 100)
turtle1.pendown()

turtle2 = Turtle()

turtle2.color('green')
turtle2.shape('turtle')

turtle2.penup()
turtle2.goto(-160, 70)
turtle2.pendown()

turtle3 = Turtle()

turtle3.color('blue')
turtle3.shape('turtle')

turtle3.penup()
turtle3.goto(-160, 40)
turtle3.pendown()

turtle4 = Turtle()

turtle4.color('pink')
turtle4.shape('turtle')

turtle4.penup()
turtle4.goto(-160, 10)
turtle4.pendown()

for movement in range(100):
    turtle1.forward(randint(1, 5))
    turtle2.forward(randint(1, 5))
    turtle3.forward(randint(1, 5))
    turtle4.forward(randint(1, 5))

input('Press Enter to Close')
