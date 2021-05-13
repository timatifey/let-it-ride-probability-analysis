from enum import Enum


class CardSuit(Enum):
    # if value % 2 == 0 -> красная else черная
    HEARTS = 0  # Черви
    PIKES = 1  # Пики
    TILES = 2  # Бубны
    CLOVERS = 3  # Трефы


class CardType(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11  # Валет
    QUEEN = 12  # Дама
    KING = 13  # Король
    ACE = 14  # Туз


class Card:
    def __init__(self, suit: CardSuit, type: CardType):
        self.suit: CardSuit = suit
        self.type: CardType = type

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.suit == other.suit and self.type == other.type

    def __str__(self):
        return "Card<{} {}>".format(self.suit.name, self.type.name)

    def __repr__(self):
        return "Card<{} {}>".format(self.suit.name, self.type.name)


def initDeckCardList():
    deckCards: list = []
    for suit in CardSuit:
        for cardType in CardType:
            deckCards.append(Card(suit, cardType))
    return deckCards
