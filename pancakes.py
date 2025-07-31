# Controls all the mouse clicks/drags for cooking pancakes

ubeSteps = [
    'Make sure to do these in order!!',
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
    'Make sure to do these in order!!',
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
pancakePath = 'recipes/ingredients/pancakes/'
pancakeIngredients = {
    'starter'   : {
                    'flour'         : (f'{pancakePath}flour.png', 
                                    65, 140, 122, 147),
                    'milk'          : (f'{pancakePath}milk.png', 
                                    190, 145, 85, 141),
                    'egg'           : (f'{pancakePath}egg.png', 
                                    440, 160, 57, 66),
                    'ubeYam'        : (f'{pancakePath}ubeYam.png', 
                                    360, 220, 121, 80),
                    'pandanExtract' : (f'{pancakePath}pandanExtract.png', 
                                    490, 235, 69, 71),
                    'emptyBowl'     : (f'{pancakePath}bowl.png',
                                    350, 350, 205, 157),
                    'spoon'         : (f'{pancakePath}spoon.png',
                                    150, 150, 90, 150)
                },

    'bowlStates': {
                    () : f'{pancakePath}bowl.png',
                    ('flour',) : 
                                    f'{pancakePath}bowl1.png',
                    ('flour', 'egg') : 
                                    f'{pancakePath}bowl2.png',
                    ('flour', 'egg', 'milk') : 
                                    f'{pancakePath}bowl3.png',
                    ('flour', 'egg', 'milk', 'pandanExtract') : 
                                    f'{pancakePath}bowlWithPandan.png',
                    ('flour', 'egg', 'milk', 'pandanExtract', 'spoon') : 
                                    f'{pancakePath}pandanMix.png',
                    ('flour', 'egg', 'milk', 'ubeYam') : 
                                    f'{pancakePath}bowlWithUbe.png',
                    ('flour', 'egg', 'milk', 'ubeYam', 'spoon') : 
                                    f'{pancakePath}ubeMix.png',

                }

}