from collections import Counter


Card = tuple[int, str]
Hand = list[Card]



def score_hand(hand: Hand) -> int:
    ranks = [rank for rank, suit in hand]
    counts = Counter(ranks)
    straight = len(counts) == 5 and max(ranks) - min(ranks) == 4
    flush = len({suit for rank, suit in hand}) == 1
    if straight and flush:
        return 80
    if 4 in counts.values():
        return 60
    if sorted(counts.values()) == [2, 3]:
        return 50
    if flush:
        return 45
    if straight:
        return 40
    if max(counts.values()) >= 3:
        return 30
    return max(ranks)






### ♥ ♠ ♦ ♣