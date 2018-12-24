#IF module.py has same name as the class, whenever you call the class you need to
#PartyAnimal.Partyanimal()

from enrico.party.party import PartyAnimal

class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 1
        self.party()
        print(self.name, "points", self.points)


s = PartyAnimal("Sally")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown()
