import random
#Generates 28 dominoe variations
class CDominoes:
    def __init__(self):
        self.dominoes = []
        self.createDominoes()

    def createDominoes(self):
        for i in range(7):
            for j in range(i, 7):
                self.dominoes.append((i,j))
    
    
    def get_dominoes(self):
        return self.dominoes

#Randomizes the domino list
class CRandom:
    def mix(dominoes):    
        random.shuffle(dominoes)
        return dominoes
    

