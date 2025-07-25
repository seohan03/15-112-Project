import random

phrases = [
    'Hello may I please\nget order please',
    'mmm the order\nsounds perfect today',
    'My friend told me to try\nthe order, get me one of those!'
]

class Customer:
            self.phrase = phrases[0]
    def __init__(self, image, ordersDict):
        self.sprite = image

        names = [name for name in ordersDict]
        index = random.randrange(len(names))
        self.orderName  = names[index]
        
        self.price, self.cost = ordersDict[self.orderName]
    
    def speak(self):
        phrase = phrases[random.randrange(len(phrases))]
        orderIdx = phrase.find('order')
        return phrase[:orderIdx] + self.orderName + phrase[orderIdx+5:]

