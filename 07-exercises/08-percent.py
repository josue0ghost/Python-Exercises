"""
    Show X% of Y
    -   X and Y must be inputs
"""

percent = float(input("Insert percentage (%): "))
number = float(input("Insert number: "))

print(f"{percent}% of {number} = {number * (percent / 100)}")