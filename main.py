from cmu_graphics import *
from PIL import Image
from customer import *
from recipes import *
from cook import *
from kitchen import *


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
    app.chosenRecipe = None
    # reset buttons for cook game
    app.rx, app.ry, app.rw, app.rh = 500, 20, 80, 40
        

    # {name : [order price, order cost]}
    app.orders = {
        # 'Coconut Latte'     : [2.99, 0.30], 
        # 'Iced Americano'    : [1.99, 0.20],
        # 'Iced Matcha Latte' : [3.99, 0.99],
        # 'Hot Matcha Latte'  : [3.99, 0.99],
        'Ube Pancake'       : [4.99, 1.50],
        'Pandan Egg Waffle' : [4.99, 1.59],
        'Mango Bingsoo'     : [4.50, 1.20],
        'Melon Bingsoo'     : [3.99, 0.99]
    }
    
    # kitchen
    app.moneyMade = 0
    app.moneySpent = 0
    app.served = 0
    app.currCust = Customer(CMUImage(Image.open('customers/pink.png')),
                            app.orders)
    app.currRecipe = Recipe(app.currCust.orderName)
    app.orderMade = None
    app.orderx, app.ordery = 300, 400
    app.orderw = app.orderh = 0
    app.kitchen = Kitchen(app)    
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
        app.kitchen.redoButton(mouseX, mouseY)
        app.kitchen.handleMousePress(mouseX, mouseY)
        if app.kitchen.dragging:
            return

        # not magic numbers, values based on where buttons are in drawing
        elif (340 <= mouseX <= 500) and (60 <= mouseY <= 180):
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
            
            app.chosenRecipe = app.currRecipe.getChosenRecipe(mouseX, mouseY)

            app.gameImg = (CMUImage(Image.open(
                            app.currRecipe.getGameImg())
                            ))
            
            if (app.currRecipe.orderName == 'Ube Pancake' or 
                app.currRecipe.orderName == 'Pandan Egg Waffle'):
                app.currCook = Pancakes(app.chosenRecipe)
            elif (app.currRecipe.orderName == 'Mango Bingsoo' or 
                app.currRecipe.orderName == 'Melon Bingsoo'):
                app.currCook = Bingsoo(app.chosenRecipe)
            elif (app.currRecipe.orderName == 'Iced Americano' or 
                app.currRecipe.orderName == 'Coconut Latte'):
                app.currCook = Coffee(app.chosenRecipe)
            elif (app.currRecipe.orderName == 'Hot Matcha Latte' or 
                app.currRecipe.orderName == 'Iced Matcha Latte'):
                app.currCook = Matcha(app.chosenRecipe)
            
            app.screen = 'cookGame'


    #######################################
    # Cooking Game Screen
    #######################################
    elif app.screen =='cookGame':
        app.currCook.handleMousePress(mouseX, mouseY)
        
        
def onMouseDrag(app, mouseX, mouseY):
    if app.screen == 'kitchen':
        if app.orderMade != None:
            app.kitchen.handleMouseDrag(mouseX, mouseY)

    elif app.screen == 'cookGame':
        app.currCook.handleMouseDrag(mouseX, mouseY)

def onMouseRelease(app, mouseX, mouseY):
    if app.screen == 'kitchen':
        if app.orderMade != None:
            app.kitchen.handleMouseRelease(mouseX, mouseY)
               
    elif app.screen == 'cookGame':
        app.currCook.handleMouseRelease(mouseX, mouseY)
        if app.currCook.finishedOrder == True:
            app.screen = 'kitchen'
            app.orderMade = app.currCook.chosen
            app.orderx, app.ordery = 300, 400

            path = f'finishedFoods/{app.orderMade}.png'
            img  = Image.open(path)
            w, h = img.size
            img.close()
            app.orderw, app.orderh = w, h



############################################################
# Draw 
############################################################

def redrawAll(app):

    # start screen
    if app.screen == 'start':
        drawLabel('start', 300, 300, size = 80)
        drawImage(app.kitchenImg, 0, 0, width = app.width, height = app.height)

        
    #kitchen screen
    elif app.screen == 'kitchen':
        drawImage(app.kitchenImg, 0, 0, width = app.width, height = app.height)
        drawImage(app.currCust.sprite, 80, 207, width=189, height=189)
        
        for text, margin in app.currCust.getSpeakLines():
            drawLabel(text, 230, margin, size = 12)
        drawLabel(f'Money Made: ${app.moneyMade}', 175, 605, size = 20)
        drawLabel(f'Served: {app.served}', 175, 630, size = 20)
        if app.orderMade != None:
            url = f'finishedFoods/{app.orderMade}.png'
            plateImg = CMUImage(Image.open(url))
            drawImage(plateImg, app.orderx, app.ordery, width = 153, height = 168)
        drawImage('images/redoButton.png', 524, 40, width = 50, height = 51)
    

    #recipe book screen
    elif app.screen == 'recipeBook':
        drawImage(app.currRecipe.getRecipeBookScreen(), 0, 0,
                  width = app.width, height = app.height)
        # X location
        # drawRect(45, 70, 45, 43, fill='green', opacity = 50)
        
        # Ready locations
        drawLabel('ready', 150, 450)
        drawLabel('ready', 450, 450)
    
    elif app.screen == 'cookGame':
        scene = app.currCook.getScene()
        drawImage(app.gameImg, 0, 0, width = app.width, height = app.height)

        for url, x, y, w, h in scene['images']:
            drawImage(CMUImage(Image.open(url)), x, y, width=w, height=h)
        
        for text, margin in app.currCook.getInstructionLines():
            drawLabel(text, 370, margin, size = 11)
    
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
