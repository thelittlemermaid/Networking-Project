import sys
import random
import socket
import pygame
import random
from random import shuffle
import copy
import pprint
from pprint import pprint
import pickle

playerWins = 0
serverWins = 0
count = 0

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

    if (count <= 30):
        for card in (range(len(playerHand)) or range(len(serverHand))):
            print("\r\n")
            print("Player's # of Cards: ", len(playerHand))
            print("Server's # of Cards: ", len(serverHand))
            playerCard = playerHand.pop(0)
            serverCard = serverHand.pop(0)
            print("Player's card is: ", playerCard.getRank() + " of " + playerCard.getSuit())
            print("Server's card is: ", serverCard.getRank() + " of " + serverCard.getSuit(), "\r\n")
            

            if(playerCard.getRankValue() > serverCard.getRankValue()):
                #discard = serverHand.pop(card)
                playerHand.append(playerCard)
                playerHand.append(serverCard)
                
                count += 1
                playerWins += 1

            elif(playerCard.getRankValue() < serverCard.getRankValue()):
                #discard = playerHand.pop(card)
                serverHand.append(serverCard)
                serverHand.append(playerCard)
                
                count += 1
                serverWins += 1

            elif(playerCard.getRankValue() == serverCard.getRankValue()):
                print("War!")
                count +=1
                discardPile = []
                for item in range(0,3):
                    discardPile.append(playerHand.pop(item))
                    discardPile.append(serverHand.pop(item))

                playerLastCard = playerHand.pop(0)
                serverLastCard = serverHand.pop(0)
                
                result = compareLastCard(playerLastCard, serverLastCard)
                # discardPile.append(playerHand[card])
                # discardPile.append(serverHand[card])
                if(result == 1):
                    playerWins += 1
                    for item in discardPile:
                        playerHand.append(item)
                        # pprint(vars(item))
                elif(result == 0):
                    serverWins += 1
                    for item in discardPile:
                        serverHand.append(item)
                discardPile.clear()

            # print("Player's # of Cards: ", len(playerHand))
            # print("Server's # of Cards: ", len(serverHand))
            print("Game count: ", count)
            print('Player Wins: ', playerWins)
            print('Server Wins: ', serverWins, "\r\n")
        
        
def compareLastCard(playerCard, serverCard):
    player = playerCard.getRankValue()
    server = serverCard.getRankValue()

    if player > server:
        return 1
    else:
        return 0

def main():
    playDeck = CardDeck.cardDeck()
    shuffledPlayingDeck = random.sample(playDeck, len(playDeck))
    playerHand, serverHand = CardDeck.split_list(shuffledPlayingDeck)

    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.bind(('127.0.0.1', 8080))
    # s.listen(5)
    # connect, clientAddress = s.accept()
    
    
    # for card in len(playerHand):
    #     data_string = pickle.dumps(playerHand[card])
    #     s.send(data_string)
    # s.close()

    #gameover = True if (playerWins >= 15) or (serverWins >= 15) or (len(serverHand) == 0) or (len(playerHand) == 0) else False
    try:
        compareCards(playerHand, serverHand, playerWins, serverWins, count)
        #print("Count" , count)
    except IndexError:
        print("Count", count)

        

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


# class create_GUI:
#     def __init__():
#         icon = pygame.image.load('cardImages/icon.png')
#         green = pygame.image.load('cardImages/green.png')

#         pygame.init()
#         # load and set the logo
#         logo = pygame.image.load("cardImages/icon_full.png")
#         pygame.display.set_icon(logo)
#         pygame.display.set_caption("War Card Game")

#         # create a surface on screen that has the size of 240 x 180
#         screen = pygame.display.set_mode((640,480))

#         # define a variable to control the main loop
#         running = True

#         # main loop
#         while running:
#             # event handling, gets all event from the event queue
#             for event in pygame.event.get():
#                 # only do something if the event is of type QUIT
#                 if event.type == pygame.QUIT:
#                     # change the value to False, to exit the main loop
#                     running = False

#             screen.blit(green, (0,0))
#             screen.blit(diamondA, (50,50))
#             screen.blit(clubA, (80, 50))
#             screen.blit(clubK, (50, 300))
#             screen.blit(spadeK, (80, 300))

#             pygame.display.flip()

# class ClientInteractions:
#     global connection, clientAddress, response
#     def confirmPlay(socket):
#         while True:
#             connection, clientAddress = socket.accept()
#             connection.send("Do you want to play?".encode())
#             response = connection.recv(1024)
#         if (response.decode() == "Yes"):
#             #playGame()
#         elif (response.decode() == "No"):
#             sys.exit(-1)

