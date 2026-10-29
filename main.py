Card = tuple[int, str]
Hand = list[Card]



def score_hand(hand: Hand) -> int:
    ranks = [rank for rank, suit in hand]
    if 14 in ranks:
        return 14
    return 0











### ♥ ♠ ♦ ♣