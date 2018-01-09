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

# test single card
card_1 = Card(A, S)
card_2 = Card(A, D)
assert card_1 == card_2
card_3 = Card(K, S)
assert card_1 != card_3
assert card_1 > card_3
assert not card_1 < card_3

# test comparing two poker hands
cards = [Card(v, s) for v, s in [(A, S), (2, D), (4, C), (7,  H), (K, S)]]
hand_1 = PokerHand(cards)
cards = [Card(v, s) for v, s in [(A, C), (3, D), (5, C), (8,  H), (T, S)]]
hand_2 = PokerHand(cards)
assert hand_1 == hand_2
assert hand_2 == hand_1

cards = [Card(v, s) for v, s in [(A, S), (2, D), (4, C), (7,  H), (K, S)]]
hand_1 = PokerHand(cards)
cards = [Card(v, s) for v, s in [(Q, S), (3, D), (5, C), (8,  H), (T, S)]]
hand_2 = PokerHand(cards)
assert hand_1 > hand_2
assert hand_2 < hand_1

# test creating a deck
deck = create_deck()
assert len(deck) == 52
assert all(isinstance(card, Card) for card in deck)

# test creating a hand from the deck
cards = deal_hand(5, deck)
hand_1 = PokerHand(cards)
cards = deal_hand(5, deck)
hand_2 = PokerHand(cards)
