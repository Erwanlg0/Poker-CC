from collections import Counter


Card = tuple[int, str]
Hand = list[Card]



def score_hand(hand: Hand) -> int:
    ranks = [rank for rank, suit in hand]
    counts = Counter(ranks)
    if max(counts.values()) >= 3:
        return 30
    return max(ranks)






### ♥ ♠ ♦ ♣