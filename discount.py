from util import getInput, drawLines
from store import Store

class Discount():
    
    discount_details = {}

    def __init__(self):
        self.setupStoreDiscount()

    def setupStoreDiscount(self):
        self.addDiscountToRegister()
        self.addDiscountToSeniorCitizen()
        self.addDiscountToEmployee()
        
    def addDiscountToRegister(self):
        for key, value in Store.store_opening_inventory.iteritems():
            Store.store_opening_inventory[key] = self.addDiscount(value, value["name"] + " Register")
            print "Enter any discounts specific to items. Total discount will be computed as the sum of register discount and item discount."
            for k, v in value["items"].iteritems():
                Store.store_opening_inventory[key]["items"][k] = self.addDiscountOnItem(v)

    def addDiscountOnItem(self, item):
        return self.addDiscount(item, item['name'])

    def addDiscountToSeniorCitizen(self):
        ans = getInput("Are you giving any discount to senior citizen? (Y/N)")
        if ans == "Y":
            discount = getInput("Senior Citizen Discount: ")
            Discount.discount_details["senior_citizen_discount"] = discount
        else:
            Discount.discount_details["senior_citizen_discount"] = 0

    def addDiscountToEmployee(self):
        ans = getInput("Are you giving any discount to your employees? (Y/N)")
        if ans == "Y":
            discount = getInput("Employee Discount: ")
            Discount.discount_details["employee_discount"] = discount
        else:
            Discount.discount_details["employee_discount"] = 0
    
    def addDiscount(self, dict_item, dict_name):
        discount = getInput(dict_name + " Discount: ")
        dict_item['discount_percent'] =  discount
        return dict_item