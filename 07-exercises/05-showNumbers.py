"""
    Show all numbers between two inputs
"""

numberA = int(input("Insert low limit for range: "))
numberB = int(input("Insert high limit for range: "))

if numberA < numberB:
    for number in range(numberA, numberB + 1):
        print(number)
else:
    print("The high limit must be greater than low limit")

