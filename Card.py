import sys
import random
import socket
import pygame
import random
from random import shuffle
import copy
import pprint
from pprint import pprint

global playerWins
global serverWins
global count

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
    
    def cardRankValue(self, cardRankValue):
        self._cardRankValue = cardRankValue
        return cardRankValue
    
    def getImage(self):
        return self._image

    def getRank(self):
        return self._rank

    def getSuit(self):
        return self._suits
    
    def getRankValue(self):
        return self._rankValue


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

def compareCards(playerHand, serverHand, playerWins, serverWins, count):
    print("\r\n")
    print("Player's # of Cards: ", len(playerHand))
    print("Server's # of Cards: ", len(serverHand))


    for card in (range(len(playerHand)) or range(len(serverHand))):
        print("Player's card is: ", playerHand[0].getRank() + " of " + playerHand[0].getSuit())
        print("Server's card is: ", serverHand[0].getRank() + " of " + serverHand[0].getSuit(), "\r\n")

        if(playerHand[0].getRankValue() > serverHand[0].getRankValue()):
            discard = serverHand.pop(serverHand[0])
            playerHand.append(discard)
            
            count += 1
            playerWins += 1

        elif(playerHand[0].getRankValue() < serverHand[0].getRankValue()):
            discard = playerHand.pop(playerHand[0])
            serverHand.append(discard)
            
            count += 1
            serverWins += 1

        elif(playerHand[0].getRankValue() == serverHand[0].getRankValue()):
            print("War!")

        print("Player's # of Cards: ", len(playerHand))
        print("Server's # of Cards: ", len(serverHand))
        print('Player Wins: ', playerWins)
        print('Server Wins: ', serverWins, "\r\n")

def war(playerHand, serverHand, playerWins, serverWins, count):
    playerWar = []
    serverWar = []

    for item in range(0,3):
        playerWar.append(playerHand.pop(item))
        serverWar.append(serverHand.pop(item))
    
    compareCards(playerHand, serverHand, playerWins, serverWins, count)


def main():
    playerWins = 0
    serverWins = 0
    count = 0
    playDeck = CardDeck.cardDeck()
    shuffledPlayingDeck = random.sample(playDeck, len(playDeck))
    playerHand, serverHand = CardDeck.split_list(shuffledPlayingDeck)
    try:
        while (count <= 30):
            compareCards(playerHand, serverHand, playerWins, serverWins, count)
    except IndexError:
        print("Game Over")
    

            #Can't figure out how to pop three cards at 
            # playerDiscard = playerHand.pop(card[:3])
            # serverDiscard = serverHand.pop(card[:3])

            
            # count += 1
            # serverWins += 1

        

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