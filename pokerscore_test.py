import unittest
from holdem_evaluator import poker_score

class TestPokerScore(unittest.TestCase):
    def test_with_one_pair(self):
        hand = '7d 8c Qs Kd 7s'.split()
        result = poker_score(hand)
        self.assertEqual(result, ((2, 1, 1, 1), (7, 13, 12, 8)))
        
    def test_with_two_pair(self):
        hand = '7d 7s Qs Kd Qd'.split()
        result = poker_score(hand)
        self.assertEqual(result, ((2, 2, 1), (12, 7, 13)))

    def test_with_royal_flush(self):
        hand = 'As Ks Qs Js Ts'.split()
        result = poker_score(hand)
        self.assertEqual(result, ((5,), (14, 13, 12, 11, 10)))

    def test_with_four_of_a_kind(self):
        hand = '6d 6s 6c 6h Ts'.split()
        result = poker_score(hand)
        self.assertEqual(result, ((4, 1), (6, 10)))

    def test_with_full_house(self):
        hand = '2d 2s 9c 9d 9h'.split()
        result = poker_score(hand)
        print(result)
        self.assertEqual(result, ((3, 2), (9, 2)))

    def test_with_flush(self):
        hand = 'Ks Js 9s 2s Ts'.split()
        result = poker_score(hand)
        self.assertEqual(result, ((3, 1, 3), (13, 11, 10, 9, 2)))
        
    def test_with_straight(self):
        hand = '4s 5h 6s 7d 8c'.split()
        result = poker_score(hand)
        self.assertEqual(result, ((3, 1, 2), (8, 7, 6, 5, 4)))

    def test_with_straight_flush(self):
        hand = '9s Ks Qs Js Ts'.split()
        result = poker_score(hand)
        self.assertEqual(result, ((5,), (13, 12, 11, 10, 9)))

    def test_with_three_of_a_kind(self):
        hand = '6d 6s 6c 8h Ts'.split()
        result = poker_score(hand)
        self.assertEqual(result, ((3, 1, 1), (6, 10, 8)))

    def test_with_high_card(self):
        hand = '2d 9s 8h Ts As'.split()
        result = poker_score(hand)
        self.assertEqual(result, ((1,), (14, 10, 9, 8, 2)))

    def test_with_straight_and_A_is_1(self):
        hand = 'As 3s 5d 4h 2s'.split()
        result = poker_score(hand)
        self.assertEqual(result, ((3, 1, 2), (5, 4, 3, 2, 1)))

    def test_with_more_than_5_cards(self):
        hand = 'As Ks Qs Js Ts 8s'.split()
        result = poker_score(hand)
        self.assertEqual(result, ((5,), (14, 13, 12, 11, 10)))

    def test_score_with_hands_of_equal_rank_flush(self):
        hand1 = 'As Ks Qs Js Td 8s'.split()
        hand2 = 'Ts Qs 2s 3s 4s'.split()
        result1 = poker_score(hand1)
        result2 = poker_score(hand2)
        self.assertTrue(result1 > result2)

    def test_score_with_hands_of_equal_rank_full_house(self):
        hand1 = '9h 9s 9c Kh Kc'.split()
        hand2 = 'Jh Jc Js 2h 2d'.split()
        result1 = poker_score(hand1)
        result2 = poker_score(hand2)
        self.assertTrue(result1 < result2)

    def test_score_with_hands_of_equal_rank_equal_score(self):
        hand1 = 'Td Qd 9d 8d 7d 4d'.split()
        hand2 = 'Ts Qs 9s 8s 7s 5s'.split()
        result1 = poker_score(hand1)
        result2 = poker_score(hand2)
        self.assertTrue(result1 == result2)
        
if __name__ == '__main__':
    unittest.main()