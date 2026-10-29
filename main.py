Card = tuple[int, str]
Hand = list[Card]



def score_hand(hand: Hand) -> int:
    return max(rank for rank, suit in hand)











### ♥ ♠ ♦ ♣