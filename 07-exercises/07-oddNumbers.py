"""
    Show all odd numbers between 2 inputs
"""

numberA = int(input("Insert low limit for range: "))
numberB = int(input("Insert high limit for range: "))

if numberA < numberB:
    for count in range(numberA, numberB + 1):
        if (count % 2) != 0:
            print(f"{count} is odd")
else:
    print("High limit must be greater than low limit")