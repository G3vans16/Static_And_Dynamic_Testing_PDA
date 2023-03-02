import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card ("Clubs", 3)
        self.card2 = Card ("Diamonds", 4) 
        self.card3 = Card ("Hearts", 10)
        self.card4 = Card ("Spades", 1)

    def test_card_has_suit(self):
        self.assertEqual("Clubs", self.card1.suit)
    
    def test_card_has_value(self):
        self.assertEqual(3, self.card1.value)

    def test_check_for_ace(self):
        card = self.card4
        self.assertEqual(True, CardGame.check_for_ace(self, card))

    def test_check_for_ace_when_not_ace(self):
        card = self.card1
        self.assertEqual(False, CardGame.check_for_ace(self, card))

    def test_highest_card_card1(self):
        card1 = self.card3
        card2 = self.card2
        self.assertEqual(card1, CardGame.highest_card(self, card1, card2))

    def test_highest_card_card2(self):
        card1 = self.card1
        card2 = self.card2
        self.assertEqual(card2, CardGame.highest_card(self, card1, card2))

    def test_cards_total(self):
        cards = self.card1, self.card2, self.card3, self.card4
        cards_total = "You have a total of 18"
        returned_total = CardGame.cards_total(self, cards)
        self.assertEqual(cards_total, returned_total)


