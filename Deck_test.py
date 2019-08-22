import unittest
from Card import Card
from Deck import Deck


class TestDeck(unittest.TestCase):
    def test_init_with_deck(self):
        deck = Deck()
        result = str(Deck)

    def test_deal_top_card(self):
        deck = Deck()
        nextCard = deck.deal()
        self.assertEqual(len(deck), 51)

    def test_deal_more_than_one_card(self):
        deck = Deck()
        result = deck.deal(3)
        self.assertEqual(len(result), 3)
        self.assertEqual(len(deck), 52 - 3)

    def test_deal_specific_card(self):
        deck = Deck()
        result = deck.deal(specify_card=Card('4c'))
        self.assertEqual(result, Card('4c'))
        self.assertEqual(len(result), 51)
        self.assertFalse('4c' in str(deck))


if __name__ == '__main__':
    unittest.main()
