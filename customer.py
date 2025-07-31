import random

phrases = [
    'Hello may I please\nget order please',
    'mmm the order\nsounds perfect today',
    'My friend told me to try\nthe order, \nget me one of those!'
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
    
    def getSpeakLines(self):
        lines = []
        ogLine = self.speak()
        parts = ogLine.split('\n')

        lineHeight = 12
        marginy = 80
        for part in parts:
            lines.append((part, marginy))
            marginy += lineHeight

        return lines

    def isSatisfied(self, givenOrder):
        return givenOrder == self.orderName


