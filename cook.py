from bingsoo import *
from pancakes import *
import copy

class Cook:

    def __init__(self, chosenRecipe):
        self.chosen = chosenRecipe
        self.step   = 0
        self.placed = []
        self.ogStarter = copy.deepcopy(self.ingredients['starter'])

        
    def recordDrop(self, ingre):
        if ingre not in self.placed:
            self.placed.append(ingre)
            self.ingredients['starter'].pop(ingre, None)

    def resetIngredients(self):
        self.placed = []
        self.ingredients['starter'] = copy.deepcopy(self.ogStarter)
    
    def getBowlImage(self):
        placedSet = set(self.placed)
        bestCombo = tuple()
        bestImg = self.ingredients['bowlStates'][()]

        for combo, imgPath in self.ingredients['bowlStates'].items():
            comboSet = set(combo)
            if comboSet.issubset(placedSet):
                if len(combo) > len(bestCombo):
                    bestCombo = combo
                    bestImg   = imgPath

        return bestImg


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
        self.placed = []
        if chosenRecipe == 'ube':
            self.steps       = ubeSteps
            self.ingredients = pancakeIngredients
        elif chosenRecipe == 'pandan':
            self.steps       = pandanSteps
            self.ingredients = pancakeIngredients
        self.ogStarter = copy.deepcopy(self.ingredients['starter'])

class Bingsoo(Cook):
    def __init__(self, chosenRecipe):
        self.placed = []
        if chosenRecipe == 'mango':
            self.steps       = mangoSteps
            self.ingredients = bingsooIngredients
        elif chosenRecipe == 'melon':
            self.steps       = melonSteps
            self.ingredients = bingsooIngredients
        else:
            raise ValueError(f"Unknown bingsoo type: {chosenRecipe}")
        self.ogStarter = copy.deepcopy(self.ingredients['starter'])
