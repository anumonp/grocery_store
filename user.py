from util import getInput, drawLines

class User():
    
    def __init__(self):
        name = ""
        age = ""
        number = ""
        is_senior_citizen = 0

    def getUserDetails(self):
        drawLines()
        print "Lets capture customer details"
        drawLines()
        self.name = getInput("Customer Name: ")
        self.number = getInput("Mobile Number: ")
        self.age = getInput("Age: ")