from store import Store
from util import getInput, drawLines, calculateDiscountedPrice
from discount import Discount
import uuid

class Transaction():
    transactions = {}
    def __init__(self, cust_details):
        self.initialiseTransaction(cust_details)

    def initialiseTransaction(self, cust_details):
        billed_items = []
        total_billed_items = self.billItems(billed_items)
        txn_id = uuid.uuid4().hex
        Transaction.transactions[txn_id] = total_billed_items
        self.generateBill(cust_details,txn_id,total_billed_items)
        
    def billItems(self, billed_items):
        register = self.selectRegister()
        Store.showRegisterCatalog(register)
        return self.chooseItem(register, billed_items)
        

    def selectRegister(self):
        print "Please select the register:"
        for i, (key, value) in enumerate(Store.store_inventory.items()):
            print str(i+1) + " " + key
        register = raw_input()
        return list(Store.store_inventory)[int(register)-1]

    def chooseItem(self, register, billed_items):
        item = {}
        item['register'] = register
        item_no = getInput("Please select the item from above catalogue:")
        item_name = list(Store.store_inventory[register]['items'])[int(item_no)-1]
        item['item'] = item_name
        item['discount_percent'] = int(Store.store_inventory[register]['discount_percent']) + int(Store.store_inventory[register]['items'][item_name]['discount_percent'])
        item['price'] = Store.store_inventory[register]['items'][item_name]['price']
        count = getInput("Please mention the number of " + item_name + " you need:")
        item['count'] = count
        ans = getInput("Do you want to bill more items (Y/N)?")
        billed_items.append(item)
        Store.repopulateAvailableStock(item)
        if ans == "Y":
            self.billItems(billed_items)
        return billed_items

    def generateBill(self, cust_details, txn_id, total_billed_items):
        drawLines()
        print "Transaction Id: " + txn_id
        drawLines()
        print "Name: " + cust_details['name']
        print "Mobile Number: " + cust_details['number']
        if 'emp_code' in cust_details.keys():
            print "Employee Code: " + cust_details['emp_code']
        drawLines()
        print "{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format('Item', 'Units', 'Unit Price', 'Discount Percent', 'Total', 'Discounted Price')
        drawLines()
        total = 0
        for item in total_billed_items:
            price = item['price']
            total_price = int(item['count']) * int(price)
            discounted_total = calculateDiscountedPrice(total_price, item['discount_percent'])
            total = total + discounted_total
            print "{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(item['item'], item['count'], price, str(item['discount_percent']) + "%", total_price, discounted_total)
        drawLines()
        if 'is_senior_citizen' in cust_details.keys() and cust_details['is_senior_citizen'] == 1:
            print "Total: " + str(total)
            print "Senior Citizen Discount: " + str(Discount.discount_details["senior_citizen_discount"]) + "%"
            total = calculateDiscountedPrice(total, Discount.discount_details["senior_citizen_discount"])
        if 'emp_code' in cust_details.keys():
            print "Total: " + str(total)
            print "Employee Discount: " + str(Discount.discount_details["employee_discount"]) + "%"
            total = calculateDiscountedPrice(total, Discount.discount_details["employee_discount"])
        print "Total to be paid: " + str(total)
        drawLines()