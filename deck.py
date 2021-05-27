import random 

class Card:
    def __init__(self, val, suit):
        self.val = val 
        self.suit = suit 
    def show(self):
        print(f"{self.val} of {self.suit}")

class Deck:
    def __init__(self, deck_type='standard'):
        self.cards = []
        self.deck_type = deck_type 

        self.build(self.deck_type)

    def build(self, deck_type):
        if deck_type == 'standard':
            for s in ['Spades', 'Hearts', 'Diamonds', 'Clubs']:
                for v in range(1,11):
                    self.cards.append(Card(v, s))
                for f in ['Jack', 'Queen', 'King']:
                    self.cards.append(Card(f, s))
        
    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        random.shuffle(self.cards)

if __name__ == '__main__':
    pass