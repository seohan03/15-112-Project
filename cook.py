from bingsoo import *
from pancakes import *
import copy


class Cook:

    def __init__(self, chosenRecipe, ingredients, steps):
        self.chosen         = chosenRecipe
        self.step           = steps
        self.placed         = set()
        self.ingredients    = copy.deepcopy(ingredients)  
        self.ogStarter      = copy.deepcopy(ingredients['starter'])
        self.drag           = None
        self.offset         = (0, 0)

    def handleMousePress(self, x, y):
        if self.hitReset(x, y):
            self.resetIngredients()
        
        key = self.ingredientUnder(x, y)
        if key != None and key != 'emptyBowl':
            self.drag = key
            url, ix, iy, iw, ih = self.ingredients['starter'][key]
            self.offset = (x-ix, y-iy)

    def handleMouseDrag(self, x, y):
        if self.drag:
            url, ix, iy, iw, ih = self.ingredients['starter'][self.drag]
            dx, dy = self.offset
            self.ingredients['starter'][self.drag] = (url, x-dx, y-dy, iw, ih)
    
    def handleMouseRelease(self, x, y):
        if self.drag != None:
            key = self.drag
            # ingredient
            url, ix, iy, iw, ih = self.ingredients['starter'][key]
            # bowl
            url, bx, by, bw, bh = self.ingredients['starter']['emptyBowl']
            
            if self.overlap(ix, iy, iw, ih, bx, by, bw, bh):
                self.dropIntoBowl(key)
            
            self.drag = None

    def recordDrop(self, ingre):
        if ingre not in self.placed:
            self.placed.append(ingre)
            self.ingredients['starter'].pop(ingre, None)

    def resetIngredients(self):
        self.placed.clear()
        self.ingredients['starter'] = copy.deepcopy(self.ogStarter)
    
    def ingredientUnder(self, x, y):
        for key, (url, ix, iy, iw, ih) in self.ingredients['starter'].items():
            if (ix <= x <= ix+iw) and (iy <= y <= iy+ih):
                return key
        return None

    def hitReset(self, x, y):
        return 500 <= x <= 580 and 20 <= y <= 60 # button rect

    def dropIntoBowl(self, ingredient):
        self.placed.add(ingredient)
        self.ingredients['starter'].pop(ingredient, None)

    def bowlImage(self):
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

    def getScene(self):
        imgs = []
        for key, (url, x, y, w, h) in self.ingredients['starter'].items():
            if key != 'emptyBowl' and key != self.drag:
                imgs.append((url, x, y, w, h))
        
        bowlUrl = self.bowlImage()
        url, bx, by, bw, bh = self.ingredients['starter']['emptyBowl']
        imgs.append((bowlUrl, bx, by, bw, bh))

        if self.drag:
            url, x, y, w, h = self.ingredients['starter'][self.drag]
            imgs.append((url, x, y, w, h))

        for key, (url, x, y, w, h) in self.ingredients['board'].items():
            imgs.append((url, x, y, w, h))

        # reset button is always in same place)
        imgs.append(('reset.png', 500, 20, 80, 40))

        return {'images': imgs}

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

    @staticmethod
    def overlap(x1,y1,w1,h1,x2,y2,w2,h2):
            return not (x1+w1 < x2 or x1 > x2+w2 or
                        y1+h1 < y2 or y1 > y2+h2)


# Subclasses 

class Pancakes(Cook):
    def __init__(self, chosenRecipe):
        # pick the right step‑list and ingredient map
        super().__init__(chosenRecipe, pancakeIngredients,
                         steps=ubeSteps if 'ube' in chosenRecipe 
                         else pandanSteps)


class Bingsoo(Cook):
    def __init__(self, chosenRecipe):
        super().__init__(chosenRecipe, bingsooIngredients,
                         steps=mangoSteps if 'mango' in chosenRecipe 
                         else melonSteps)
        
    def handleMouseRelease(self, x, y):
        if self.drag != None:
            key = self.drag
            # ingredient
            url, ix, iy, iw, ih = self.ingredients['starter'][key]
            # bowl
            url, bx, by, bw, bh = self.ingredients['starter']['emptyBowl']
            # chopping board
            cx, cy, cw, ch = 40, 430, 261, 150

            if self.overlap(ix, iy, iw, ih, bx, by, bw, bh):
                self.dropIntoBowl(key)
            elif self.overlap(ix, iy, iw, ih, cx, cy, cw, ch):
                self.chopFruit(key)

            self.drag = None
    
    def chopFruit(self, fruit):
        url, x, y, w, h = self.ingredients['starter'].pop(fruit, None)
        newUrl = url.replace('.png', 'Chopped.png')

        bx, by, bw, bh = self.ingredients['boardArea']
        x = bx + (bw-w)//2
        y = by + (bh-h)//2

        self.ingredients['board'][fruit] = (newUrl, x,y , w, h)

