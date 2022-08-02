from unicodedata import name


class PartyAnimal:      # This is the template for making PartyAnimal object
    x = 0               # Attribute -> This is a bit of data code
    name = ""
    def __init__(self, nam):
        self.name = nam
        print(self.name, "constructed")

    def party(self):            # method -> is a funct but because it is inside a class we call it METHOD 
        self.x = self.x + 1
        print("So far", self.x)

class FootballFan(PartyAnimal):         # FootballFan class that extends PartyAnimal
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)

s = PartyAnimal("Sally")      # constructing and assign at "an"

s.party()              # calling

j = FootballFan("Jim")
j.party()
j.touchdown()