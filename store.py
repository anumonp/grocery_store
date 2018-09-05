from util import getInput, drawLines, printHeader
class Store():
    
    store_opening_inventory = {}
    # Sample Data
    # store_opening_inventory = {'Veggies': {'items': {'Tomato': {'count': 100, 'price': 2, 'name': 'Tomato'}, 'Carrot': {'count': 100, 'price': 7, 'name': 'Carrot'}}, 'name': 'Veggies'}, 'Fruits': {'items': {'orange': {'count': 100, 'price': 17, 'name': 'orange'}, 'Apple': {'count': 100, 'price': 23, 'name': 'Apple'}}, 'name': 'Fruits'}}
    store_inventory = {}

    def __init__(self):
        self.setupStore()

    def setupStore(self):
        self.createRegister()
        self.addInventory()
        Store.store_inventory = Store.store_opening_inventory
        self.showCatalog()
    
    def createRegister(self):
        register_name = getInput("Please input the register name:")
        register = {'name': register_name, 'items': {}}
        self.store_opening_inventory[register_name] = register
        ans = getInput("Do you want to add more registers (Y/N)?")
        if ans == "Y":
            self.createRegister()

    def addInventory(self):
        self.addItemToRegister()

    def addItemToRegister(self):
        print "Lets add items to your register. Please select the register:"
        for index, (key, value) in enumerate(self.store_opening_inventory.items()):
            print str(index+1) + " " + key

        register = raw_input()
        item = getInput("Please input the " + list(self.store_opening_inventory)[int(register)-1] + " name:")
        self.store_opening_inventory[list(self.store_opening_inventory)[int(register)-1]]['items'][item] = {'name':item}
        stock = getInput("Please input the stock count:")
        self.store_opening_inventory[list(self.store_opening_inventory)[int(register)-1]]['items'][item]['count'] = int(stock)
        price = getInput("Please input the price:")
        self.store_opening_inventory[list(self.store_opening_inventory)[int(register)-1]]['items'][item]['price'] = int(price)
        ans = getInput("Do you want to add more items (Y/N)?")
        if ans == "Y":
            self.addItemToRegister()

    def showCatalog(self):
        drawLines()
        printHeader('Catalog')
        drawLines()
        print "{:<15} {:<15} {:<15} {:<15}".format('Register','Item','Count', 'Price')
        drawLines()
        for k, v in self.store_opening_inventory.iteritems():
            for key, value in v["items"].iteritems():
                print "{:<15} {:<15} {:<15} {:<15}".format(k, value['name'], value['count'], value['price'])
        drawLines()
    
    @classmethod
    def showRegisterCatalog(self, register):
        print "{:<15} {:<15} {:<15} {:<15}".format('Sl No', 'Item','Count', 'Price')
        drawLines()
        for i, (key, value) in enumerate(self.store_inventory[register]["items"].iteritems()):
            print "{:<15} {:<15} {:<15} {:<15}".format(str(i+1), value['name'], value['count'], value['price'])
        drawLines()

    @classmethod
    def showClosingCatalogue(self):
        drawLines()
        printHeader('Catalog')
        drawLines()
        print "{:<15} {:<15} {:<15} {:<15}".format('Register','Item','Count', 'Price')
        drawLines()
        for k, v in self.store_inventory.iteritems():
            for key, value in v["items"].iteritems():
                print "{:<15} {:<15} {:<15} {:<15}".format(k, value['name'], value['count'], value['price'])
        drawLines()

    @classmethod
    def repopulateAvailableStock(self, item):
        Store.store_inventory[item['register']]['items'][item['item']]['count'] = int(Store.store_inventory[item['register']]['items'][item['item']]['count']) - int(item['count'])

    

