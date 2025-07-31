import random

phrases = [
    'Hello may I please\nget order please',
    'mmm the order\nsounds perfect today',
    'My friend told me to try\nthe order, get me one of those!'
]

class Customer:
    def __init__(self, image, ordersDict):
        self.sprite    = image
        names          = list(ordersDict)
        index          = random.randrange(len(names))
        self.orderName = names[index]
        self.price, self.cost = ordersDict[self.orderName]

        templateIndex   = random.randrange(len(phrases))
        self.phraseTemp = phrases[templateIndex]

            
    def speak(self):
        orderIdx = self.phraseTemp.find('order')
        return (
            self.phraseTemp[:orderIdx]
            + self.orderName
            + self.phraseTemp[orderIdx+5:]
        )

    def isSatisfied(self, givenOrder):
        return givenOrder == self.orderName


