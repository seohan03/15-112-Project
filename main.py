from cmu_graphics import *
from PIL import Image, ImageDraw
from customer import *
from recipes import *
from profits import *

def onAppStart(app):
    app.counter = 0
    app.width = 600
    app.height = 700 
    app.screen = 'start'  

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
    if app.screen == 'start':
        if (mouseX > 0):
            app.screen = 'kitchen'
    elif app.screen == 'kitchen':
        # not magic numbers, values based on where buttons are in drawing
        if (340 <= mouseX <= 500) and (60 <= mouseY <= 180):
            app.screen = 'recipeBook'
    elif app.screen == 'recipeBook':
        if (45 <= mouseX <= 90) and (70 <= mouseY <= 113):
            app.screen = 'kitchen'
        if app.currRecipe.isOnReady(mouseX, mouseY):
            app.gameImg = (CMUImage(Image.open(
                            app.currRecipe.getGameScreen(mouseX, mouseY))
                            ))
            app.screen = 'cookGame'
    elif app.screen =='cookGame':
        if (mouseX <= 0) and (mouseY <= 0):
            app.screen = 'kitchen'
            
def onMouseDrag(app, mouseX, mouseY):
    if app.screen == 'cookGame':
        pass
    
    
############################################################
# Draw 
############################################################

def redrawAll(app):

    # start screen
    if app.screen == 'start':
        drawImage(CMUImage(Image.open('recipes/food/pandan.png')), 0, 0, width = app.width, height = app.height)
        drawImage(CMUImage(Image.open('recipes/ingredients/pancakes/flour.png')),
                  65, 140, width = 122, height = 147)
        drawImage(CMUImage(Image.open('recipes/ingredients/pancakes/milk.png')), 
                  190, 145, width = 85, height = 141)
        
        drawImage(CMUImage(Image.open('recipes/ingredients/pancakes/egg.png')), 
                  440, 160, width = 57, height = 66)
        drawImage(CMUImage(Image.open('recipes/ingredients/pancakes/ubeYam.png')), 
                  360, 220, width = 121, height = 80)
        drawImage(CMUImage(Image.open('recipes/ingredients/pancakes/pandanExtract.png')), 
                  490, 235, width = 69, height = 71)

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
        drawRect(35, 50, 45, 43, fill='green', opacity = 50)
        



    

############################################################
# Main
############################################################

def main():
    runApp()

main()
