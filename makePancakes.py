# Controls all the mouse clicks/drags for cooking pancakes

ubeSteps = [
    'Add the pancake mix',
    'Add egg into the bowl',
    'Add milk into the bowl',
    'Mash in the ube',
    'Mix all together',
    'Pour mixture into the frying pan',
    'Cook and flip once color changes',
    'All done!'
]

pandanSteps = [
    'Add the pancake mix',
    'Add egg into the bowl',
    'Add milk into the bowl',
    'Add in the pandan extract',
    'Mix all together',
    'Pour mixture into the egg waffle pan',
    'Cook and flip the pan once there is steam',
    'All done!'
]

# IngredientName = (imageURL, left, top, width, height)
ingredients = {
    'flour' : ('recipes/ingredients/pancakes/flour.png', 65, 140, 122, 147),
    'milk' : ('recipes/ingredients/pancakes/milk.png', 190, 145, 85, 141),
    'egg' : ('recipes/ingredients/pancakes/egg.png', 440, 160, 57, 66),
    'ubeYam' : ('recipes/ingredients/pancakes/egg.png', 360, 220, 121, 80),
    'pandanExtract' : ('recipes/ingredients/pancakes/pandanExtract.png', 
                       490, 235, 69, 71)
}

class Pancakes():

    def __init__(self, orderName):
        if orderName == 'Ube Pancake':
            self.order = 'ube'
        elif orderName == 'Pandan Egg Waffle':
            self.order = 'pandan'
        self.step = 0
    
    # def mouseOnIngredient(self, x, y):
    #     if 
        
    def chefSpeak(self):
        if self.order == 'ube':
            return ubeSteps[self.step]
        elif self.order == 'pandan':
            return pandanSteps[self.step]

