import numpy as np
from card import *


class Player:
    def __init__(self, money: int):
        self._cards = []
        self._money = money
        self._bets = []

    def startGame(self, cards: list, bet: int):
        if not self.canPlayWithRate(bet):
            raise ValueError('Bet is more then player can use')
        self._money -= bet * 3
        self._cards = cards
        self._bets = [bet] * 3

    def canPlayWithRate(self, bet):
        return bet * 3 <= self._money

    def seeNewCard(self, newCard):
        self._cards.append(newCard)

    def pullBet(self):
        self._money += self._bets.pop()

    def getBets(self):
        return self._bets.copy()

    def getMoney(self):
        return self._money

    def addMoney(self, newMoney: int):
        self._money += newMoney

    def getCards(self):
        return self._cards.copy()

    def returnCards(self):
        returnCards = self._cards.copy()
        self._cards.clear()
        return returnCards


class LetItRideGame:
    def __init__(self, deckOfCards: list):
        self._deck = deckOfCards
        self._dealerCards = []
        self._player = None
        self._stageNum = -1

    def startGame(self, bet: int, player: Player):
        self._player = player
        np.random.shuffle(self._deck)
        self._stageNum = 0
        playerCards = []
        for i in range(3):
            playerCards.append(self.__pullCard())
        self._player.startGame(playerCards, bet)

        self._dealerCards.append(self.__pullCard())
        self._dealerCards.append(self.__pullCard())

    def nextStage(self):
        if self._stageNum == 0:
            newCard = self._dealerCards.pop(0)
            print("Show new card: {}".format(newCard))
            self._player.seeNewCard(newCard)
            self._stageNum += 1
        elif self._stageNum == 1:
            newCard = self._dealerCards.pop(0)
            print("Show new card: {}".format(newCard))
            self._player.seeNewCard(newCard)
            coefficient = self.calculateCoefficientOfPlayerByResultCards(self._player.getCards())
            print("Ended cards: {}\nCoefficient: {}".format(self._player.getCards(), coefficient))
            for card in self._player.returnCards():
                self._deck.append(card)
            self._player.addMoney(sum(self._player._bets) * coefficient)
            self._player._bets = []
            self._stageNum = -1
        else:
            raise Exception('Game has not started yet')

    def printDeck(self):
        print("Deck [{}]: {}".format(len(self._deck), self._deck))

    def __pullCard(self):
        card = self._deck[0]
        self._deck.pop(0)
        return card

    @staticmethod
    def calculateCoefficientOfPlayerByResultCards(cards: list):
        cardSuitSet = set()
        cardTypeSet = set()
        cardTypeCounter = {}
        for type in CardType:
            cardTypeCounter[type] = 0
        cardTypeCounterValues = cardTypeCounter.values()
        cardValues = sorted([card.type.value for card in cards])
        isRow = True
        for i in range(len(cardValues) - 2):
            if cardValues[i + 1] - cardValues[i] != 1:
                isRow = False
                break

        for card in cards:
            cardSuitSet.add(card.suit)
            cardTypeSet.add(card.type)
            cardTypeCounter[card.type] += 1

        # Royal Flush
        if isRow and len(cardSuitSet) == 1 and CardType.ACE in cardTypeSet:
            return 1000

        # Straight-Flush
        if isRow and len(cardSuitSet) == 1:
            return 200

        # Four of a kind
        if 4 in cardTypeCounterValues or 5 in cardTypeCounterValues:
            return 50

        # Full house
        if 3 in cardTypeCounterValues and 2 in cardTypeCounterValues:
            return 11

        # Flush
        if len(cardSuitSet) == 1:
            return 8

        # Straight
        if isRow:
            return 5

        # Three of a kind
        if 3 in cardTypeCounterValues:
            return 3

        # Two pair
        if sorted(cardTypeCounterValues) == [1, 2, 2]:
            return 2

        # Pair
        if 2 in cardTypeCounterValues:
            return 1

        return 0
