from collections import Counter


Card = tuple[int, str]
Hand = list[Card]
CombinationScores = dict[str, int]

COMBINATION_SCORES = {
    "high_card": 0,
    "three_of_a_kind": 30,
    "straight": 40,
    "flush": 45,
    "full_house": 50,
    "four_of_a_kind": 60,
    "straight_flush": 80,
}

def _is_straight(ranks: list[int]) -> bool:
    return len(set(ranks)) == 5 and max(ranks) - min(ranks) == 4


def _is_flush(hand: Hand) -> bool:
    return len({suit for _, suit in hand}) == 1


def available_combinations(hand: Hand) -> CombinationScores:
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


def score_hand(hand: Hand) -> int:
    return max(available_combinations(hand).values())


def score_hands(hands: list[Hand]) -> int:
    return sum(score_hand(hand) for hand in hands)


### ♥ ♠ ♦ ♣