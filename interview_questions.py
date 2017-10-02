import random
""" Move non-zeros to the start of the array in as few writes as possible
[1, 0, 3, 1, 2, 0, 5, 0] => [1, 1, 3, 5, 2, ?, ?, ?]
"""
def removeZeros(arr):
    """
    Input: Array of numbers
    Output: Input array with all non-zero values appearing before zero values
    Constraint: Use minimum number of writes

    """

    start_index = 0
    end_index = len(arr) - 1
    while start_index < end_index:
        if arr[start_index] != 0:
            start_index += 1
        else:
            while arr[end_index] == 0 and end_index > start_index:
                end_index -= 1
            if arr[end_index] != 0:
                arr[start_index] = arr[end_index]
                start_index +=1
                end_index -= 1




"""interpretations of a number string?
a=1,b=2,z=26 etc

11 = 2 (aa, k)
111 = 3 (aaa, ak, ka)
90 = 0
20 = 1 (t)
"""
def numberOfInterpretations(numberString):
    """
    Input: String of digits
    Output: Integer indicating the number of ways the string of digits can be
    interpreted using the mapping:  a=1, b=2, c=3,...,z = 26
    """
    counts = [None for _ in numberString]
    return interpretation_count(numberString,counts)
def interpretation_count(numberString,counts):
    if  numberString == "":
        return 0
    digit = int(numberString[0:1])
    if digit == 0:
        return 0
    num = int(numberString)
    if  num < 11 or num == 20:
        return 1
    if num < 27:
        return 2
    index = len(numberString) - 1
    if counts[index] == None:
        count =  interpretation_count(numberString[1:],counts)
        digits = int(numberString[0:2])
        if digits < 27:
            count += interpretation_count(numberString[2:],counts)
        counts[index] = count
    return counts[index]
"""
We will be implementing a modified version of the board game Set.  Our Set deck contains 27 cards
with three attributes each: shape, number, and fill.  Possible values are:
    shapes = ["oval", "squiggle", "diamond"]
    shading = ["solid","striped","open"]
    counts = [1,2,3]

Create a class that models a set card and provides a method to print itself.
Create a SetGame class.  On initialization generate a deck of Set cards stored within the class
instance.  Order is unimportant.

Edit SetGame to track the cards on the table in an instnace variable, table, & provide a deal(num_cards)
method to deal random cards.

Write a function is_set() that accepts three cards and returns a boolean indicating whether for each attribute
all cards match or all cards differ.
"""
class Card:
    def __init__(self,shape,fill,count):
        self.shape = shape
        self.fill = fill
        self.count = count

    def __repr__(self):
        return "shape: %s, fill: %s, count: %s" %(self.shape,self.fill,self.count)
class SetGame(object):
    def __init__(self):
        self.deck = []
        self.table = []
        shapes = ["oval", "squiggle", "diamond"]
        shading = ["solid","striped","open"]
        counts = [1,2,3]
        for shape in shapes:
            for shade in shading:
                for count in counts:
                    card = Card(shape,shade,count)
                    self.deck.append(card)
    def deal(self,num_cards):
        for i in range(min(num_cards,len(self.deck))):
            total = len(self.deck)
            index = random.randint(0,total-1)
            self.table.append(self.deck.pop(index))
    def is_set(self,card):
        cards = [card1,card2,card3]
        shapes = set()
        fills = set()
        counts = set()
        for card in cards:
            shapes.add(card.shape)
            fills.add(card.fill)
            counts.add(card.count)
        if (len(shapes == 2) or len(fills == 2) or len(counts == 2)):
            return False
        return True

if __name__ == "__main__":
    arr = [1, 0, 3, 1, 2, 0, 5, 0]
    removeZeros(arr)
    print arr
    print numberOfInterpretations('11')
    print numberOfInterpretations('111')
    print numberOfInterpretations('90')
    print numberOfInterpretations('20')
    print numberOfInterpretations('1119')
    print numberOfInterpretations('00')
    print numberOfInterpretations('200')
    print numberOfInterpretations('202')
    game = SetGame()
    print game.deck
    game.deal(4)
    for card in game.table:
        print card
