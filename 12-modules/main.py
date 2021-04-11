'''
    Python3 modules:
    https://docs.python.org/3/py-modindex.html

'''
# import whole module
# import mymodule
# print(mymodule.helloWorld('Emma'))

# import only one function
# from mymodule import helloWorld
# print(helloWorld('Emma'))

# import whole module without using module name
from mymodule import *
print(helloWorld('Emma'))

# datetime module
import datetime

print(datetime.date.today())
fullDate = datetime.datetime.now()
print(fullDate)
print(fullDate.strftime("%d/%m/%Y, %H:%M:%S"))

# math module
import math

print(math.sqrt(16))
print(math.pi)
print(math.ceil(math.pi))   # redondear arriba
print(math.floor(math.pi))  # redondear abajo

# random module
import random
print(random.randint(15, 67))
print(random.random())