####----------Challenge 4 Bonus----------#####
import turtle
pen = turtle.Turtle()
pen_width = int(input("Enter the pen thickness: "))
pen_color = input("Enter the pen color: ")
pen.width(pen_width)
pen.color(pen_color)
for i in range(50):
    pen.forward(100)
    pen.left(100)
    
    pen.circle(100)
turtle.done()