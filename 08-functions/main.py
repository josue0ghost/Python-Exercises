# def functionName (params)

def getName(name):
    return f"getting name... Name: {name}"

def getLastname(lastname):
    return f"getting lastname... LastName: {lastname}"

def getCompleteName(name, lastname):
    return getName(name) + "\n" + getLastname(lastname)

# lambda functions
getYear = lambda year: f"getting year... Year: {year}"