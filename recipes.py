class Recipe():

    def __init__(self, orderName):
        self.orderName = orderName
    
    def getRecipePage(self):
        if (self.orderName == 'Ube Pancake' or 
            self.orderName == 'Pandan Egg Waffle'):
            return 'pancakePage'
        elif (self.orderName == 'Coconut Latte' or 
              self.orderName == 'Iced Americano'):
            return 'coffeePage'
        elif(self.orderName == 'Iced Matcha Latte' or 
             self.orderName == 'Hot Matcha Latte'):
            return 'matchaPage'
        elif(self.orderName == 'Melon Bingsoo' or 
             self.orderName == 'Mango Bingsoo'):
            return 'bingsooPage'
    
    def getRecipeBookScreen(self):
        recipe = self.getRecipePage()
        if recipe == 'pancakePage':
            return 'recipes/pancakePage.png'
        elif recipe == 'coffeePage':
            return 'recipes/coffeePage.png'
        elif recipe == 'matchaPage':
            return 'recipes/matchaPage.png'
        elif recipe == 'bingsooPage':
            return 'recipes/bingsooPage.png'
    
    def isOnReady(self, x, y):
        return (((75 <= x <= 225) and (410 <= y <= 490)) or 
                ((380 <= x <= 530) and (410 <= y <= 490)))
        
    def getSideOfPage(self, x, y):
        # Left page
        if (75 <= x <= 225) and (410 <= y <= 490):
            return 'leftPage'
        # Right page
        elif (380 <= x <= 530) and (410 <= y <= 490):
            return 'rightPage'
    
    def getGameImg(self):
        if self.getRecipePage() == 'pancakePage':
            return 'recipes/food/pancakeKitchen.png'
        elif self.getRecipePage() == 'bingsooPage':
            return 'recipes/food/bingsooKitchen.png'
        elif self.getRecipePage() == 'coffeePage':
            return 'recipes/food/coffeeKitchen.png'
        elif self.getRecipePage() == 'matchaPage':
            return 'recipes/food/matchaKitchen.png'
    
    def getChosenRecipe(self, x, y):
        sideOfPage = self.getSideOfPage(x, y)
        recipeBook = self.getRecipePage()

        if sideOfPage == 'leftPage':
            if recipeBook == 'pancakePage':
                return 'Ube Pancake'
            elif recipeBook == 'coffeePage':
                return 'Coconut Latte'
            elif recipeBook == 'matchaPage':
                return 'Iced Matcha'
            elif recipeBook == 'bingsooPage':
                return 'Melon Bingsoo'
            
        elif sideOfPage == 'rightPage':
            if recipeBook == 'pancakePage':
                return 'Pandan Egg Waffle'
            elif recipeBook == 'coffeePage':
                return 'Iced Americano'
            elif recipeBook == 'matchaPage':
                return 'Hot Matcha Latte'
            elif recipeBook == 'bingsooPage':
                return 'Mango Bingsoo'
