from poker import Card, PokerHand

# test high card rank
hand = PokerHand('3D JC 8S 4H 2C')
assert hand.rank == 'High Card', hand.rank

hand = PokerHand('AS TC 2H 3H 8D')
assert hand.rank == 'High Card', hand.rank

hand = PokerHand('2H 3D 7D 9S TS')
assert hand.rank == 'High Card', hand.rank

hand = PokerHand('TS QH 3D 5D 6D')
assert hand.rank == 'High Card', hand.rank

# test pair rank
hand = PokerHand('AH AD 8C 4S 7H')
assert hand.rank == 'Pair', hand.rank

hand = PokerHand('2H 3H 5H 7D 2C')
assert hand.rank == 'Pair', hand.rank

hand = PokerHand('9S TC 2S 8C 8S')
assert hand.rank == 'Pair', hand.rank

hand = PokerHand('AC QH 3D 5D 3H')
assert hand.rank == 'Pair', hand.rank

# test two pair rank
hand = PokerHand('4C 4S 3C 3D QC')
assert hand.rank == 'Two Pair', hand.rank

hand = PokerHand('2H 3H 2D 3S AS')
assert hand.rank == 'Two Pair', hand.rank

hand = PokerHand('TS QS KD QD TC')
assert hand.rank == 'Two Pair', hand.rank

hand = PokerHand('8D 7H 7C 8C AC')
assert hand.rank == 'Two Pair', hand.rank

# test three of a kind rank
hand = PokerHand('7C 7D 7S KC 3D')
assert hand.rank == 'Three of a Kind', hand.rank

hand = PokerHand('AD AH 2D 3C AC')
assert hand.rank == 'Three of a Kind', hand.rank

hand = PokerHand('KH QS QC 8C QD')
assert hand.rank == 'Three of a Kind', hand.rank

hand = PokerHand('2D 3D 2H 2C 5S')
assert hand.rank == 'Three of a Kind', hand.rank

# test straight rank
hand = PokerHand('9C 8D 7S 6D 5H')
assert hand.rank == 'Straight', hand.rank

hand = PokerHand('AS 2S 3D 4H 5C')
assert hand.rank == 'Straight', hand.rank

hand = PokerHand('TC JH QD KD AD')
assert hand.rank == 'Straight', hand.rank

hand = PokerHand('3C 5H 4D 7D 6C')
assert hand.rank == 'Straight', hand.rank

# test flush rank
hand = PokerHand('4C JC 8C 2C 9C')
assert hand.rank == 'Flush', hand.rank

hand = PokerHand('2D 5D 7D QD KD')
assert hand.rank == 'Flush', hand.rank

hand = PokerHand('8H 6H 7H KH AH')
assert hand.rank == 'Flush', hand.rank

hand = PokerHand('TS AS 2S 5S 8S')
assert hand.rank == 'Flush', hand.rank

# test full house rank
hand = PokerHand('TH TD TS 9C 9D')
assert hand.rank == 'Full House', hand.rank

hand = PokerHand('2D 2S 2C 3C 3H')
assert hand.rank == 'Full House', hand.rank

hand = PokerHand('KC QC KD KH QH QD')
assert hand.rank == 'Full House', hand.rank

hand = PokerHand('AH 5C 5D 5S AS')
assert hand.rank == 'Full House', hand.rank

# test four of a kind rank
hand = PokerHand('JH JD JS JC 7D')
assert hand.rank == 'Four of a Kind', hand.rank

hand = PokerHand('KD KH KS 2S KC')
assert hand.rank == 'Four of a Kind', hand.rank

hand = PokerHand('2D 3H 3C 3S 3D')
assert hand.rank == 'Four of a Kind', hand.rank

hand = PokerHand('9H 9C AC 9S 9D')
assert hand.rank == 'Four of a Kind', hand.rank

# test straight flush rank
hand = PokerHand('8C 7C 6C 5C 4C')
assert hand.rank == 'Straight Flush', hand.rank

hand = PokerHand('AD 2D 3D 4D 5D')
assert hand.rank == 'Straight Flush', hand.rank

hand = PokerHand('2S 3S 4S 5S 6S')
assert hand.rank == 'Straight Flush', hand.rank

hand = PokerHand('3H 4H 5H 6H 7H')
assert hand.rank == 'Straight Flush', hand.rank

# test royal flush rank
hand = PokerHand('AD KD QD JD TD')
assert hand.rank == 'Royal Flush', hand.rank

hand = PokerHand('KC JC AC TC QC')
assert hand.rank == 'Royal Flush', hand.rank

hand = PokerHand('TH QH AH JH KH')
assert hand.rank == 'Royal Flush', hand.rank

hand = PokerHand('QS TS KS JS AS')
assert hand.rank == 'Royal Flush', hand.rank

# keep this at the end - it will only show if all your tests pass
print('Tests passing!')