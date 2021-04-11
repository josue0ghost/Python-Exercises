"""
    Show 1 to 60's powers of 2
    -   Using while bucle
    -   Using for bucle
"""

count = 1

# Using while
print("---- WHILE ----")
while count < 61:
    power = pow(count, 2)
    print(f"pow({count}, 2) = {power}")
    count += 1

# Using for
print("---- FOR ----")
for number in range(1, 61):
    power = pow(number, 2)
    print(f"pow({number}, 2) = {power}")