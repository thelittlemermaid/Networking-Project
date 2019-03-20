import sys

class Card:
    rank = 0
    suits = 0
    number = 0
    #Card.next()
    cardSuit = ""
    cardRank = ""

    def __init__(self, val):
            self.val = data
            self.next = None
            self.prev = None

    def Card(self, rank, suits, number, temp):
        self._rank = rank
        self._suits = suits
        self._number = number
        self._temp = temp

    def set_rank(self, rank):
        self._rank = rank

    def set_suits(self, suits):
        self._suits = suits
      
    def set_number(self, number):
        self._number = number

    def set_cardSuit(self, cardSuit):
        self._cardSuit = cardSuit

    def set_cardRank(self, cardRank):
        self._cardRank = cardRank

    def get_rank(self):
        return self._rank

    def get_suit(self):
        return self._suits

    def get_number(self):
        return self._number

    def get_cardSuit(self):
        return self._cardSuit

    def get_cardRank(self):
        return self._cardRank

class CardDeck:
    deck = []
    rank = 0
    suits = 0
    counter = 0

    def cardDeck():
        for rankIndex in range (0, 13):
            for suitsIndex in range (0, 4):
                print(rankIndex)
                #deck[counter] = 

def main():
    CardDeck.cardDeck()

if __name__ == "__main__":
    main()