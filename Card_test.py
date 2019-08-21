import unittest
from Card import Card


class TestCard(unittest.TestCase):
    def test_init_with_number_input(self):
        card = Card(5) # 3c
        self.assertEqual(card.get_card_number(), 5)

    def test_init_with_string_input(self):
        card = Card('3c') # 3c
        self.assertEqual(card.get_card_number(), 5)

    def test_9_diamond(self):
        card = Card('9d')
        self.assertEqual(card.cardNumber, 28)
        self.assertEqual(card.get_suit(), 'd')
        self.assertEqual(card.get_rank(), '9')
        self.assertEqual(card.get_rank_value(), 9)
        
    def test_2_diamond(self):
        card = Card(0)
        self.assertEqual(card.get_suit(), 'd')
        self.assertEqual(card.get_rank(), '2')
        self.assertEqual(card.get_rank_value(), 2)
        self.assertEqual(card.cardNumber, 0)

    def test_5_club(self):
        card = Card('5c')
        self.assertEqual(card.cardNumber, 13)
        self.assertEqual(card.get_suit(), 'c')
        self.assertEqual(card.get_rank(), '5')
        self.assertEqual(card.get_rank_value(), 5)
        
    def test_a_spade(self):
        card = Card('As')
        self.assertEqual(card.get_suit(), 's')
        self.assertEqual(card.get_rank(), 'A')
        self.assertEqual(card.get_rank_value(), 14)
        self.assertEqual(card.cardNumber, 51)

    def test_k_heart(self):
        card = Card('Kh')
        self.assertEqual(card.get_suit(), 'h')
        self.assertEqual(card.get_rank(), 'K')
        self.assertEqual(card.get_rank_value(), 13)
        self.assertEqual(card.cardNumber, 46)

    def test_card_equality(self):
        card = Card('kh')
        card2 = Card('kh')
        self.assertTrue(card == card2)

if __name__ == '__main__':
    unittest.main()
