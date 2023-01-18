from turtle import Screen
import turtle as t
import random

tim = t.Turtle()
tim.speed("fastest")
screen = Screen()
t.colormode(255)

color_list_ocean = [(14, 193, 186), (5, 143, 153), (68, 240, 231), (4, 146, 139), (11, 180, 187),
                    (1, 102, 112), (186, 254, 250), (54, 218, 207), (1, 49, 71), (1, 111, 107),
                    (87, 198, 205), (228, 248, 252), (102, 229, 234), (0, 71, 67), (162, 162, 162),
                    (93, 93, 93), (51, 61, 78), (12, 242, 230)]

tim.penup()
tim.hideturtle()
tim.setpos(-250, -200)


def paint_dots():
    position = -200
    for i in range(10):
        for i in range(10):
            color = random.choice(color_list_ocean)
            tim.dot(20, color)
            tim.forward(50)
        position += 50
        tim.setpos(-250, position)


paint_dots()
screen.exitonclick()
