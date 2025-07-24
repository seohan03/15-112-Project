orderPrices = [
        None,
        2.99, 1.99,
        2.99, 2.99,
        4.99, 4.99,
        3.99, 3.99
    ]

orderCosts = [
    None,
    .30, .20,
    .40, .40,
    1.50, 1.50,
    .99, .99
]

class Food:
    
    def __init__(self, name, orderList):
        self.name = name
        self.orderPrice = orderPrices[self.getIndex(orderList)]
        self.orderCost = orderCosts[self.getIndex(orderList)]

    def getIndex(self, orderList):
        for i in range(len(orderList)):
            if orderList[i] == self.name:
                return i
    
    
    
# tests:
orderNames = [
         None, 
        'coconut latte', 'iced americano',  
        'iced matcha latte', 'hot matcha latte',
        'ube pancake', 'pandan egg waffle',
        'mango bingsoo', 'melon bingsoo'
        ] 

ube = Food('ube pancake', orderNames)

print(ube.orderCost)
