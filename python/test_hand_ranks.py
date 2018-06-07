from poker import PokerHand
import json

# gunzip the file first
with open('hand_ranks.json') as f:
    hand_ranks = json.load(f)

for hand, rank in hand_ranks.items():
    assert PokerHand(hand).rank == rank
print("All tests passing!")
