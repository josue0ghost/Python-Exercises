import classes

person = classes.Person()
person.setName("Emmanuel")
person.setLastName("Alvarado")
person.setHeight("174 cm")
person.setAge("21 yo")

print(f"Person is: {person.getName()} {person.getLastName()}")
print(person.speak())

programmer = classes.Programmer()
programmer.setName("Emmanuel")
programmer.setLastName("Alvarado")
print(f"The programer's name is: {programmer.getName()} {programmer.getLastName()}")
print(programmer.getLanguages())
print(programmer.speak())

###### super()

NetworkTech = classes.NetworkTechnician()
NetworkTech.setName("Manuel")

# Constructors are exclusive for every class
# super() was implemented on classes.py in NetworkTechnician class
print(NetworkTech.auditNetworks, NetworkTech.getName(), NetworkTech.getLanguages())