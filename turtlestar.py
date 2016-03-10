
"""
File: turtlestar.py
Copyright (c) 2016 Lisa Dong
License: MIT
-asks user for 2 numbers: points and length.
-converts these strings to int / float
-creates a turtle
-uses a for loop to guide the turtle to create a n-star , using the info user input
"""    



import turtle

n = raw_input("enter an odd number greater than or equal to 5  ")
side_len = raw_input("enter a side length:  ")

points = int(n)
length = float(side_len)

turtwig = turtle.Pen()

for x in range(points):
    turtwig.forward(length)
    turtwig.right((720+180*(points-5))/points)


input = raw_input("press enter to exit" )

turtle.bye()

