from poker import PokerHand

# test high card rank
hand = PokerHand('3D JC 8S 4H 2C')
assert hand.rank == 'High Card', hand.rank

# keep this at the end - it will only show if all your tests pass
print('Tests passing!')
