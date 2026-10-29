Card = tuple[int, str]
Hand = list[Card]



def score_hand(hand: Hand) -> int:
    ranks = [rank for rank, suit in hand]
    if 14 in ranks:
        return 14
    if 13 in ranks:
        return 13
    if 12 in ranks:
        return 12
    if 11 in ranks:
        return 11
    return 0











### ♥ ♠ ♦ ♣