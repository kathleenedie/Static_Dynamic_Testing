import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card("spades", 1)
        self.card2 = Card("clubs", 4)
        self.card3 = Card("diamonds", 5)
        self.card4 = Card("spades", 8)
        self.card5 = Card("hearts", 12)

        self.card_game = CardGame()

    def test_card_is_ace(self):
        self.assertEqual(True, self.card_game.check_for_ace(self.card1))

    def test_card_is_not_ace(self):
        self.assertEqual(False, self.card_game.check_for_ace(self.card2))

    def test_highest_card_1(self):
        self.assertEqual(self.card3, self.card_game.highest_card(self.card3, self.card2))

    def test_highest_card_2(self):
        self.assertEqual(self.card3, self.card_game.highest_card(self.card2, self.card3))

    def test_cards_total(self):
        cards = [self.card3, self.card4, self.card5]
        self.assertEqual("You have a total of 25", self.card_game.cards_total(cards))