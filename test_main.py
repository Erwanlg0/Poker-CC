import unittest

from main import score_hand


class TestHandScoring(unittest.TestCase):
    def test_ace_high(self):
        hand = [(2, "♥"), (4, "♠"), (6, "♦"), (9, "♣"), (14, "♠")]
        self.assertEqual(score_hand(hand), 14)

    def test_king_high(self):
        hand = [(2, "♥"), (4, "♠"), (6, "♦"), (9, "♣"), (13, "♠")]
        self.assertEqual(score_hand(hand), 13)

    def test_queen_high(self):
        hand = [(2, "♥"), (4, "♠"), (6, "♦"), (9, "♣"), (12, "♠")]
        self.assertEqual(score_hand(hand), 12)

    def test_three_of_a_kind(self):
        hand = [(2, "♥"), (2, "♠"), (2, "♦"), (9, "♣"), (13, "♠")]
        self.assertEqual(score_hand(hand), 30)

    def test_straight(self):
        hand = [(5, "♣"), (6, "♦"), (7, "♥"), (8, "♠"), (9, "♣")]
        self.assertEqual(score_hand(hand), 40)

    def test_flush(self):
        hand = [(2, "♥"), (7, "♥"), (9, "♥"), (11, "♥"), (13, "♥")]
        self.assertEqual(score_hand(hand), 45)

    def test_full_house(self):
        hand = [(2, "♥"), (2, "♠"), (2, "♦"), (9, "♣"), (9, "♠")]
        self.assertEqual(score_hand(hand), 50)

    def test_four_of_a_kind(self):
        hand = [(2, "♥"), (2, "♠"), (2, "♦"), (2, "♣"), (13, "♠")]
        self.assertEqual(score_hand(hand), 60)

    def test_straight_flush(self):
        hand = [(5, "♥"), (6, "♥"), (7, "♥"), (8, "♥"), (9, "♥")]
        self.assertEqual(score_hand(hand), 80)

    def test_assignment_example(self):
        hands = [
            [(2, "♥"), (2, "♠"), (2, "♦"), (9, "♣"), (9, "♠")],
            [(5, "♣"), (6, "♦"), (7, "♥"), (8, "♠"), (9, "♣")],
            [(2, "♥"), (7, "♥"), (9, "♥"), (11, "♥"), (13, "♥")],
            [(3, "♣"), (8, "♦"), (10, "♥"), (12, "♠"), (13, "♣")],
        ]
        self.assertEqual(sum(score_hand(hand) for hand in hands), 148)


    def test_jack_high(self):
        hand = [(2, "♥"), (4, "♠"), (6, "♦"), (9, "♣"), (11, "♠")]
        self.assertEqual(score_hand(hand), 11)

    def test_ten_high(self):
        hand = [(2, "♥"), (4, "♠"), (6, "♦"), (9, "♣"), (10, "♠")]
        self.assertEqual(score_hand(hand), 10)

    def test_nine_high(self):
        hand = [(2, "♥"), (4, "♠"), (6, "♦"), (8, "♣"), (9, "♠")]
        self.assertEqual(score_hand(hand), 9)

    def test_eight_high(self):
        hand = [(2, "♥"), (4, "♠"), (6, "♦"), (7, "♣"), (8, "♠")]
        self.assertEqual(score_hand(hand), 8)

if __name__ == "__main__":
    unittest.main()







### ♥ ♠ ♦ ♣