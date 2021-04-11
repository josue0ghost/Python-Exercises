"""
    Show all multiplication tables from 1 to 10
"""

for count in range(1, 11):
    print(f"----- Multiplication table ({count}) -----")
    for mult in range(1, 11):
        print(f"{count} x {mult} = {count * mult}")