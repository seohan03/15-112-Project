from cmu_graphics import *
from PIL import Image, ImageDraw

# from recipes.py import *

def onAppStart(app):
    app.width = 600
    app.height = 600
    app.stepsPerSecond = 2
    app.stepCounter = 0
    app.kitchenImg = CMUImage(Image.open('images/kitchen.png'))
    

def onStep(app):
    app.stepCounter += 1   

def redrawAll(app):
    drawImage(app.kitchenImg, 0, 0, width = app.width, height = app.height)
    if app.stepCounter%2 == 0:
        customer = CMUImage(Image.open('customers/customers2.png'))
    else:
        customer = CMUImage(Image.open('customers/customers.png'))
    drawImage(customer, 80, 150, width = 190, height = 187)
    # drawImage(app.customer2Img, 50, 150, width = 229, height = 229)



def main():
    runApp()

main()
