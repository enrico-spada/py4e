class PartyAnimal:
    x = 0

    #Constructor
    def __init__(self):
        print("I am constructed")

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

    #Deconstructor
    def __del__(self):                      #this is executed right before the object is thrown away
        print("I am decostructed", self.x)


an = PartyAnimal()
an.party()
an.party()
an = 42                 #throw away the old object in that memory location
print("an contains", an)
