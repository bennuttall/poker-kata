from itertools import product
from random import shuffle

VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
SUITS = ('H', 'D', 'S', 'C')

class Card:
    def __init__(self, value, suit):
        value = str(value)
        suit = str(suit)
        if value not in VALUES:
            raise ValueError
        self.value = value
        if suit not in SUITS:
            raise ValueError
        self.suit = suit

    def __repr__(self):
        return '<Card object {}{}>'.format(self.value, self.suit)

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value_index < other.value_index

    def __gt__(self, other):
        return self.value_index > other.value_index

    @property
    def value_index(self):
        return VALUES.index(self.value)


class PokerHand:
    def __init__(self, cards):
        if any(not isinstance(card, Card) for card in cards):
            raise ValueError
        if len(cards) != 5:
            raise ValueError
        card_set = {repr(card) for card in cards}
        duplicate_cards = len(card_set) < len(cards)
        if duplicate_cards:
            raise ValueError
        self.cards = sorted(cards)

    def __repr__(self):
        return '<PokerHand object {}>'.format(', '.join(str(card) for card in self))

    def __iter__(self):
        return iter(self.cards)

    def __gt__(self, other):
        return self.cards[-1] > other.cards[-1]

    def __lt__(self, other):
        return self.cards[-1] < other.cards[-1]

    def __eq__(self, other):
        return self.cards[-1] == other.cards[-1]

def create_deck():
    cards = [Card(value, suit) for value, suit in product(VALUES, SUITS)]
    shuffle(cards)
    return cards

def deal_hand(n, deck):
    return [deck.pop() for i in range(n)]
