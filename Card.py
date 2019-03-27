import sys
import random
import socket
import pygame
from pygame.locals import *
import random
import copy

black = (0,0,0)
white = (255,255,255)
gray = (192,192,192)

class Card:
    # rank = 0
    # suits = 0
    # number = 0
    # Card.next()
    # cardSuit = ""
    # cardRank = ""

    # def __init__(self, val):
    #         self.val = data
    #         self.next = None
    #         self.prev = None

    def __init__(self, rank, suits, number, temp, *args, **kwargs):
        self._rank = rank
        self._suits = suits
        self._number = number
        self._temp = temp
        #self._image = image
    
    # def __init__(self, rank, suits):
    #     self.rank = rank
    #     self.suits = suits

    # def set_rank(self, rank):
    #     self._rank = rank

    # def set_suits(self, suits):
    #     self._suits = suits
      
    # def set_number(self, number):
    #     self._number = number

    def cardSuit(self, cardSuit):
        self._cardSuit = cardSuit
        return cardSuit

    def cardRank(self, cardRank):
        self._cardRank = cardRank
        return cardRank

    # def get_rank(self):
    #     return self._rank

    # def get_suit(self):
    #     return self._suits

    # def get_number(self):
    #     return self._number

    # def get_cardSuit(self):
    #     return self._cardSuit

    # def get_cardRank(self):
    #     return self._cardRank

class CardDeck:
    #deck = []
    rank = 0
    suits = 0
    #counter = 0

    def cardDeck():
        suitList = ["Spades", "Hearts", "Clubs", "Diamonds"]
        rankList = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        deck = []
        for rankIndex in range (0, 13):
            for suitsIndex in range (0, 4):
                newCard = Card(rankIndex, suitsIndex, number = 0, temp = 0)
                deck.append((newCard.cardRank(rankList[rankIndex])) + " of " + (newCard.cardSuit(suitList[suitsIndex])))
        return deck

    def assignImages(deck):
        for card in reversed(deck):
            newCard = Card()
            


    def shuffle(deck):
        tempCard = Card(rank = None, suits = None, number = None, temp = None)
        for card in deck:
            randomNum = random.randint(0, 51)
            tempCard = card
            card = randomNum
            deck[randomNum] = tempCard
        return deck

class GUI:
    def __init__():
        pygame.init()
        screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption('War Game')
        font = pygame.font.SysFont('arial', 15)
        drawTxt = font.render('Draw', 1, black)
        restartTxt = font.render('Restart', 1, black)
        gameoverTxt = font.render('GAME OVER', 1, white)
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((80, 150, 15))
        hitB = pygame.draw.rect(background, gray, (10, 445, 75, 25))
        standB = pygame.draw.rect(background, gray, (95, 445, 75, 25))
        ratioB = pygame.draw.rect(background, gray, (555, 420, 75, 50))

# class ClientInteractions:
#     def confirmPlay(socket):
#         while True:
#             global connection, clientAddress = socket.accept()
#             connection.send("Do you want to play?".encode())
#             global response = connection.recv(1024)
#         if (response == "Yes"):
#             sendDeck()
#             #playGame()
#         elif (response == "No"):
#             sys.exit(-1)


#     def sendDeck(shuffledCardDeck, socket):
#         clientOneCards = shuffledCardDeck[:25]
#         clientTwoCards = shuffledCardDeck[26:]
#         connection.send(clientOneCards)



def main():
    newCardDeck = CardDeck.cardDeck()
    shuffledCardDeck = CardDeck.shuffle(newCardDeck)
    # serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # serverSocket.bind(("127.0.0.1", 51819))
    # serverSocket.listen(2)
    # clientOneSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # clientOneSocket
    # clientTwoSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #print(shuffledCardDeck)
    window = GUI

if __name__ == "__main__":
    main()

   