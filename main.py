import colorgram
import turtle as turtle_module
import random

colors = colorgram.extract('image.jpg.jpg', 6)

rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, b, g)
    rgb_colors.append(new_color)



pudge = turtle_module.Turtle()
turtle_module.colormode(255)
pudge.penup()

pudge.left(225)
pudge.forward(125)
pudge.setheading(0)

for y in range(5):
    for x in range(5):
        pudge.dot(20, random.choice(rgb_colors))
        pudge.forward(50)
    pudge.left(90)
    pudge.forward(50)
    pudge.left(90)
    pudge.forward(250)
    pudge.left(180)


screen = turtle_module.Screen()
screen.exitonclick()
