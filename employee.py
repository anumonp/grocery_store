from util import getInput, drawLines
from user import User

class Employee(User):

    def __init__(self):
        emp_code = ""
        
    def getEmployeeDetails(self):
        self.getUserDetails()
        self.emp_code = getInput("Employee Code: ")
        emp_details = {
            "name" : self.name,
            "number": self.number,
            "emp_code": self.emp_code,
        }
        drawLines()
        return emp_details