from bingsoo import *
from pancakes import *

class Cook:

    def __init__(self, chosenRecipe):
        self.chosen = chosenRecipe
        self.step   = 0

    def getAllStarterIngredients(self):
        starterIngredients = dict()
        for key, value in self.ingredients['starter'].items():
            starterIngredients[key] = value

        return starterIngredients

    def chefSpeak(self):
        return self.steps[self.step]

    def nextStep(self):
        if self.step < len(self.steps) - 1:
            self.step += 1

    def getIngredientUnder(self, mx, my):
        for name, (url, x, y, w, h) in self.getAllStarterIngredients().items():
            if x <= mx <= x + w and y <= my <= y + h:
                return name
        return None
    
    def isOnStarterIngredient(self, mx, my):
        return (self.getIngredientUnder(mx, my) is not None)

# Subclasses 

class Pancakes(Cook):
    def __init__(self, chosenRecipe):
        # pick the right step‑list and ingredient map
        if chosenRecipe == 'ube':
            self.steps       = ubeSteps
            self.ingredients = pancakeIngredients
        elif chosenRecipe == 'pandan':
            self.steps       = pandanSteps
            self.ingredients = pancakeIngredients

class Bingsoo(Cook):
    def __init__(self, chosenRecipe):
        super().__init__(chosenRecipe)
        if chosenRecipe == 'mango':
            self.steps       = mangoSteps
            self.ingredients = bingsooIngredients
        elif chosenRecipe == 'melon':
            self.steps       = melonSteps
            self.ingredients = bingsooIngredients
        else:
            raise ValueError(f"Unknown bingsoo type: {chosenRecipe}")
