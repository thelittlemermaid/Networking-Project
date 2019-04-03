import sys
import random
import socket
import pygame
from pygame.locals import *
import random
from random import shuffle
import copy

black = (0,0,0)
white = (255,255,255)
gray = (192,192,192)

class Card:
    def __init__(self, rank, suits, number, temp, image, *args, **kwargs):
        self._rank = rank
        self._suits = suits
        self._number = number
        self._temp = temp
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
                newCard = Card(rankIndex, suitsIndex, number = 0, temp = 0, image = 0)
                deck.append((newCard.cardRank(rankList[rankIndex])) + (newCard.cardSuit(suitList[suitsIndex])))
                            
        return deck

    def imageDeck():
        suitList = ["s" , "h", "c", "d"]
        rankList = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "q", "k", "a"]
        images = []
        for rankIndex in range (0, 13):
            for suitsIndex in range (0, 4):
                newCard = Card(rankIndex, suitsIndex, number = 0, temp = 0, image = 0)
                image = pygame.image.load('cardImages/cards/' + rankList[rankIndex] + suitList[suitsIndex] + '.png')
                images.append(newCard.cardImage(image))

        return images
    
    def split_list(a_list):
        half = len(a_list)//2
        return a_list[:half], a_list[half:]


def main():
    newCardDeck = CardDeck.cardDeck()
    newImageDeck = CardDeck.imageDeck()
    newPlayingDeck = Card.merge(newCardDeck, newImageDeck)
    playerWins = 0
    serverWins = 0
    count = 0
    #print(newPlayingDeck)
    shuffledPlayingDeck = random.sample(newPlayingDeck, len(newPlayingDeck))
    playerHand, serverHand = CardDeck.split_list(shuffledPlayingDeck)
    print("Player's # of Cards: ", len(playerHand))
    print("Server's # of Cards: ", len(serverHand))
    
    for card in range(0, 10):

        print("Player's card is: ", playerHand[card])
        print("Server's card is: ", serverHand[card], "\r\n")
       
        
        playerHand[card]
        serverHand[card]
        playerCard = [item[card] for item in playerHand]
        serverCard = [item[card] for item in serverHand]
        print('Player Wins: ', playerWins)
        print('Server Wins: ', serverWins, "\r\n")
        if(playerCard > serverCard):
            
            count += 1
            playerWins += 1

        if(playerCard < serverCard):
            
            count += 1
            serverWins += 1


if __name__ == "__main__":
    main()






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