import unittest
from Card import Card


class TestCard(unittest.TestCase):

    def test_2_diamond(self):
        card = Card(0)
        self.assertEqual(card.get_suit(), 'd')
        self.assertEqual(card.get_rank(), '2')
        self.assertEqual(card.get_rank_value(), 2)
