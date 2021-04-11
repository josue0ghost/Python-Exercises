from car import Car

myCar = Car("Blue", "Renault", "Clio", 200, 100, 4)

print(myCar.getInfo())

# detect type
myCar = ""
if type(myCar) == Car:
    print("Is an object")
else:
    print("Is not an object")

