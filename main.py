from cmu_graphics import *
from PIL import Image, ImageDraw
import random
from customer import *
from food import *

def onAppStart(app):
    app.counter = 0
    app.width = 600
    app.height = 700 
    app.screen = 'start'  

    app.orderNames = [
         None, 
        'coconut latte', 'iced americano',  
        'iced matcha latte', 'hot matcha latte',
        'ube pancake', 'pandan egg waffle',
        'mango bingsoo', 'melon bingsoo'
        ] 

    # images
    app.kitchenImg = CMUImage(Image.open('images/kitchen.png'))
    app.recipeImg = CMUImage(Image.open('images/recipeScene.png'))

# Mouse Press and Change Screen Functions

def onMousePress(app,mouseX,mouseY):
    if app.screen == 'start':
        if (mouseX> 0):
            app.screen = 'kitchen'
    elif app.screen == 'kitchen':
        if (340 <= mouseX <= 500) and (60 <= mouseY <= 180):
            app.screen = 'recipeBook'
    
############################################################
# Start Screen
############################################################

def start_redrawAll(app):
    drawLabel('start', 200, 160, size=24, bold=True)

def start_onKeyPress(app, key):
    if key == 'space':
        setActiveScreen('kitchen')

############################################################
# Kitchen Screen
############################################################

def kitchen_onScreenActivate(app):
    app.moneyMade = 0
    app.moneySpent = 0
    app.served = 0
    custSprite = CMUImage(Image.open('customers/pink-still.png'))
    app.currCust = Customer(custSprite, app.orderNames)

def kitchen_redrawAll(app):
    drawImage(app.kitchenImg, 0, 0, width = app.width, height = app.height)
    drawImage(app.currCust.getImg(), 80, 207, width=189, height=189)
    drawLabel(app.currCust.speak(), 240, 100, size = 10)
    # drawRect(340, 60, 160, 120, fill = 'green', opacity = 50)

def kitchen_onMousePress(app, x, y):
    if (340 <= x <= 500) and (60 <= y <= 180):
        setActiveScreen('recipeBook')
    

############################################################
# Recipe Book Screen
############################################################

def recipeBook_redrawAll(app):
    drawImage(app.recipeImg, 0, 0, width = app.width, height = app.height)

############################################################
# Main
############################################################

def main():
    runAppWithScreens(initialScreen='kitchen')

main()
