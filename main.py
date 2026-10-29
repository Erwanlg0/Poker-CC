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
    straight = _is_straight(ranks)
    flush = _is_flush(hand)
    combinations = {"high_card": max(ranks)}

    if max(counts.values()) >= 3:
        combinations["three_of_a_kind"] = COMBINATION_SCORES["three_of_a_kind"]
    if straight:
        combinations["straight"] = COMBINATION_SCORES["straight"]
    if flush:
        combinations["flush"] = COMBINATION_SCORES["flush"]
    if sorted(counts.values()) == [2, 3]:
        combinations["full_house"] = COMBINATION_SCORES["full_house"]
    if 4 in counts.values():
        combinations["four_of_a_kind"] = COMBINATION_SCORES["four_of_a_kind"]
    if straight and flush:
        combinations["straight_flush"] = COMBINATION_SCORES["straight_flush"]
    return combinations


def score_hand(hand: Hand) -> int:
    return max(available_combinations(hand).values())


def score_hands(hands: list[Hand]) -> int:
    return sum(score_hand(hand) for hand in hands)


def score_hands_bonus(hands: list[Hand]) -> int:
    limited_combinations = {"full_house"}
    used_combinations = set()
    total = 0
    return total

### ♥ ♠ ♦ ♣