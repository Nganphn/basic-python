class Human:
    def __init__(self, name = "", age = ""):
        self.name = name
        self.age = age
    
    def __str__(self):
        return "Name: " + self.name + ", "  + "Age: " + self.age

    name = ""
    age = ""