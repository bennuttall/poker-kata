from poker import Card, PokerHand

# test high card rank test high card rank
hand_1 = PokerHand('3D JC 8S 4H 2C')
assert hand_1.rank == 'High Card', hand_1.rank

hand_1 = PokerHand('A')
assert hand_1.rank == 'High Card', hand_1.rank

# keep this at the end - it will only show if all your tests pass
print('Tests passing!')
