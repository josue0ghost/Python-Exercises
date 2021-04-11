noneVar = None
string = "This is a string"
integer = 24
float = 34.5
boolean = True
list = [23, 345, 45.6, "NaN", True]
tuple = ("master", 25) #tuples does not change
dictionary = {
    "name": "Emmanuel",
    "lastName": "Alvarado"
}
range = range(9)
byte = b"This is a byte"

print("Value: {}, type: {}".format(byte, type(byte)))

# conversión de datos
print(str(integer) + " this number was converted to a string")