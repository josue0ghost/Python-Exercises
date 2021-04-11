# Define a class

class Car:

    # Attributes or Properties (variables)
    color = "Red"
    brand = "Ferrari"
    model = "Aventador"
    velocity = 300
    horsepower = 500
    seats = 2

    # Getters and Setters
    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color
    
    def setModel(self, model):
        self.model = model
    
    def getModel(self):
        return self.model

    # Methods. Actions our class does
    # With 'self' I access the properties of my class
    def accelerate(self):
        self.velocity += 1
    
    def brake(self):
        self.velocity -= 1
    
    def getVelocity(self):
        return self.velocity

# end of class definition

# create object or instance our class
myCar = Car()
print(myCar.brand, myCar.model)

myCar.accelerate()
print(f"Velocity: {myCar.getVelocity()}")