VALUES = '23456789TJQKA'
SUITS = 'HDSC'

HAND_RANKS = (
    'High Card',
    'Pair',
    'Two Pair',
    'Three of a Kind',
    'Straight',
    'Flush',
    'Full House',
    'Four of a Kind',
    'Straight Flush',
    'Royal Flush'
)

class Card:
    """
    Represents a single playing card. Initialise with a two-character string in
    the form <value><suit> e.g. AS for the ace of spades:

    >>> card = Card('AS')
    """
    def __init__(self, value_suit):
        value, suit = value_suit
        if value not in VALUES:
            raise ValueError
        self.value = value
        if suit not in SUITS:
            raise ValueError
        self.suit = suit

    def __repr__(self):
        return '<Card object {}>'.format(self)

    def __str__(self):
        return '{}{}'.format(self.value, self.suit)

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
    """
    Represents a hand of five cards. Initialise with five 2-character strings
    each separated by a space, e.g:

    >>> hand = PokerHand('3D JC 8S 4H 2C')

    Evaluate the hand rank by accessing the rank property:

    >>> hand.rank
    'High Card'
    """
    def __init__(self, cards):
        cards = cards.split(' ')
        self.cards = [Card(sv) for sv in cards]
        card_set = {repr(card) for card in cards}
        duplicate_cards = len(card_set) < len(cards)
        if duplicate_cards:
            raise ValueError
        self.cards = sorted(self.cards)

    def __repr__(self):
        card_strings = (str(card) for card in self)
        return '<PokerHand object ({})>'.format(', '.join(card_strings))

    def __iter__(self):
        return iter(self.cards)

    def __gt__(self, other):
        return self.cards[-1] > other.cards[-1]

    def __lt__(self, other):
        return self.cards[-1] < other.cards[-1]

    def __eq__(self, other):
        return self.cards[-1] == other.cards[-1]

    @property
    def rank(self):
        suits = [card.suit for card in self]
        suits_set = {card.suit for card in self}
        
        values = [card.value for card in self]
        values_set = {card.value for card in self}
        value_counts = {values.count(v) for v in values}
        values_str = ''.join(values)
        
        flush = len(suits_set) == 1
        straight = values_str in VALUES or values_str == '2345A'
        royal = values_str == 'TJQKA'
        
        if flush:
            if royal:
                return 'Royal Flush'
            if straight:
                return 'Straight Flush'
            return 'Flush'
        if straight:
            return 'Straight'
        if len(values_set) == 2:
            if 4 in value_counts:
                return 'Four of a Kind'
            return 'Full House'
        if len(values_set) == 3:
            if 3 in value_counts:
                return 'Three of a Kind'
            return 'Two Pair'
        if len(values_set) == 4:
            return 'Pair'
        return 'High Card'