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


    def test_jack_high(self):
        hand = [(2, "♥"), (4, "♠"), (6, "♦"), (9, "♣"), (11, "♠")]
        self.assertEqual(score_hand(hand), 11)

if __name__ == "__main__":
    unittest.main()







### ♥ ♠ ♦ ♣