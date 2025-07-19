from cmu_graphics import *

def onAppStart(app):
    app.width = 600
    app.height = 600

    # coffee values
    app.coffeex = 130
    app.coffeey = 170
    app.coffeeWidth = 500
    app.coffeeHeight = 500

def redrawAll(app):
    drawImage('kitchen.png', 0, 0, width = app.width, height = app.height)
    drawImage('coffee-machine.png', app.coffeex, app.coffeey, 
              width = app.coffeeWidth, height = app.coffeeHeight, 
              align = 'center')



def main():
    runApp()

main()
