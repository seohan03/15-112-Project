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

# IngredientName = (imageURL, left, top, width, height)
bingsooPath = 'recipes/ingredients/bingsoo/'
bingsooIngredients = {
    'starter' : {
                'blender'       : (f'{bingsooPath}blender.png',
                                    65, 140, 122, 147),
                'condensedMilk' : (f'{bingsooPath}condensedMilk.png', 
                                    360, 220, 121, 80),
                'emptyBowl'     : (f'{bingsooPath}emptyBowl.png', 
                                    490, 235, 69, 71),
                'mangoFruit'    : (f'{bingsooPath}mangoFruit.png', 
                                    490, 235, 69, 71),
                'melonFruit'    : (f'{bingsooPath}melonFruit.png', 
                                    490, 235, 69, 71),
                'iceCreamTub'   : (f'{bingsooPath}iceCreamTub.png', 
                                    490, 235, 69, 71),
                'jam'           : (f'{bingsooPath}jam.png', 
                                    490, 235, 69, 71),
    },
                
    'mangoBlender'  : (f'{bingsooPath}mangoBlender.png', 
                        190, 145, 85, 141),
    'melonBlender'  : (f'{bingsooPath}melonBlender.png', 
                        190, 145, 85, 141),
    'choppedMango'  : (f'{bingsooPath}choppedMango.png', 
                        190, 145, 85, 141),
    'choppedMelon'  : (f'{bingsooPath}choppedMelon.png', 
                        440, 160, 57, 66),
    
    'mangoBowl'     : (f'{bingsooPath}mangoBowl.png', 
                        490, 235, 69, 71),
    'melonBowl'     : (f'{bingsooPath}melonBowl.png', 
                        490, 235, 69, 71),
    'mangoWithJam'  : (f'{bingsooPath}mangoWithJam.png', 
                        490, 235, 69, 71),
    'melonWithMilk' : (f'{bingsooPath}melonWithMilk.png', 
                        490, 235, 69, 71),
    'iceCreamScoop' : (f'{bingsooPath}iceCreamScoop.png', 
                        490, 235, 69, 71),
}