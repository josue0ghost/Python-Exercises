"""
    for varibale in iterable_element
        instructions

    iterable_element can be a list, range, etc
"""

count = 0

for count in range(0, 10):
    print(str(count))
    if count == 8:
        break