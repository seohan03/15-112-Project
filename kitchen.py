class Kitchen():

    def __init__(self, completedOrder):
        self.order = completedOrder
    
    def handleMousePress(self, x, y):
        if (app.orderx <= mouseX <= app.orderx + app.orderw and
            app.ordery <= mouseY <= app.ordery + app.orderh):
            