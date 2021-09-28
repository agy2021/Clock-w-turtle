from turtle import *
import datetime
import os
from platform import system
from time import sleep

print("Note: the clock might be off and then skip a few seconds. This is because of the animation.")
title("Clock made with Turtle")

hideturtle()

style = ("Courier", 28)

bgcolor("black")
color("lightblue")

write("Welcome! The date is ", font=style, align="right")

color("blue")
write(datetime.datetime.now().strftime("%B %d, %Y"), font=style, align="left")

print("\nTurtle window sucessfully opened. Starting Clock...")
print("Clearing this terminal in 2 seconds...")

sleep(2)

platform = system()

if platform == "Windows":
    os.system("cls")
else:
    os.system("clear")

while True:   
    hideturtle()

    reset()

    hideturtle() 
    bgcolor("black")
    color("white")

    style = ('Courier', 70, 'italic')

    write(datetime.datetime.now().strftime("%I:%M:%S")+ datetime.datetime.now().strftime(" %p"), font=style, align="center")

    penup()

    #positioning the turtle
    color("blue")
    speed(100)
    hideturtle()
    left(180)
    forward(230)
    left(180)

    #drawing the underline
    hideturtle()
    pendown()
    speed(6)

    forward(470)

    pencolor("light blue")
    penup()

    hideturtle()
    speed(100)
    left(90)
    forward(80)
    left(90)

    pendown()
    speed(6)
    forward(460)

    sleep(0.1)
