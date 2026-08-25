import turtle as t
from turtle import Turtle, Screen
from random import choice
t.colormode(255)
color_list = [(199, 175, 118), (125, 36, 24), (187, 158, 50), (170, 105, 56), (5, 57, 83), (222, 223, 226), (200, 216, 205), (108, 67, 85), (39, 36, 35), (86, 142, 58), (20, 123, 176), (110, 161, 175), (75, 39, 47), (9, 67, 47), (64, 153, 137), (133, 41, 43), (184, 98, 80), (179, 201, 186), (210, 200, 113), (179, 175, 177), (151, 176, 164), (93, 142, 156), (28, 80, 59)]
jin = Turtle()
jin.hideturtle()
jin.speed('fastest')
current_y = 0
for row_count in range(10):
    for i in range(10):
        jin.dot(20, choice(color_list))
        jin.penup()
        jin.forward(50)
    current_y += 40
    jin.goto(0, current_y)
    jin.pendown()

screen = Screen()
screen.exitonclick()
