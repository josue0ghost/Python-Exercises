class Car:

    # Attributes or Properties (variables)
    # public attributes
    color = "Red"
    brand = "Ferrari"
    model = "Aventador"
    velocity = 300
    horsepower = 500
    seats = 2

    # private attributes (add __ to the property name)
    __privateAtt = ""

    # Constructor
    def __init__(self, color, brand, model, velocity, horespower, seats):
        self.color = color
        self.brand = brand
        self.model = model
        self.velocity = velocity
        self.horsepower = horespower
        self.seats = seats        

    # Getters and Setters
    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color
    
    def setModel(self, model):
        self.model = model
    
    def getModel(self):
        return self.model
    
    def getBrand(self):
        return self.brand

    def getInfo(self):
        Info = "-- Car information --"
        Info += "\n Color: " + self.getColor()
        Info += "\n Brand: " + self.getBrand()
        Info += "\n Model: " + self.getModel()
        Info += "\n Velocity: " + str(self.getVelocity())
        return Info

    # Methods. Actions our class does
    # With 'self' I access the properties of my class
    def accelerate(self):
        self.velocity += 1
    
    def brake(self):
        self.velocity -= 1
    
    def getVelocity(self):
        return self.velocity

# end of class definition