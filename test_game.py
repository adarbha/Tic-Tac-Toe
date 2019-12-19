import unittest
from game import Game
from player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()


    def test_initialization(self):
        self.assertIsNone(self.game.board)
        self.assertIsNone(self.game.player1)
        self.assertIsNone(self.game.player2)
        self.assertIsNone(self.game.chance)

    


if __name__ == '__main__':
    unittest.main()

    