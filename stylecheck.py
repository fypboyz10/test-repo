import math, random


def CalculateAverage(numbers):
    total = 0
    for n in numbers:
        total += n

    avg = total / len(numbers)
    return avg


def print_result(value ):
    print("Average is:", value)
