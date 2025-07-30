from cmu_graphics import *
from PIL import Image, ImageFont
from customer import *
from recipes import *
from profits import *
from cook import *

font = ImageFont.truetype("PixelifySans-Regular.ttf", size=36)

def rectsOverlap(x1, y1, w1, h1, x2, y2, w2, h2):
    return not (x1 + w1 < x2 or x1 > x2 + w2 or  
                y1 + h1 < y2 or y1 > y2 + h2)

def onAppStart(app):
    app.counter = 0
    app.width = 600
    app.height = 700 
    app.screen = 'start' 
    app.dragging = None
    app.draggingName = None
    app.dragOffset = (0, 0)
    # reset buttons for cook game
    app.rx, app.ry, app.rw, app.rh = 500, 20, 80, 40

    # {name : [order price, order cost, recipe page url]}
    app.orders = {
        'Coconut Latte'     : [2.99, 0.30], 
        'Iced Americano'    : [1.99, 0.20],
        'Iced Matcha Latte' : [3.99, 0.99],
        'Hot Matcha Latte'  : [3.99, 0.99],
        'Ube Pancake'       : [4.99, 1.50],
        'Pandan Egg Waffle' : [4.99, 1.59],
        'Mango Bingsoo'     : [4.50, 1.20],
        'Melon Bingsoo'     : [3.99, 0.99]
    }
    
    # kitchen
    app.moneyMade = 0
    app.moneySpent = 0
    app.served = 0
    app.currCust = Customer(CMUImage(Image.open('customers/pink-still.png')),
                            app.orders)
    app.currRecipe = Recipe(app.currCust.orderName)
    app.orderMade = None
    app.orderx, app.ordery, app.orderw, app.orderh = 400, 400, 153, 168
    app.newCustomer = False
    

    # images
    app.kitchenImg = CMUImage(Image.open('images/kitchen.png'))

############################################################
# Mouse Press / Change Screen Functions
############################################################


def onMousePress(app,mouseX,mouseY):

    #######################################
    # Start Screen
    #######################################
    if app.screen == 'start':
        if (mouseX > 0):
            app.screen = 'kitchen'


    #######################################
    # Kitchen Screen
    #######################################
    elif app.screen == 'kitchen':
        if app.orderMade != None:
            

                
        # not magic numbers, values based on where buttons are in drawing
        if (340 <= mouseX <= 500) and (60 <= mouseY <= 180):
            app.screen = 'recipeBook'
        
    

    #######################################
    # Recipe Book Screen
    #######################################
    elif app.screen == 'recipeBook':
        # not magic numbers, values based on where buttons are in drawing
        # exit out button
        if (45 <= mouseX <= 90) and (70 <= mouseY <= 113):
            app.screen = 'kitchen'
        # ready button
        if app.currRecipe.isOnReady(mouseX, mouseY):
            
            chosenRecipe = app.currRecipe.getChosenRecipe(mouseX, mouseY)

            app.gameImg = (CMUImage(Image.open(
                            app.currRecipe.getGameImg())
                            ))
            
            if (app.currRecipe.orderName == 'Ube Pancake' or 
                app.currRecipe.orderName == 'Pandan Egg Waffle'):
                app.currCook = Pancakes(chosenRecipe)
            elif (app.currRecipe.orderName == 'Mango Bingsoo' or 
                app.currRecipe.orderName == 'Melon Bingsoo'):
                app.currCook = Bingsoo(chosenRecipe)
            elif (app.currRecipe.orderName == 'Iced Americano' or 
                app.currRecipe.orderName == 'Coconut Latte'):
                app.currCook = Coffee(chosenRecipe)
            elif (app.currRecipe.orderName == 'Hot Matcha Latte' or 
                app.currRecipe.orderName == 'Iced Matcha Latte'):
                app.currCook = Matcha(chosenRecipe)
            
            app.screen = 'cookGame'


    #######################################
    # Cooking Game Screen
    #######################################

    elif app.screen =='cookGame':
        app.currCook.handleMousePress(mouseX, mouseY)
        
        
def onMouseDrag(app, mouseX, mouseY):
    if app.screen == 'kitchen':
        if app.orderMade != None:
            

    if app.screen == 'cookGame':
        app.currCook.handleMouseDrag(mouseX, mouseY)

def onMouseRelease(app, mouseX, mouseY):
    if app.screen == 'kitchen':
        if app.orderMade != None:
           if app.currCust.isSatisfied(app.orderMade, mouseX, mouseY):
               app.newCustomer = True
               

    if app.screen == 'cookGame':
        app.currCook.handleMouseRelease(mouseX, mouseY)
        if app.currCook.finishedOrder == True:
            app.screen = 'kitchen'
            app.orderMade = app.currCook.chosen

############################################################
# Draw 
############################################################

def redrawAll(app):

    # start screen
    if app.screen == 'start':
        drawLabel('start', 300, 300, size = 80, font = 'Pixelify Sans')

        

    #kitchen screen
    elif app.screen == 'kitchen':
        drawImage(app.kitchenImg, 0, 0, width = app.width, height = app.height)
        drawImage(app.currCust.sprite, 80, 207, width=189, height=189)
        drawLabel(app.currCust.speak(), 240, 100, size = 10)
        drawLabel(f'Money Made: {app.moneyMade}', app.width/2, 600, size = 20)
        drawLabel(f'Served: {app.served}', app.width/2, 640, size = 20)
        if app.orderMade != None:
            drawImage((CMUImage(Image.open(
                            f'finishedFoods/{app.currCook.chosen}')
                            )), 400, 400, 153, 168)
        # drawRect(340, 60, 160, 120, fill = 'green', opacity = 50)
    

    #recipe book screen
    elif app.screen == 'recipeBook':
        drawImage(app.currRecipe.getRecipeBookScreen(), 0, 0,
                  width = app.width, height = app.height)
        # X location
        # drawRect(45, 70, 45, 43, fill='green', opacity = 50)
        
        # Ready locations
        # drawRect(75, 410, 150, 80, fill = 'green', opacity = 50)
        # drawRect(380, 410, 150, 80, fill = 'green', opacity = 50)
    
    elif app.screen == 'cookGame':
        scene = app.currCook.getScene()
        drawImage(app.gameImg, 0, 0, width = app.width, height = app.height)

        for url, x, y, w, h in scene['images']:
            drawImage(CMUImage(Image.open(url)), x, y, width=w, height=h)
    
        if app.currCook.finishedOrder == True:
            drawLabel('Done!', app.width/2, app.height/2, size = 50)

        # Chopping board location
        # drawRect(40, 430, 261, 150, fill = 'green', opacity = 50)

        
        



    

############################################################
# Main
############################################################

def main():
    runApp()

main()
