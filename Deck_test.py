import unittest
from Card import Card
from Deck import Deck


class TestDeck(unittest.TestCase):
    def test_init_with_deck(self):
        deck = Deck()
        # self.assertEqual(card.get_card_number(), 5)
        result = str(Deck)

    def test_deal_top_card(self):
        deck = Deck()
        nextCard = deck.deal()
        

if __name__ == '__main__':
    unittest.main()
