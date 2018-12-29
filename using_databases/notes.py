
# OBJECT ORIENTED PYTHON

#Class:                                 --> shape of an object
#a template for the object
#It is the blueprint for making things

#Method or Message:                     --> functions built-in into objects
#a defined capability of a class
#it is defined in the class and is also part of the object
#usually, it only affect one specific instance

#Field or Attribute:
#a bit of data in a class

#Object or Instance:                    --> it is the actual object created ar runtime
#a particular instance of a class

################################################################################

#Constructor and Destructor         --> they are optional
#they are specially named methods

#Constructor:   in OOP, a constructor in a class is a special block of statements
#               called when an object is created
#initialize all variables required by the class to create the SPECIFIC INSTANCE


#Destructor:            --> seldom used
#

class PartyAnimal:
    x = 0

    #Constructor
    def __init__(self):
        print("I am constructed")

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

    #Deconstructor
    def __del__(self):
        print("I am decostructed", self.x)





################################################################################

#Inheritance: we can create a class customizing an existing class
#The new class (child) has all the capabilities of the old class (parent), and some additional ones


class PartyAnimal:
    x = 0
    name = ""
    def __init__(self):
        self.name = name
        print(self.name, "constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.party)

class FootballFan(PartyAnimal):     #class FootballFan EXTENDS class PartyAnimal
    points = 0
    def touchdown(self):
        self.points = self.points + 1
        self.party()
        print(self.name, "points", self.points)


#Subclasses: hierarchy of classes      --> just another way to DRY
#Aninals
    #Mammals
        #dogs
        #cats

################################################################################

#Definitions

#Class: a template
#Attribute: a variable within a class
#Method: a function within a class
#Object: a particular instance of a class
#Constructor: code that runs when an object is created
#Inheritance: the ability to extend a class to make a new class


################################################################################

#SQL is a standard

#MySQL: open source; simple but fast; can't solve less problem than OracleSQL

#PostgreSQL: open source more similar to OracleSQL than MySQL

#SQLLite: embedded database; so small that it is built-in into the application
#It is already built-in in Python ;) --> import

################################################################################
