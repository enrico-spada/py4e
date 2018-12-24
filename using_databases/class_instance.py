class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, z):              #remember self is nothing but an alias of the instance
        self.name = z                   #assign z to the attribute name of the instance
        print(self.name, "constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)

s = PartyAnimal("Sally")
s.party()

j = PartyAnimal("Jim")
j.party()
s.party()
