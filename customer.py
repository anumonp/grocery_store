from util import getInput, drawLines
from user import User

class Customer(User):

    def __init__(self):
        self.is_senior_citizen = 0
    
    def getCustomerDetails(self):
        self.getUserDetails()
        if int(self.age) >= 60:
            self.is_senior_citizen = 1
        
        cust_details = {
            "name" : self.name,
            "number": self.number,
            "is_senior_citizen": self.is_senior_citizen
        }
        drawLines()
        return cust_details