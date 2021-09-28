import unittest
from main import Game

game = Game()


class MyTestCase(unittest.TestCase):
    def test_TestInput_A(self):
        self.assertEqual(game.TestInput("paper"), True)  # Tests that correct input is accepted

    def test_TestInput_B(self):
        self.assertEqual(game.TestInput("thermonuclear warhead"), False)  # Test that incorrect input is rejected

    def test_FindWin_A(self):
        self.assertEqual(game.FindWin("rock", "paper"), "paper beats rock! YOU WON!")  # Test player victory

    def test_FindWin_B(self):
        self.assertEqual(game.FindWin("paper", "rock"), "paper beats rock! I WON!")  # Test bot victory

    def test_FindWin_C(self):
        self.assertEqual(game.FindWin("rock", "rock"), "rock and rock?! Stalemate!")  # Test Stalemate

    def test_FindWin_D(self):
        self.assertEqual(game.FindWin("EEEEEE", "ERROR"), "... what. Somehow, an error occurred?")  # Test Error

    def test_BotMove_A(self):
        self.assertEqual(game.BotMove(0, 0), "rock")  # Test Rock

    def test_BotMove_B(self):
        self.assertEqual(game.BotMove(1, 1), "paper")  # Test Paper

    def test_BotMove_C(self):
        self.assertEqual(game.BotMove(2, 2), "scissors")  # Test Scissors

    def test_BotMove_D(self):
        self.assertEqual(game.BotMove(3, 3), "scissors")  # Test Error


if __name__ == '__main__':
    unittest.main()
