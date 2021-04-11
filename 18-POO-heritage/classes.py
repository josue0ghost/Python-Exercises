# Heritage: posibility to share attributes and methods between classes
import random

class Person:
    """
    name
    lastName
    height
    age
    """
    def getName(self):
        return self.name
    
    def getLastName(self):
        return self.lastName
    
    def getHeight(self):
        return self.height
    
    def getAge(self):
        return self.age
    
    def setName(self, name):
        self.name = name
    
    def setLastName(self, lastName):
        self.lastName = lastName
    
    def setHeight(self, height):
        self.height = height
    
    def setAge(self, age):
        self.age = age
    
    def speak(self):
        rand = random.randint(0, 5)
        if rand == 0:
            return "I'm speaking! :o"
        elif rand == 1:
            return "Hi!"
        elif rand == 2:
            return "There you are!"
        elif rand == 3:
            return "Hey! It's me!"
        elif rand == 4:
            return "Deploying"
        else:
            return "What are you doin'?"

    def walk(self):
        return "Why am I walking?"
    
    def sleep(self):
        return "Sleeping"

class Programmer(Person): # Heritage from Person class
    def __init__(self):
        self.languages = "Java, C++, Python"
        self.exp = 5
    
    def getLanguages(self):
        return self.languages
    
    def learn(self, languages):
        self.languages = languages
        return self.languages
    
    def code(self):
        return "Hi! I'm coding"

class NetworkTechnician(Programmer):
    def __init__(self):
        super().__init__() # super() gets father class __init__ constructor
        self.auditNetworks = "Expert"
        self.exp = 15
    
    def audit(self):
        return "I'm auditing networks"
