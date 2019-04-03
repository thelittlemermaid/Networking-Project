import sys
import random
import socket
import pygame
from pygame.locals import *
import random
from random import shuffle
import copy
import pprint
from pprint import pprint

class Card:
    def __init__(self, rank, rankValue, suits, image, *args, **kwargs):
        self._rank = rank
        self._rankValue = rankValue
        self._suits = suits
        self._image = image

    def cardSuit(self, cardSuit):
        self._cardSuit = cardSuit
        return cardSuit

    def cardRank(self, cardRank):
        self._cardRank = cardRank
        return cardRank
    
    def cardImage(self, cardImage):
        self._cardImage = cardImage
        return cardImage
    
    def getImage(self):
        return self._image

    def merge(list1, list2): 
        merged_list = tuple(zip(list1, list2))  
        return merged_list 

class CardDeck:

    def cardDeck():
        suitList = ["s" , "h", "c", "d"]
        rankList = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "q", "k", "a"]
        deck = []
        for rankIndex in range (0, 13):
            for suitsIndex in range (0, 4):
                image = pygame.image.load('cardImages/cards/' + rankList[rankIndex] + suitList[suitsIndex] + '.png')
                newCard = Card(rankList[rankIndex], rankIndex, suitList[suitsIndex], image = image)
                deck.append(newCard)
                            
        return deck

    
    def split_list(a_list):
        half = len(a_list)//2
        return a_list[:half], a_list[half:]


def main():
    playDeck = CardDeck.cardDeck()
    shuffledPlayingDeck = random.sample(playDeck, len(playDeck))
    playerHand, serverHand = CardDeck.split_list(shuffledPlayingDeck)
    # playerWins = 0
    # serverWins = 0
    # count = 0
    print("Player's # of Cards: ", len(playerHand))
    print("Server's # of Cards: ", len(serverHand))
    pprint(vars(playerHand[0]))

    # for card in range(0, 25):
    #     pprint(vars(playerHand[card]))
   

    for card in range(0, 1):
        print("Player's card is: ", playerHand[card])
        print("Server's card is: ", serverHand[card], "\r\n")

    #     playerCard = [item[0] for item in playerHand]
    #     print("PLAYERCARD:", playerCard[card])
    #     serverCard = [item[0] for item in serverHand]
    #     chars = {'j', 'q', 'k', 'a'}
    #     playerRank = []
    #     for char in chars:
    #         for item in playerCard[card]:
    #             if not chars:
    #                 playerRank.append(item)

    #     print('PlayerRANK:', playerRank)

    #     if(playerCard[card] > serverCard[card]):
            
    #         count += 1
    #         playerWins += 1

    #     if(playerCard[card] < serverCard[card]):
            
    #         count += 1
    #         serverWins += 1

    #     if(playerCard[card] == serverCard[card]):
    #       print("War!")
          

    #     print('Player Wins: ', playerWins)
    #     print('Server Wins: ', serverWins, "\r\n")

if __name__ == "__main__":
    main()








# def imageDeck(cardDeck):
    #     images = []
    #     suitList = ["s" , "h", "c", "d"]
    #     rankList = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "q", "k", "a"]
    #     for cards in range(0, 51):
    #             rankIndex = cardDeck.cardRank() 
    #             suitsIndex = cards.cardSuit()
    #             newCard = Card(rankIndex, suitsIndex, number = 0, temp = 0, image = None)
                
    #             images.append(newCard.cardImage(image))

    #     return images

    # def imageDeck():
    #     suitList = ["s" , "h", "c", "d"]
    #     rankList = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "q", "k", "a"]
    #     images = []
    #     for rankIndex in range (0, 13):
    #         for suitsIndex in range (0, 4):
    #             newCard = Card(rankIndex, suitsIndex, number = 0, temp = 0, image = 0)
    #             image = pygame.image.load('cardImages/cards/' + rankList[rankIndex] + suitList[suitsIndex] + '.png')
    #             images.append(newCard.cardImage(image))

    #     return images



# black = (0,0,0)
# white = (255,255,255)
# gray = (192,192,192)


# class GUI:
#     def __init__():
#         pygame.init()
#         screen = pygame.display.set_mode((640, 480))
#         pygame.display.set_caption('War Game')
#         font = pygame.font.SysFont('arial', 15)
#         drawTxt = font.render('Draw', 1, black)
#         restartTxt = font.render('Restart', 1, black)
#         gameoverTxt = font.render('GAME OVER', 1, white)
#         background = pygame.Surface(screen.get_size())
#         background = background.convert()
#         background.fill((80, 150, 15))
#         hitB = pygame.draw.rect(background, gray, (10, 445, 75, 25))
#         standB = pygame.draw.rect(background, gray, (95, 445, 75, 25))
#         ratioB = pygame.draw.rect(background, gray, (555, 420, 75, 50))

# class ClientInteractions:
#     global connection, clientAddress, response
#     def confirmPlay(socket):
#         while True:
#             connection, clientAddress = socket.accept()
#             connection.send("Do you want to play?".encode())
#             response = connection.recv(1024)
#         if (response == "Yes"):
#             sendDeck()
#             #playGame()
#         elif (response == "No"):
#             sys.exit(-1)


#     def sendDeck(shuffledCardDeck, socket):
#         clientOneCards = shuffledCardDeck[:25]
#         clientTwoCards = shuffledCardDeck[26:]
#         connection.send(clientOneCards)


# For Main()


# serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # serverSocket.bind(("127.0.0.1", 51819))
    # serverSocket.listen(2)
    # clientOneSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # clientOneSocket
    # clientTwoSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # print(shuffledCardDeck)
    # window = GUI