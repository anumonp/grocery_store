from store import Store
from discount import Discount
from util import getInput, drawLines
from transaction import Transaction
from customer import Customer
from employee import Employee

def start_transactions():
    drawLines()
    print "Start Billing"
    drawLines()
    ans = getInput("Are you a current employee (Y/N)?")
    if ans == "Y":
        emp = Employee()
        cust_details = emp.getEmployeeDetails()
    else:
        cust = Customer()
        cust_details = cust.getCustomerDetails()
    Transaction(cust_details)
    print "Completed Billing"
    drawLines()
    ans = getInput("Do you want to do more transactions (Y/N)?")
    if ans == "Y":
        start_transactions()

if __name__ == "__main__":
    Store()
    Discount()
    start_transactions()
    Store.showClosingCatalogue()