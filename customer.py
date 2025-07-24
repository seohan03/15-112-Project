import random
from food import Food

phrases = [
    "I'm indecisive,\nget me whatever you want!",
    'Hello may I please\nget order please',
    'mmm the order\nsounds perfect today',
    'My friend told me to try\nthe order, get me one of those!'
]

class Customer:
    def __init__(self, image, orderNames):
        self.image = image
        self.order  = orderNames[random.randrange(0, 9)]
        if self.order == None:
            self.phrase = phrases[0]
        else: self.phrase = phrases[random.randrange(1, 4)]

    def getImg(self):
        return self.image

    def getOrder(self):
        return self.order

    def speak(self):
        if self.order != None:
            phrase = self.phrase
            orderIdx = phrase.find('order')
            return phrase[:orderIdx] + self.order + phrase[orderIdx+5:]
        else:
            return self.phrase