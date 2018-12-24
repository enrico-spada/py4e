
# OBJECT ORIENTED PYTHON

#Class:                                 --> shape of an object
#a template
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

#Constructor:
#initialize all variables required by the class to create an instance

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


################################################################################


################################################################################

################################################################################

################################################################################

################################################################################

################################################################################

################################################################################


################################################################################

################################################################################

################################################################################

################################################################################

################################################################################
################################################################################


################################################################################

################################################################################

################################################################################