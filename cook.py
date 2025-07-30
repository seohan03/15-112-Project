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
        self.finishedOrder  = False
        


    def ingredientUnder(self, x, y):
        for key, (url, ix, iy, iw, ih) in self.ingredients['starter'].items():
            if (ix <= x <= ix+iw) and (iy <= y <= iy+ih):
                return key
        return None
        
    def handleMousePress(self, x, y):

        if self.hitReset(x, y):
            self.resetIngredients()
        
        key = self.ingredientUnder(x, y)

        if (key != None and key != 'emptyBowl' 
                        and key != 'blender' 
                        and key != 'iceCreamTub'):
            self.drag = key
            url, ix, iy, iw, ih = self.ingredients['starter'][key]
            self.offset = (x-ix, y-iy)

        elif (key == 'iceCreamTub'):
            self.drag = 'iceCreamScoop'
            scoopurl, sx, sy, sw, sh = self.ingredients['iceCreamScoop']
            self.ingredients['starter']['iceCreamScoop'] = (scoopurl,
                                                            x-sw/2, y-sh/2, 
                                                            sw, sh)
            
            self.offset = (sw/2, sh/2)

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
            bh = 130 # changing bowl height because png has empty space at top
            
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

    def hitReset(self, x, y):
        return 500 <= x <= 580 and 20 <= y <= 60 # button rect

    def dropIntoBowl(self, ingredient):
        self.placed.add(ingredient)
        self.ingredients['starter'].pop(ingredient, None)

    def bowlImage(self):
        placedSet = set(self.placed)
        bestCombo = tuple()
        maxCombo  = max(len(combo) for combo in 
                        self.ingredients['bowlStates'].keys())
        bestImg   = self.ingredients['bowlStates'][()]

        for combo, imgPath in self.ingredients['bowlStates'].items():
            comboSet = set(combo)
            if comboSet.issubset(placedSet):
                if len(combo) > len(bestCombo):
                    bestCombo = combo
                    bestImg   = imgPath

        self.finishedOrder = (len(bestCombo) == maxCombo)
        

        return bestImg

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

        # reset button is always in same place)
        imgs.append(('reset.png', 500, 20, 80, 40))

        return {'images': imgs}

    def chefSpeak(self):
        return self.steps[self.step]

    def nextStep(self):
        if self.step < len(self.steps) - 1:
            self.step += 1
    

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
    
    def ingredientUnder(self, x, y):

        for key, (url, ix, iy, iw, ih) in self.ingredients['board'].items():
            if (ix <= x <= ix+iw) and (iy <= y <= iy+ih):
                return key

        for key, (url, ix, iy, iw, ih) in self.ingredients['starter'].items():
            if (ix <= x <= ix+iw) and (iy <= y <= iy+ih):
                return key
            
        return None
        
    def handleMouseRelease(self, x, y):
        if self.drag != None:
            key = self.drag
            # ingredient
            url, ix, iy, iw, ih = self.ingredients['starter'][key]
            # bowl
            url, bx, by, bw, bh = self.ingredients['starter']['emptyBowl']
            # chopping board
            cx, cy, cw, ch = 40, 430, 261, 150
            # blender
            blx, bly, blw, blh = 35, 160, 243, 245

            if Cook.overlap(ix, iy, iw, ih, bx, by, bw, bh):
                self.dropIntoBowl(key)
            elif Cook.overlap(ix, iy, iw, ih, cx, cy, cw, ch):
                self.chopFruit(key)
            elif Cook.overlap(ix, iy, iw, ih, blx, bly, blw, blh):
                self.blend(key)

            self.drag = None
    
    def chopFruit(self, fruit):
        url, x, y, w, h = self.ingredients['starter'].pop(fruit)
        choppedUrl = url.replace('Fruit.png', 'Chopped.png') 
        choppedName = f'{fruit}Chopped'
        self.ingredients['starter'][choppedName] = (choppedUrl, x, y, w, h)
        if self.drag == fruit:
            self.drag = choppedName
    
    def blend(self, choppedFruit):
        if choppedFruit == 'mangoChopped' or choppedFruit == 'melonChopped':
            self.ingredients['starter'].pop(choppedFruit, None)
            
            url, x, y, w, h = self.ingredients['starter'].pop('blender')
    
            if choppedFruit == 'mangoChopped':
                blendUrl = f'{bingsooPath}mangoBlender.png'
                blendName = 'mangoBlender'
            else:   
                blendUrl = f'{bingsooPath}melonBlender.png'
                blendName = 'melonBlender'
            
            self.ingredients['starter'][blendName] = (blendUrl, x, y, w, h)
            
            