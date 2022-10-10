# Name: Adam Stapleton
# Date started: 9/30/2022
# Date completed: 9/30/2022
# Purpose: Uses many methods to complete calculations and relational tests based
#          on my birthdate.
import math

def printCase(input):
    #takes input, finds associated case, prints result
    match input:
        case 4:
            print('The difference between bDay and bMonth: ' + str(input))
        case 10:
            print('The month I was born: ' + str(input))
        case 14:
            print('The day I was born: ' + str(input))
        case True:
            print('Is bDay larger than bMonth? ' + str(input))

def printMath(input):
    #takes input from mathematical calculations, finds associated case,
    #prints result
    if input > 145:
        print('The circumference of the circle: ' + str(input))
    else:
        print('The area of the rectangle: ' + str(input))

def largerTest(day, month):
    #takes two numbers, finds which is larger, prints with function,
    #returns boolean result
    largerFlag = day > month
    printCase(largerFlag)
    return largerFlag

def numDifference(day, month):
    #takes two numbers, finds which is larger, subtracts appropriately,
    #prints difference with function, returns difference
    larger = day > month
    if(larger):
        diff = day - month
    else:
        diff = month - day
    printCase(diff)
    return diff

def calcCirc(day, month):
    #takes two numbers, adds them to make a radius, calculates theorhetical
    #circle circumference, prints with function, returns circumference
    radius = day + month
    circumference = 2 * math.pi * radius
    printMath(circumference)
    return circumference

def calcArea(day, month):
    #takes two numbers, multiplies to find theorhetical rectangular area,
    #returns area
    area = day * month
    return area

#create variables based on Oct. 14th, my birthday
bDay = 14
bMonth = 10
#print these values with custom function
printCase(bDay)
printCase(bMonth)
#compares and prints these values with a function
whichLarger = largerTest(bDay, bMonth)
#prints the difference between the two values
difference = numDifference(bDay, bMonth)
#finds and prints circumference where radius is sum of the two values
circ = calcCirc(bDay, bMonth)
#finds and prints area where bDay is length and bMonth is width
area = calcArea(bDay, bMonth)
printMath(area)
