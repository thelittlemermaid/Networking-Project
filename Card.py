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

def compareCards(client_socket, playerHand, serverHand, screen):
    global playerWins
    global serverWins
    global count
    count += 1
    font = pygame.font.SysFont("arial", 15)
    print("Player's # of Cards: ", len(playerHand))
    print("Server's # of Cards: ", len(serverHand))
    print("\r\n")
    scoreBox(screen, ("Player Wins:" + str(playerWins)), playerWins, serverWins, playerHand, serverHand, 400, 325)
    scoreBox(screen, ("Server Wins:" + str(serverWins)), playerWins, serverWins, playerHand, serverHand, 400, 350)

    scoreBox(screen, ("# of Player Cards:" + str(len(playerHand))), playerWins, serverWins, playerHand, serverHand, 400, 400)
    scoreBox(screen, ("# of Server Cards:" + str(len(serverHand))), playerWins, serverWins, playerHand, serverHand, 400, 425)
    playerCard = playerHand.pop(0)
    serverCard = serverHand.pop(0)
    cards = [playerCard.getRankValue(), serverCard.getRankValue()]
    client_socket.send(str(cards).encode())
    response = (client_socket.recv(4096)).decode()


    t = Thread(target=displayCards, args=(playerCard, serverCard, screen))
    t.start()
    pygame.display.flip()

    print("Player's card is: ", playerCard.getRank() + " of " + playerCard.getSuit())
    print("Server's card is: ", serverCard.getRank() + " of " + serverCard.getSuit(), "\r\n")


    if(response == "1"):
        playerHand.append(playerCard)
        playerHand.append(serverCard)

        playerWins += 1

    elif(response == "2"):
        serverHand.append(serverCard)
        serverHand.append(playerCard)

        serverWins += 1

    elif(response == "3"):
        print("War!")
        discardPile = []
        discardPile.append(playerCard)
        discardPile.append(serverCard)
        for item in range(2):
            discardPile.append(playerHand.pop(0))
            discardPile.append(serverHand.pop(0))

        playerLastCard = playerHand.pop(0)
        serverLastCard = serverHand.pop(0)
        warCards = [playerLastCard.getRankValue(), serverLastCard.getRankValue()]
        war = Thread(target=displayWar, args=(playerLastCard, serverLastCard, discardPile, screen))
        war.start()
        pygame.display.flip()
        client_socket.send(str(warCards).encode())
        result = (client_socket.recv(4096)).decode()

        if(result == "1"):
            playerWins += 1
            for item in discardPile:
                playerHand.append(item)
            playerHand.append(playerLastCard)
            playerHand.append(serverLastCard)
        elif(result == "2"):
            serverWins += 1
            for item in discardPile:
                serverHand.append(item)
            serverHand.append(playerLastCard)
            serverHand.append(serverLastCard)
        elif(result == "3"):
            print("War!")
            discardPile = []
            discardPile.append(playerCard)
            discardPile.append(serverCard)
            for item in range(2):
                discardPile.append(playerHand.pop(0))
                discardPile.append(serverHand.pop(0))

            playerLastCard = playerHand.pop(0)
            serverLastCard = serverHand.pop(0)
            warCards = [playerLastCard.getRankValue(), serverLastCard.getRankValue()]
            war = Thread(target=displayWar, args=(playerLastCard, serverLastCard, discardPile, screen))
            war.start()
            pygame.display.flip()
            client_socket.send(str(warCards).encode())
            result = (client_socket.recv(4096)).decode()

    scoreBox(screen, ("Player Wins:" + str(playerWins)), playerWins, serverWins, playerHand, serverHand, 400, 325)
    scoreBox(screen, ("Server Wins:" + str(serverWins)), playerWins, serverWins, playerHand, serverHand, 400, 350)

    print("Game count: ", count)
    print('Player Wins: ', playerWins)
    print('Server Wins: ', serverWins, "\r\n")
    


def displayCards(playerCard, serverCard, screen):
    screen.blit(playerCard.getImage(), (50,80))
    screen.blit(serverCard.getImage(), (50,300))
    pygame.display.flip()

def displayWar(playerCard, serverCard, discardPile, screen):
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

def displayButton(screen, black, msg,x,y,w,h,ic,ac, client_socket, playerHand, serverHand):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            compareCards(client_socket, playerHand, serverHand, screen)         
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("arial",60)
    textSurf, textRect = text_objects(msg, smallText, black)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def startButton(screen):
    pygame.draw.rect(screen, pygame.Color(0, 255, 0), (400, 180, 150, 75))
    smallText = pygame.font.SysFont("arial",60)
    textSurf, textRect = text_objects('Play', smallText, pygame.Color(0,0,0))
    textRect.center = ( (400+(150/2)), (180+(75/2)) )
    screen.blit(textSurf, textRect)

def scoreBox(screen, msg, playerWins, serverWins, playerHand, serverHand, x, y):
    pygame.draw.rect(screen, pygame.Color(169, 169, 169), (x, y, 300, 25))
    font = pygame.font.SysFont("arial", 15)
    textSurf, textRect = text_objects(msg, font, pygame.Color(255,255,255))
    textRect.center = ( (x+(200/2)), (y+(25/2)) )
    screen.blit(textSurf, textRect)

def gameLoop(playerHand, serverHand, screen, ic, ac, client_socket, font, largeFont, black):
    global count
    global serverWins
    global playerWins
    while count <= 30:
        if (min(len(playerHand), len(serverHand)) > 0):
            screen.fill((157, 255, 137))
            displayButton(screen, pygame.Color(0,0,0), "Draw!", 400, 180, 150, 75, ic, ac,client_socket, playerHand, serverHand)
            textSurf, textRect = text_objects("Client:", font, black)
            textRect.center = (95, 60)
            screen.blit(textSurf, textRect)
            textSurf, textRect2 = text_objects("Server:", font, black)
            textRect2.center = (95, 280)
            screen.blit(textSurf, textRect2)
            pygame.display.flip()
            time.sleep(5)
    screen.fill((157, 255, 137))
    if playerWins > serverWins:
        textSurf, textRect = text_objects('Player Wins', largeFont, black)
        textRect.center = ( (250+(150/2)), (200+(100/2)) )
        screen.blit(textSurf, textRect)
    elif serverWins > playerWins:
        textSurf, textRect = text_objects('Server Wins', largeFont, black)
        textRect.center = ( (250+(150/2)), (200+(100/2)) )
        screen.blit(textSurf, textRect)
    elif serverWins == playerWins:
        textSurf, textRect = text_objects('TIE!', largeFont, black)
        textRect.center = ( (250+(150/2)), (200+(100/2)) )
        screen.blit(textSurf, textRect)
    pygame.display.flip()
    time.sleep(5)
    running = False

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
    largeFont = pygame.font.SysFont('arial', 75)
    font = pygame.font.SysFont("arial", 15)
    screen.blit(green, (0,0))

    # define a variable to control the main loop
    running = True
    startButton(screen)
    pygame.display.flip()

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:#550 > pygame.mouse.get_pos()[0] > 400 and 255 > pygame.mouse.get_pos()[0] > 180:
                gameLoop(playerHand, serverHand, screen, ic, ac, client_socket, font, largeFont, black)
                # game = Thread(target = gameLoop, args = (playerHand, serverHand, screen, ic, ac, client_socket, font, largeFont, black))
                # game.start()
            elif event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
                break # break out of the for loop


if __name__ == "__main__":
    main()