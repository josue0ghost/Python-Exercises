# capture exceptions and manage errors on code

name = input("What's your name?: ")

try:
    
    if len(name) > 1:
        user_name = f"Your name is: {name}"

        print(user_name)

except:
    print("An error has raised. Please, enter name correctly")
else:
    print("Task successfull")
finally:
    print("End of iteration")

###### multiple exceptions ######

try:
    number = int(input("Insert number to power it by 2: "))
    print(f"Power({number}, 2): {number*number}")
except TypeError:
    print("Convert your string to int")
except ValueError:
    print("Insert a correct number")
except Exception as e:
    print(f"An error has raised: {type(e).__name__}")

###### personalized exeptions ######

age = int(input("Insert your age: "))

if age < 5 or age > 110:
    raise ValueError("Age not real")
else:
    print("Age real xd")
