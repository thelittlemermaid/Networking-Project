import sys
import os
import random
import socket
import pygame
import random
from random import shuffle
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

def compareCards(client_socket, playerHand, serverHand, playerWins, serverWins, count, screen, playerWinTxt, ServerWinTxt, WarTxt):
    font = pygame.font.SysFont("arial", 15)
    print("Player's # of Cards: ", len(playerHand))
    print("Server's # of Cards: ", len(serverHand))
    print("\r\n")
    scoreBox(screen, ("# of Player Cards:" + str(len(playerHand))), playerWins, serverWins, playerHand, serverHand, 400, 400)
    scoreBox(screen, ("# of Server Cards:" + str(len(serverHand))), playerWins, serverWins, playerHand, serverHand, 400, 425)
    playerCard = playerHand.pop(0)
    serverCard = serverHand.pop(0)
    cards = [playerCard.getRankValue(), serverCard.getRankValue()]
    client_socket.send(str(cards).encode())
    response = (client_socket.recv(4096)).decode()

    textSurf, textRect = text_objects("Client:", font, pygame.Color(0,0,0))
    textRect.center = (95, 60)
    screen.blit(textSurf, textRect)
    textSurf, textRect2 = text_objects("Server:", font, pygame.Color(0,0,0))
    textRect2.center = (95, 280)
    screen.blit(textSurf, textRect2)

    scoreBox(screen, ("Player Wins:" + str(playerWins)), playerWins, serverWins, playerHand, serverHand, 400, 325)
    scoreBox(screen, ("Server Wins:" + str(serverWins)), playerWins, serverWins, playerHand, serverHand, 400, 350)
    pygame.display.flip()

    t = Thread(target=displayCards, args=(playerCard, serverCard, screen, playerWinTxt, ServerWinTxt))
    t.start()
    pygame.display.flip()


    #time.sleep(1.5)
    print("Player's card is: ", playerCard.getRank() + " of " + playerCard.getSuit())
    print("Server's card is: ", serverCard.getRank() + " of " + serverCard.getSuit(), "\r\n")


    if(response == "1"):
        playerHand.append(playerCard)
        playerHand.append(serverCard)

        count += 1
        playerWins += 1

    elif(response == "2"):
        #discard = playerHand.pop(card)
        serverHand.append(serverCard)
        serverHand.append(playerCard)

        count += 1
        serverWins += 1

    elif(response == "3"):
        print("War!")
        count +=1
        discardPile = []
        discardPile.append(playerCard)
        discardPile.append(serverCard)
        for item in range(2):
            discardPile.append(playerHand.pop(0))
            discardPile.append(serverHand.pop(0))

        playerLastCard = playerHand.pop(0)
        serverLastCard = serverHand.pop(0)
        warCards = [playerLastCard.getRankValue(), serverLastCard.getRankValue()]
        war = Thread(target=displayWar, args=(playerLastCard, serverLastCard, discardPile, screen, WarTxt))
        war.start()
        pygame.display.flip()
        # screen.fill((157, 255, 137))
        client_socket.send(str(warCards).encode())
        result = (client_socket.recv(4096)).decode()
        # discardPile.append(playerHand[card])
        # discardPile.append(serverHand[card])
        if(result == "1"):
            playerWins += 1
            for item in discardPile:
                playerHand.append(item)
            playerHand.append(playerLastCard)
            playerHand.append(serverLastCard)
                # pprint(vars(item))
        elif(result == "2"):
            serverWins += 1
            for item in discardPile:
                serverHand.append(item)
            serverHand.append(playerLastCard)
            serverHand.append(serverLastCard)
        #discardPile.clear()

    # print("Player's # of Cards: ", len(playerHand))
    # print("Server's # of Cards: ", len(serverHand))
    print("Game count: ", count)
    print('Player Wins: ', playerWins)
    print('Server Wins: ', serverWins, "\r\n")
    


def displayCards(playerCard, serverCard, screen, playerWinTxt, ServerWinTxt):
    screen.blit(playerCard.getImage(), (50,80))
    screen.blit(serverCard.getImage(), (50,300))
    pygame.display.flip()

def displayWar(playerCard, serverCard, discardPile, screen, WarTxt):
    screen.blit(discardPile[0].getImage(), (160, 80))
    screen.blit(discardPile[2].getImage(), (180, 80))
    screen.blit(discardPile[4].getImage(), (200,80))
    screen.blit(playerCard.getImage(), (220,80))
    screen.blit(discardPile[1].getImage(), (160,300))
    screen.blit(discardPile[3].getImage(), (180,300))
    screen.blit(discardPile[5].getImage(), (200,300))
    screen.blit(serverCard.getImage(), (220,300))
    pygame.display.flip()

def text_objects(text, font, black):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def displayButton(screen, black, msg,x,y,w,h,ic,ac, client_socket, playerHand, serverHand, playerWins, serverWins, count, playerWinTxt, ServerWinTxt, WarTxt):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            compareCards(client_socket, playerHand, serverHand, playerWins, serverWins, count, screen, playerWinTxt, ServerWinTxt, WarTxt)         
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("arial",60)
    textSurf, textRect = text_objects(msg, smallText, black)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def scoreBox(screen, msg, playerWins, serverWins, playerHand, serverHand, x, y):
    pygame.draw.rect(screen, pygame.Color(169, 169, 169), (x, y, 300, 25))
    font = pygame.font.SysFont("arial", 15)
    textSurf, textRect = text_objects(msg, font, pygame.Color(255,255,255))
    textRect.center = ( (x+(200/2)), (y+(25/2)) )
    screen.blit(textSurf, textRect)


def main():
    playDeck = CardDeck.cardDeck()
    shuffledPlayingDeck = random.sample(playDeck, len(playDeck))
    playerHand, serverHand = CardDeck.split_list(shuffledPlayingDeck)
    client_socket = socket.socket()
    client_socket.connect(('127.0.0.1', 8080))

    black = (0,0,0)
    ic = pygame.Color(201, 25, 65)
    ac = pygame.Color(23, 54, 125)

    pygame.init()
    # load and set the logo
    logo = pygame.image.load("cardImages/icon_full.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("War Card Game")

    # create a surface on screen that has the size of 640X480
    screen = pygame.display.set_mode((640,480))
    
    icon = pygame.image.load('cardImages/icon.png')
    green = pygame.image.load('cardImages/green.png')
    font = pygame.font.SysFont('arial', 26)
    playerWinTxt = font.render('Player Wins', 1, black)
    ServerWinTxt = font.render("Server Wins", 1, black)
    WarTxt = font.render("WAR!", 1, black)
    font = pygame.font.SysFont("arial", 15)
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
                pygame.quit()
                sys.exit()
                break # break out of the for loop


        for item in range(30):
            if (min(len(playerHand), len(serverHand)) > 0):
                #displayButton(screen, black, "Draw", 500, 240, 100, 100, ic, ac, action=compareCards)
                screen.fill((157, 255, 137))
                displayButton(screen, pygame.Color(0,0,0), "Draw!", 400, 180, 150, 75, ic, ac,client_socket, playerHand, serverHand, playerWins, serverWins, item, playerWinTxt, ServerWinTxt, WarTxt)
                time.sleep(3)
                # compareCards(client_socket, playerHand, serverHand, playerWins, serverWins, count, screen, playerWinTxt, ServerWinTxt, WarTxt)
                pygame.display.flip()
        running = False
        pygame.quit()


if __name__ == "__main__":
    main()