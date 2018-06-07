from poker import PokerHand, VALUES, SUITS
from itertools import product, combinations
import json

deck = ['{}{}'.format(v, s) for v, s in product(VALUES, SUITS)]

def sort_cards_string(card_string):
    cards = card_string.split(' ')
    return ' '.join(sorted(cards))

hand_ranks = {
    sort_cards_string(' '.join(c)): PokerHand(' '.join(c)).rank
    for c in combinations(deck, 5)
}

with open('hand_ranks.json', 'w') as f:
    json.dump(hand_ranks, f)
