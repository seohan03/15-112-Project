from cmu_graphics import *
from recipes.py import *

def onAppStart(app):
    app.width = 200
    app.height = 200
    app.size = 500

    # coffee values
    app.coffeex = 130
    app.coffeey = 190
    app.coffeeWidth = 200
    app.coffeeHeight = 300

def redrawAll(app):
    # drawImage('kitchen.png', 0, 0, width = app.width, height = app.height)
    pass

def main():
    runApp()

main()
