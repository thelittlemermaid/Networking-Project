import sys
import socket
import pygame
import random
from threading import Thread
import time


#   Global Variables:
playerWins = 0
serverWins = 0
count = 0


#   Card class:
#   Each card contains a Rank (2-10, J,Q,K,A ), RankValue (0-12), Suit (Q,D,S,H), & Image
#   This class also contains getters to pull each attribute out in our Main
class Card:
    def __init__(self, rank, rankValue, suits, image, *args, **kwargs):
        self._rank = rank
        self._rankValue = rankValue
        self._suits = suits
        self._image = image

    def getImage(self):
        return self._image

    def getRank(self):
        return self._rank

    def getSuit(self):
        return self._suits

    def getRankValue(self):
        return self._rankValue


#   CardDeck Class that is comprised of 52 Card objects
#   Each card is developed through two For loops, the outer for loop for the Suits
#   And the inner for loop for the ranks. When Each card is created it is also assigned
#   an Image that is in our source folder. Each card image can be found in the cardImages Folder

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

#   This method calls for a list (our Deck) and will 
#   split the deck evenly depending on the number of cards

    def split_list(a_list):
        half = len(a_list)//2
        return a_list[:half], a_list[half:]

#   This method passes in a socket, the two hands, and the screen which is
#   our game window for it to be updated each round. 

def compareCards(client_socket, playerHand, serverHand, screen):
    global playerWins
    global serverWins
    global count
    count += 1

#   To Print out how many cards each hand has in the terminal
    print("Player's # of Cards: ", len(playerHand))
    print("Server's # of Cards: ", len(serverHand))
    print("\r\n")

#   This updates every round the total number of wins the Client / Server has in our GUI
    scoreBox(screen, ("Player Wins:" + str(playerWins)), 400, 325)
    scoreBox(screen, ("Server Wins:" + str(serverWins)), 400, 350)

#   This updates the total number of cards in the Scorebox on the GUI (Bottom Right Corner)
    scoreBox(screen, ("# of Player Cards:" + str(len(playerHand))), 400, 400)
    scoreBox(screen, ("# of Server Cards:" + str(len(serverHand))), 400, 425)

#   Pops off the top card out of each hand
    playerCard = playerHand.pop(0)
    serverCard = serverHand.pop(0)

#   Thread to Start our Display Cards Method, skip to line 223 to see this method 
    t = Thread(target=displayCards, args=(playerCard, serverCard, screen))
    t.start()
    pygame.display.flip()

#   Putting the rankValues from the popped off cards and storing them into an array
#   Once they're stored, they are sent to the Server for further comparisons
#   Client will wait for the response before further actions
    cards = [playerCard.getRankValue(), serverCard.getRankValue()]
    client_socket.send(str(cards).encode())
    response = (client_socket.recv(4096)).decode()

#   Printing out the Cards to make sure that the game is working correctly in the Terminal
    print("Player's card is: ", playerCard.getRank() + " of " + playerCard.getSuit())
    print("Server's card is: ", serverCard.getRank() + " of " + serverCard.getSuit(), "\r\n")

#   Next Steps in our game. Once the server compares the two values that it receives, it will
#   send back a 1, 2, or 3. A 1 means that the Server lost and the Player will receive the cards
#   for that round. A 2 means that the Client lost and the Server will receive the cards. A 3 means
#   that a War happened and the Client will prepare the GUI for more cards, and send the server
#   two more cards for further comparisons. 

    # Player Wins
    if response == "1":
        playerHand.append(playerCard)
        playerHand.append(serverCard)

        playerWins += 1

    # Server Wins
    elif response == "2":
        serverHand.append(serverCard)
        serverHand.append(playerCard)

        serverWins += 1


    # War
    elif response == "3":
        print("War!")
#   Discard Pile is for the cards from the Client and Server to be placed in.
#   These cards will be used in our GUI so the Client can see the War happening.
        discardPile = []
        discardPile.append(playerCard)
        discardPile.append(serverCard)

#   We decided to pop off three cards from each hand and have the 
#   comparisons come from the third card.

        for item in range(2):
            discardPile.append(playerHand.pop(0))
            discardPile.append(serverHand.pop(0))

        playerLastCard = playerHand.pop(0)
        serverLastCard = serverHand.pop(0)

#   Thread to display the War happening in the GUI 
        warCards = [playerLastCard.getRankValue(), serverLastCard.getRankValue()]
        war = Thread(target=displayWar, args=(playerLastCard, serverLastCard, discardPile, screen))
        war.start()
        pygame.display.flip()

#   Client will send back two more cards for further comparisons. It will wait for the 
#   Server to send back a response like above. 
        client_socket.send(str(warCards).encode())
        result = (client_socket.recv(4096)).decode()


#   If Player wins War, all cards will be appended to the back of the Player's Hand
        if result == "1":
            playerWins += 1
            for item in discardPile:
                playerHand.append(item)
            playerHand.append(playerLastCard)
            playerHand.append(serverLastCard)

#   If Server wins War, all cards will be appended to the back of the Server's hand. 
        elif result == "2":
            serverWins += 1
            for item in discardPile:
                serverHand.append(item)
            serverHand.append(playerLastCard)
            serverHand.append(serverLastCard)

#   If second War happens it will rinse and repeat with putting more cards into a discardPile
#   and sending the cards back to server for further comparisons like above. 
        elif result == "3":
            print("War!")
            discardPile2 = []
            discardPile2.append(playerCard)
            discardPile2.append(serverCard)
            for item in range(2):
                discardPile2.append(playerHand.pop(0))
                discardPile2.append(serverHand.pop(0))          
            playerLastCard = playerHand.pop(0)
            serverLastCard = serverHand.pop(0)
            warCards = [playerLastCard.getRankValue(), serverLastCard.getRankValue()]
            war = Thread(target=displayWar, args=(playerLastCard, serverLastCard, discardPile, screen))
            war.start()
            pygame.display.flip()
            client_socket.send(str(warCards).encode())
            result = (client_socket.recv(4096)).decode()

            if result == "1":
                playerWins += 1
                for item in discardPile2:
                    playerHand.append(discardPile[item])
                    playerHand.append(item)
                playerHand.append(playerLastCard)
                playerHand.append(serverLastCard)
            elif result == "2":
                serverWins += 1
                for item in discardPile2:
                    serverHand.append(discardPile[item])
                    serverHand.append(item)
                serverHand.append(playerLastCard)
                serverHand.append(serverLastCard)

#   Updates the Player / Server wins after every round.     

    scoreBox(screen, ("Player Wins:" + str(playerWins)), 400, 325)
    scoreBox(screen, ("Server Wins:" + str(serverWins)), 400, 350)

#   Prints to Terminal PlayerWins, ServerWins, and Game count
#   Mainly for testing purposes and to check if everything is correct

    print("Game count: ", count)
    print('Player Wins: ', playerWins)
    print('Server Wins: ', serverWins, "\r\n")

#   Method to display the two cards that are popped off in the beginning of CompareCards
#   on lines 87 & 88. This method gets called in the Thread in Compare Cards every round.

def displayCards(playerCard, serverCard, screen):
    screen.blit(playerCard.getImage(), (50,80))
    screen.blit(serverCard.getImage(), (50,300))
    pygame.display.flip()

#   This method is used if a war takes place, and will display the cards on the GUI
#   It will have a pile of four cards for Client and Server and will have them in 
#   order that they are discarded in the discardPile.

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

#   This method generates the text that will be displayed on our GUI screen

def text_objects(text, font, black):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

#   This creates our "Draw!" button

def displayButton(screen, black, msg,x,y,w,h,ic,ac, client_socket, playerHand, serverHand):
#   Uses the pygame event collector to collect metrics regarding the user's mouse position on the GUI screen.
    mouse = pygame.mouse.get_pos()

#   If the user's mouse is within the boundaries of the box drawn, the color of the box changes.
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
#   Checks the event collecter to respond when the user interacts with the GUI.
    for event in pygame.event.get():
#   If the user clicks the "x", the game closes.
        if event.type == pygame.QUIT:
            sys.exit()
#   If the user clicks the "Draw!" button, the compareCards method on line 67 is called.
        if event.type == pygame.MOUSEBUTTONDOWN:
            compareCards(client_socket, playerHand, serverHand, screen)         
#   Otherwise, if none of the above conditions are met, the normal button is drawn.
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("arial",60)
    textSurf, textRect = text_objects(msg, smallText, black)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(textSurf, textRect)


#   Start Button to be displayed before the game starts any comparing or anything
#   This method is called in main, in our main loop to help start the game
#   We implemented this to be able to have all events inside our main loop

def startButton(screen):
    pygame.draw.rect(screen, pygame.Color(0, 255, 0), (400, 180, 150, 75))
    smallText = pygame.font.SysFont("arial",60)
    textSurf, textRect = text_objects('Play', smallText, pygame.Color(0,0,0))
    textRect.center = ( (400+(150/2)), (180+(75/2)) )
    screen.blit(textSurf, textRect)

#   This ScoreBox will display during each round and will contain, the number of wins
#   for both the Client and the Server, and the amount of cards that each player
#   has in their hand. 

def scoreBox(screen, msg, x, y):
    pygame.draw.rect(screen, pygame.Color(169, 169, 169), (x, y, 300, 25))
    font = pygame.font.SysFont("arial", 15)
    textSurf, textRect = text_objects(msg, font, pygame.Color(255,255,255))
    textRect.center = ( (x+(200/2)), (y+(25/2)) )
    screen.blit(textSurf, textRect)


#   This is our main game loop.
#   This method calls all of the necessary methods for a round to be played.
#   At the end of a game, this method will also determine the winner (based on number of cards held) and display it to the screen.


def gameLoop(playerHand, serverHand, screen, ic, ac, client_socket, font, largeFont, black):
    global count
    global serverWins
    global playerWins
    while count < 30:
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
            time.sleep(1.75)
    screen.fill((157, 255, 137))
    if len(playerHand) > len(serverHand):
        textSurf, textRect = text_objects('Player Wins', largeFont, black)
        textRect.center = ( (250+(150/2)), (200+(100/2)) )
        screen.blit(textSurf, textRect)
    elif len(serverHand) > len(playerHand):
        textSurf, textRect = text_objects('Server Wins', largeFont, black)
        textRect.center = ( (250+(150/2)), (200+(100/2)) )
        screen.blit(textSurf, textRect)
    elif len(serverHand) == len(playerHand):
        textSurf, textRect = text_objects('TIE!', largeFont, black)
        textRect.center = ( (250+(150/2)), (200+(100/2)) )
        screen.blit(textSurf, textRect)
    pygame.display.flip()


#   This is our main. It contains mainly how the game is controlled. First we begin by creating
#   the deck that is getting played with. Next we will shuffle the deck by using the random
#   library and then splitting the deck by the split method that we created in our CardDeck class.
#   Once the deck is created we create our Client Socket, and assign it an IP that is passed in by the
#   terminal.

#   Next we begin by starting up our GUI window and setting its size, icon, and background color. 
#   Once these are all set we begin by displaying our start button and going into our main loop.
#   The main loop will wait for an Event to take place, either clicking on the start button or 
#   clicking on the exit button. If the Start button is clicked, then the scoreBox, and Compare Button
#   will pop up and will allow the user to click on the Compare Button until round 30 has came or 
#   either user is out of cards. The exit button can be clicked at any time during the game and 
#   will allow the game to be stopped until the user decides to run both scripts again. 

def main():
#   Assigns IP from user input in the terminal
    ipAddress = sys.argv[1]
#   Main deck is created
    playDeck = CardDeck.cardDeck()
#   Shuffling main deck
    shuffledPlayingDeck = random.sample(playDeck, len(playDeck))
#   Splitting the shuffled main deck by player and Server
    playerHand, serverHand = CardDeck.split_list(shuffledPlayingDeck)
#   Creating Client Socket
    client_socket = socket.socket()
#   Assigning Client Socket an IP and Port
    client_socket.connect((ipAddress, 8080))

    black = (0,0,0)
    ic = pygame.Color(201, 25, 65)
    ac = pygame.Color(23, 54, 125)

#   Initalizing the screen
    pygame.init()
#   Load and set the logo
    logo = pygame.image.load("cardImages/icon_full.png")
    pygame.display.set_icon(logo)
#   Set Window Caption
    pygame.display.set_caption("War Card Game")

#   Create a surface on screen that has the size of 640X480
    screen = pygame.display.set_mode((640,480))
    
#   Load in background color
    green = pygame.image.load('cardImages/green.png')
#   Set Game Font
    largeFont = pygame.font.SysFont('arial', 75)
    font = pygame.font.SysFont("arial", 15)
    screen.blit(green, (0,0))

    # define a variable to control the main loop
    running = True
#   Display Start Button
    startButton(screen)
    pygame.display.flip()

    # main loop
    while running:
        # event handling, gets all events from the event queue
        for event in pygame.event.get():
            # if the user clicks the "Start" button, the gameLoop method on line 304 is triggered
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                gameLoop(playerHand, serverHand, screen, ic, ac, client_socket, font, largeFont, black)
            # if the user clicks the "x", the game closes
            elif event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please use the command: python Card.py [server IP Address] to run this script.")
    else:
        main()