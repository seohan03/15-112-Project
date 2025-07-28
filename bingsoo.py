mangoSteps: [
    'Place mango on chopping board to cut',
    'Shake mouse to cut',
    'Add cut fruit into freezing blender',
    'Pour shavings into bowl',
    'Drizzle mango jam',
    'Add a scoop of vanilla ice cream',
    'All done!'
] # type: ignore

melonSteps: [
    'Place melon on chopping board to cut',
    'Shake mouse to cut',
    'Add cut fruit into freezing blender',
    'Pour shavings into bowl',
    'Drizzle condensed milk',
    'Add a scoop of vanilla ice cream',
    'All done!'
] # type: ignore

class Bingsoo():
    def __init__(self, chosenRecipe):
        if chosenRecipe == 'Mango Bingsoo':
            self.order = 'mango'
        elif chosenRecipe == 'Melon Bingsoo':
            self.order = 'melon'
        self.step = 0
    
    def chefSpeak(self):
        if self.order == 'mango':
            return mangoSteps[self.step]
        elif self.order == 'melon':
            return melonSteps[self.step]