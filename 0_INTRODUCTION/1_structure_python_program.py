#Documentation section
#structure of python program

#import section
import math

#global declaration section
iRadius = 5

#class section
class circle():
    def GetArea(self):
        return math.pi * iRadius * iRadius

    def GetCircumference(self):
        return 2 * math.pi * iRadius

#sub Program section
def ShowRadius():               
    print("\n-->Radius : ", iRadius)

# Playground sction
ShowRadius()

cObj = circle()

print("\n-->Area : ", cObj.GetArea())

print("\n-->Circumference : ", cObj.GetCircumference())
