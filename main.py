from collections import Counter


Card = tuple[int, str]
Hand = list[Card]



def score_hand(hand: Hand) -> int:
    ranks = [rank for rank, suit in hand]
    counts = Counter(ranks)
    straight = len(counts) == 5 and max(ranks) - min(ranks) == 4
    if straight:
        return 40
    if max(counts.values()) >= 3:
        return 30
    return max(ranks)






### ♥ ♠ ♦ ♣