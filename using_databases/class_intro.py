class PartyAnimal:          #Class
    x = 0                   #Attribute

    #self is an alias of the instance
    def party(self):        #Method
        self.x = self.x + 1
        print("So far", self.x)

an = PartyAnimal()          #create an instance, like    x = list()

an.party()                  #like PartyAnimal.party(an)
an.party()
an.party()

print("\n\n")

print("Type: ", type(an))
print("Dir: ", dir(an))
