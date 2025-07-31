from cmu_graphics import *
from PIL import Image
from customer import Customer
from recipes import Recipe
import random



def rectsOverlap(x1, y1, w1, h1, x2, y2, w2, h2):
    return not (x1 + w1 < x2 or x1 > x2 + w2 or  
                y1 + h1 < y2 or y1 > y2 + h2)

#customer values
cx, cy, cw, ch = 80, 207, 189, 189
#reset button values
resetx, resety, resetw, reseth = 524, 40, 50, 51

class Kitchen():

    def __init__(self, app):
        self.app            = app 
        self.dragging       = False
        self.dx = self.dy   = 0

    def getOrderVals(self):
        return (self.app.orderx,
                self.app.ordery,
                self.app.orderw,
                self.app.orderh)

        
    def redoButton(self, x, y):
        if (resetx <= x <= resetx+resetw and
            resety <= y <= resety+reseth):
            app.moneyMade = 0
            app.served = 0
            app.orderMade = None
            app.currCust   = Customer(
                                CMUImage(Image.open('customers/pink.png')),
                                app.orders)
            app.currRecipe = Recipe(app.currCust.orderName)


    def handleMousePress(self, x, y):
        if self.app.orderMade != None:

            ox, oy, ow, oh = self.getOrderVals()
            # if click is inside that box, start dragging
            if ox <= x <= ox+ow and oy <= y <= oy+oh:
                self.dragging = True
                self.dx, self.dy = x - ox, y - oy


    def handleMouseDrag(self, x, y):
        if self.dragging == True:
            self.app.orderx = x - self.dx
            self.app.ordery = y - self.dy


    def handleMouseRelease(self, x, y):
        if self.dragging:
            self.dragging = False

        ox, oy, ow, oh = self.getOrderVals()
        if rectsOverlap(cx, cy, cw, ch, ox, oy, ow, oh):
            if self.app.currCust.isSatisfied(self.app.orderMade):
                self.serveCurrCustomer()

    def serveCurrCustomer(self):
        name = self.app.orderMade
        price, cost = self.app.orders[name]
        self.app.moneyMade += price
        self.app.served += 1

        custUrl = random.choice([
            'customers/pink.png',
            'customers/blue.png',
            'customers/gray.png'
        ])
        img = CMUImage(Image.open(custUrl))
        self.app.currCust   = Customer(img, self.app.orders)
        self.app.currRecipe = Recipe(self.app.currCust.orderName)

        # reset
        self.app.orderMade = None
        self.ox, self.oy = 400, 400