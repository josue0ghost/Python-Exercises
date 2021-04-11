"""
    Ask for input until it is equals to "111"
"""

bucle = True
while bucle:
    word = input("INPUT: ")
    if word == "111":
        bucle = False
    else:
        print(f"You have introduced the wrong input {word}")
    
print(f"You have introduced '111'. Program finished")