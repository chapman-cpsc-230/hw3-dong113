
"""
File: turtle_poly.py
Copyright (c) 2016 Lisa Dong
License: MIT
-asks user for number of sides and the length of each side.
-this is converted from a string to an int
-a turtle is created
-using while loops, the turtle is guided to make a polygon using the user's input
"""    

import turtle

s = raw_input("enter number of sides :")
l = raw_input("enter length of each side: ")

n = int(s)
side_len = int(l)

squirtle = turtle.Pen()

for i in range (n):
    squirtle.forward(side_len)
    squirtle.right(360/n)


everstone = raw_input("hit enter to exit: ")

turtle.bye()
