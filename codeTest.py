import os, sys, math

def CalculateAverage(numbers):
    total = 0
    for n in numbers:
        total += n
    avg = total / len(numbers)  
    return avg

def printResult(value ):
    print("Average is:", value)

numbers = []
printResult(CalculateAverage(numbers))  
