import unittest
from game import Game
from player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.player1 = Player('p1','X')
        self.player2 = Player('p2','-')


    def test_initialization(self):
        self.assertIsNone(self.game.board)
        self.assertIsNone(self.game.player1)
        self.assertIsNone(self.game.player2)
        self.assertIsNone(self.game.chance)

    def test_register_players(self):
        self.game.register_player1(self.player1)
        self.assertEqual(self.player1.name,'p1', "Player1 name is not initiated accurately")
        
        self.game.register_player2(self.player1)
        self.assertIsNone(self.game.player2, "Player1 initiated in game as Player2 also")
        
        self.game.register_player2(self.player2)
        self.assertEqual(self.player2.name, 'p2', "Player2 name not initialized accurately")

    def test_start(self):
        self.game.register_player1(self.player1)
        self.game.register_player2(self.player2)

        self.game.start()
        
        self.assertEqual(self.game.board[0][0], '0')
        self.assertEqual(self.game.player_dict['p1'], self.player1)
        self.assertEqual(self.game.chance, 'p1')




        

    


if __name__ == '__main__':
    unittest.main()

    