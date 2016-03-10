"""
File: repeated_sqrt.py
Copyright (c) 2016 Lisa Dong
License: MIT
-for loop square roots a number, then squares it

the inverse operations should bring you back to same starting value, but doing this repeatedly will eventually cause errors in rounding
after 15 times, the program returns a number slightly larger than the number 2.0
after 25 times, the program returns a value of r that is less than the original number 2.0
        
""" 

from math import sqrt
for n in range(1, 26): #the for loop will square root the variable then square it, 25 times
    r = 2.0
    for i in range(n):
        r = sqrt(r) #square root of variable r
    for i in range(n):
        r = r**2 #square the variable r

    
    print r
