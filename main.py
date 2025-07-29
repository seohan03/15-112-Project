from cmu_graphics import *
from PIL import Image, ImageDraw
from customer import *
from recipes import *
from profits import *
from cook import *

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
        
        if ((app.rx <= mouseX <= app.rx + app.rw) and 
            (app.ry <= mouseY <= app.ry + app.rh)):
            app.currCook.resetIngredients()
            
        clicked = app.currCook.getIngredientUnder(mouseX, mouseY)
        if clicked != None and clicked != 'emptyBowl':
            app.draggingName = clicked
            url, x, y, w, h = app.currCook.ingredients['starter'][clicked]
            # to see where inside the image user clicked
            app.dragOffset = (mouseX - x, mouseY - y)
        else:
            app.draggingName = None
            
        if (mouseX <= 0) and (mouseY <= 0):
            app.screen = 'kitchen'
        
        
def onMouseDrag(app, mouseX, mouseY):

    if app.screen == 'cookGame' and app.draggingName != None:
        ingre = app.draggingName
        url, x0, y0, w, h = app.currCook.ingredients['starter'][ingre]
        dx, dy = app.dragOffset
        newX = mouseX - dx
        newY = mouseY - dy
        app.currCook.ingredients['starter'][ingre] = (url, newX, newY, w, h)

def onMouseRelease(app, mouseX, mouseY):

    if app.screen == 'cookGame' and app.draggingName != None:
        name = app.draggingName
        # get the ingredient’s current box
        if name != 'emptyBowl':
            url, inx, iny, inw, inh = app.currCook.ingredients['starter'][name]
            # get the bowl’s box
            url, bx, by, bw, bh = app.currCook.ingredients['starter']['emptyBowl']
            if rectsOverlap(inx, iny, inw, inh, bx, by, bw, bh):
                app.currCook.recordDrop(name)
        
        app.draggingName = None    


    
    
############################################################
# Draw 
############################################################

def redrawAll(app):

    # start screen
    if app.screen == 'start':
        drawLabel('start', 50, 50)
        

    #kitchen screen
    elif app.screen == 'kitchen':
        drawImage(app.kitchenImg, 0, 0, width = app.width, height = app.height)
        drawImage(app.currCust.sprite, 80, 207, width=189, height=189)
        drawLabel(app.currCust.speak(), 240, 100, size = 10)
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
        drawImage(app.gameImg, 0, 0, width = app.width, height = app.height)

        starterItems = app.currCook.getAllStarterIngredients()
        for name, (url, x, y, width, height) in starterItems.items():
            if name == app.draggingName:
                continue # so that the image gets drawn on top
            elif name != 'emptyBowl':
                img = CMUImage(Image.open(url))
                drawImage(img, x, y, width = width, height = height)
                
        bowlUrl = app.currCook.getBowlImage()
        url, bx, by, bw, bh  = app.currCook.ingredients['starter']['emptyBowl']
        drawImage(CMUImage(Image.open(bowlUrl)), bx, by, width=bw, height=bh)

        if app.draggingName:
            ingredients = app.currCook.ingredients
            url, x, y, w, h = ingredients['starter'][app.draggingName]
            img = CMUImage(Image.open(url))
            drawImage(img, x, y, width=w, height=h)
        
        # reset button
        
        drawRect(app.rx, app.ry, app.rw, app.rh, fill = 'green')

        
        
        



    

############################################################
# Main
############################################################

def main():
    runApp()

main()
