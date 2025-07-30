mangoSteps = [
    '''Make sure to do these in order!! 
    and be careful not to get anything stuck in the blender''',
    'Place mango on chopping board to cut',
    'Shake mouse to cut',
    'Add cut fruit into freezing blender',
    'Pour shavings into bowl',
    'Drizzle mango jam',
    'Add a scoop of vanilla ice cream',
    'All done!'
] 

melonSteps = [
    '''Make sure to do these in order!! 
    and be careful not to get anything stuck in the blender''',
    'Place melon on chopping board to cut',
    'Shake mouse to cut',
    'Add cut fruit into freezing blender',
    'Pour shavings into bowl',
    'Drizzle condensed milk',
    'Add a scoop of vanilla ice cream',
    'All done!'
] 

# IngredientName = (imageURL, left, top, width, height)
bingsooPath = 'recipes/ingredients/bingsoo/'
bingsooIngredients = {
    'starter' : {
                'blender'       : (f'{bingsooPath}blender.png',
                                    35, 160, 243, 245),
                'condensedMilk' : (f'{bingsooPath}condensedMilk.png', 
                                    375, 158, 73, 86),
                'emptyBowl'     : (f'{bingsooPath}emptyBowl.png', 
                                    355, 365, 205, 231),
                'mango'         : (f'{bingsooPath}mangoFruit.png', 
                                    465, 185, 113, 74),
                'melon'         : (f'{bingsooPath}melonFruit.png', 
                                    475, 273, 107, 99),
                'iceCreamTub'   : (f'{bingsooPath}iceCreamTub.png', 
                                    295, 255, 159, 120),
                'jam'           : (f'{bingsooPath}jam.png', 
                                    295, 155, 69, 91),
    },

    'board' : {

    },

    'boardArea' : (40, 430, 261, 150),

    'bowlStates': {
                () : (f'{bingsooPath}emptyBowl.png'),
                ('mangoBlender') : 
                                (f'{bingsooPath}mangoBowl.png'),
                ('melonBlender') : 
                                (f'{bingsooPath}melonBowl.png'),
                ('mangoBlender', 'jam') : 
                                (f'{bingsooPath}mangoWithJam.png'),
                ('melonBlender', 'condensedMilk') : 
                                (f'{bingsooPath}melonWithMilk.png')
    },
                
    'mangoBlender'  : (f'{bingsooPath}mangoBlender.png', 
                        190, 145, 85, 141),
    'melonBlender'  : (f'{bingsooPath}melonBlender.png', 
                        190, 145, 85, 141),
    'mangoChopped'  : (f'{bingsooPath}mangoChopped.png', 
                        190, 145, 85, 141),
    'melonChopped'  : (f'{bingsooPath}melonChopped.png', 
                        440, 160, 57, 66),
    'iceCreamScoop' : (f'{bingsooPath}iceCreamScoop.png', 
                        490, 235, 69, 71),
    
}