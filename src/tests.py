#!/usr/bin/env python3
from poker import Card, PokerHand, create_deck, deal_hand

# some useful card suit/value constants
T = 'T'
J = 'J'
Q = 'Q'
K = 'K'
A = 'A'
H = 'H'
D = 'D'
S = 'S'
C = 'C'
# you can use integers for the others (but not 10 - use T)

# some useful test helper-functions
def compare_things(thing_1, op, thing_2):
    assert op in ('<', '=', '>')
    assert type(thing_1) == type(thing_2)
    if op == '<':
        assert thing_1 < thing_2
        assert not thing_1 > thing_2
        assert not thing_1 == thing_2
        assert thing_1 != thing_2
    elif op == '=':
        assert thing_1 == thing_2
        assert not thing_1 != thing_2
        assert not thing_1 < thing_2
        assert not thing_1 > thing_2
    elif op == '>':
        assert thing_1 > thing_2
        assert not thing_1 < thing_2
        assert not thing_1 == thing_2
        assert thing_1 != thing_2

def create_hand(hand_str):
    return PokerHand([Card(card_str[0], card_str[1]) for card_str in hand_str.split()])

def compare_hands(hand_str1, op, hand_str2):
    compare_things(create_hand(hand_str1), op, create_hand(hand_str2))

# test single card
card_1 = Card(A, S)
card_2 = Card(A, D)
compare_things(card_1, '=', card_2)
card_3 = Card(K, S)
compare_things(card_1, '>', card_3)
compare_things(card_2, '>', card_3)

# test comparing two poker hands
compare_hands('AS 2D 4C 7H KS', '=', 'AC 3D 5C 8H TS')

compare_hands('AS 2D 4C 7H KS', '>', 'QS 3D 5C 8H TS')

# test creating a deck
deck = create_deck()
assert len(deck) == 52
assert all(isinstance(card, Card) for card in deck)

# test creating a hand from the deck
cards = deal_hand(5, deck)
hand_1 = PokerHand(cards)
cards = deal_hand(5, deck)
hand_2 = PokerHand(cards)
