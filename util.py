def getInput(msg):
    print msg
    input = raw_input()
    return input

def drawLines():
    print "--" * 50

def printHeader(header):
    print " " * 30 + header

def calculateDiscountedPrice(price, discount_percentage):
    discount = int(price) * float(discount_percentage)/100
    return int(price) - discount