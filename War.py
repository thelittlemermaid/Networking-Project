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
from threading import Thread
import time

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

def saveImages(playerHand):
    for card in playerHand:
        pygame.image.tostring(card.getImage(), 'RGBA', False)

def compareCards(playerHand, serverHand, playerWins, serverWins, count, screen, playerWinTxt, ServerWinTxt, WarTxt):
    if (count <= 20):
        for card in (range(len(playerHand)) or range(len(serverHand))):
            print("Player's # of Cards: ", len(playerHand))
            print("Server's # of Cards: ", len(serverHand))
            print("\r\n")
            playerCard = playerHand.pop(0)
            serverCard = serverHand.pop(0)
            t = Thread(target=displayCards, args=(playerCard, serverCard, screen, playerWinTxt, ServerWinTxt, WarTxt, discardPile))
            t.start()
            #displayCards(playerCard, serverCard, screen)
            pygame.display.flip()


            time.sleep(2)
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
                discardPile.append(playerCard)
                discardPile.append(serverCard)
                for item in range(0,3):
                    discardPile.append(playerHand.pop(0))
                    discardPile.append(serverHand.pop(0))

                playerLastCard = playerHand.pop(0)
                serverLastCard = serverHand.pop(0)

                result = compareLastCard(playerLastCard, serverLastCard)
                # discardPile.append(playerHand[card])
                # discardPile.append(serverHand[card])
                if(result == 1):
                    playerWins += 1
                    for item in discardPile:
                        playerHand.append(item)
                    playerHand.append(playerLastCard)
                    playerHand.append(serverLastCard)
                        # pprint(vars(item))
                elif(result == 0):
                    serverWins += 1
                    for item in discardPile:
                        serverHand.append(item)
                    serverHand.append(playerLastCard)
                    serverHand.append(serverLastCard)
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


def displayCards(playerCard, serverCard, screen, playerWinTxt, ServerWinTxt, WarTxt, discardPile):
    screen.blit(playerCard.getImage(), (50,80))
    screen.blit(serverCard.getImage(), (50,300))
    if(playerCard.getRankValue() == serverCard.getRankValue()):
        screen.blit(discardPile[0], (60, 80))

    pygame.display.flip()

    if(playerCard.getRankValue() > serverCard.getRankValue()):
        screen.blit(playerWinTxt, (50, 480))
        pygame.display.flip()
    elif(playerCard.getRankValue() < serverCard.getRankValue()):
        screen.blit(ServerWinTxt, (50, 480))
        pygame.display.flip()
    else:
        screen.blit(WarTxt, (50,480))
        pygame.display.flip()


def main():
    playDeck = CardDeck.cardDeck()
    shuffledPlayingDeck = random.sample(playDeck, len(playDeck))
    playerHand, serverHand = CardDeck.split_list(shuffledPlayingDeck)

    black = (0,0,0)
    white = (255,255,255)
    gray = (192,192,192)


    pygame.init()
    # load and set the logo
    logo = pygame.image.load("cardImages/icon_full.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("War Card Game")

    # create a surface on screen that has the size of
    screen = pygame.display.set_mode((640,480))

    icon = pygame.image.load('cardImages/icon.png')
    green = pygame.image.load('cardImages/green.png')
    font = pygame.font.SysFont('arial', 26)
    playerWinTxt = font.render('Player Wins', 1, black)
    ServerWinTxt = font.render("Server Wins", 1, black)
    WarTxt = font.render("WAR!", 1, black)
    screen.blit(green, (0,0))
    pygame.display.flip()

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    break # break out of the for loop
            elif event.type == pygame.QUIT:
                running = False
                break # break out of the for loop



        discardPile = []
        compareCards(playerHand, serverHand, playerWins, serverWins, count, screen, playerWinTxt, ServerWinTxt, WarTxt)
        # try:
        #     compareCards(playerHand, serverHand, playerWins, serverWins, count, screen)
        #     #print("Count" , count)
        # except IndexError:
        #     print("Index Error")

        # screen.blit(playerHand[0].getImage(), (50, 80))
        pygame.display.flip()






    # sockServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sockServer.bind(('127.0.0.1', 8080))
    # print("Listening..")
    # sockServer.listen(5)
    # while True:
    #
    #     #Establish connection with client
    #     sockConnect, sockAddr = sockServer.accept()
    #     print('Connection made: ', sockAddr)
    #     print(sockConnect.recv(1024))
    #     saveImages(playerHand)
    #     for card in range(26):
    #         data_string = pickle.dumps(playerHand[card])
    #         sockConnect.send(data_string.encode())
    #
    #     #Close the socket connection
    #     sockConnect.close()


    #gameover = True if (playerWins >= 15) or (serverWins >= 15) or (len(serverHand) == 0) or (len(playerHand) == 0) else False




if __name__ == "__main__":
    main()
