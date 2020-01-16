# A program on how to draw and calculate a circle

import turtle
import math
import numpy as np

def choose():
    while True:
        circle = input('Do you want to choose [D]iameter or [R]adius to calculate?:\n').upper()

        if circle not in 'DR' or len(circle) != 1:
            print('Sorry, try again!')
        
        if circle == 'D':
            while True:
                try:
                    diameter = float(input('Enter your your diameter: \n')) # receiving input
                except ValueError:  # if the user insert other than integer, error message will come out
                    print('Sorry, only integers are accepted, try again.')

                else:
                    print('The diameter that you inserted is: {} unit(s)'.format(diameter)) # telling the user the value of their input
                    radius = diameter/2
                    area(radius)
        if circle == 'R':
            while True:
                try:
                    radius = float(input('Enter your your radius: \n')) # receiving input
                except ValueError:  # if the user insert other than integer, error message will come out
                    print('Sorry, only integers are accepted, try again.')

                else:
                    print('The radius that you inserted is: {} unit(s)'.format(radius)) # telling the user the value of their input
                    area(radius)

def draw(radius,sectorarea):
    t = turtle.Turtle() # Object created
    t.penup()
    t.setpos(0,-radius)   # Setting the position
    t.pendown()
    t.circle(radius) # Drawing the circle on canvas

def area(radius):
    # Circumference of a circle
    circumference = 2 * math.pi * radius # The formula of the circumference of a circle
    print('The circumference of the circle {} is {:.2f} unit(s)'.format(radius,circumference)) # Getting input

    # Area of a circle
    areac = math.pi * radius**2 # Formula of the area of a circle
    print('The area of the circle with radius {} is: {:.2f} unit(s)²'.format(radius,areac))

    # Area of a sector
    while True:
        try:
            degree = float(input('Enter the number of degrees in central angle of sector:\n'))
        except:
            print("Wrong input!")
            continue 
        else:
            sector = (degree/360) * math.pi * radius**2
            print('The area of the sector with central angle of {}° is: {:.2f} unit(s)²'.format(degree,sector))
            break
        break

    # Finding the area of the triangle first (Trigonometry)
    triangle = (1/2) * radius**2 * math.sin(math.radians(degree))

    # Area of sector - Area of triangle = Area of segment
    segment = np.abs(sector - triangle)
    print('The area of the segment is: {:.2f} unit(s)²'.format(segment))
    draw(radius,sector)

    input('Press any key . . .')
    choose()

choose()