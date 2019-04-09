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

def main():
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.bind(('127.0.0.1', 8888))
    clientSocket.listen(2)
    while True:
        connect, serverAddress = clientSocket.accept()
        print("Connected to:", serverAddress)
        data = connect.recv(1024)
        hand = pickle.loads(data)
        print(hand)
        clientSocket.close()

if __name__ == "__main__":
    main()