# Draw a colorful square using Python Turtle

import turtle

# Create screen
screen = turtle.Screen()
screen.bgcolor("lightblue")   # Background color

# Create turtle object
pen = turtle.Turtle()

# Customize turtle
pen.color("darkblue")         # Line color
pen.fillcolor("yellow")       # Fill color
pen.pensize(4)
pen.speed(3)

# Start filling the square
pen.begin_fill()

# Draw square
for i in range(4):
    pen.forward(150)
    pen.right(90)

# End filling
pen.end_fill()

# Hide turtle
pen.hideturtle()

# Keep window open
turtle.done()