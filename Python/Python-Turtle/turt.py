"""Turtle example from https://workshops.hackclub.com/python_turtle/
*Slightly modified
"""
import turtle

#Colour Table
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

t = turtle.Pen() #Create pen object
t.speed(11) #Set to max speed
t.shape("turtle") #Cursor shape
turtle.bgcolor('black') #Set background colour

input("Press Enter to start...")

for x in range(360):
    t.pencolor(colors[x%6]) #Colour Repeating pattern of: 0,5,4,3,2,1
    t.width(x/100 + 1) #Increase line thickness
    t.forward(x) #Draw
    t.left(59) #Change angle, Offset to create spiral

t.penup()
t.home()
t.pendown()

for x in range(360):
    t.pencolor(colors[x%5])
    t.width(x/100 + 1) #Increase line thickness
    t.forward(x) #Draw
    t.left(59) #Change angle, Offset to create spiral
