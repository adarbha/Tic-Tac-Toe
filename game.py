import numpy as np
from player import Player

class Game:
    '''Template of the game class for creating a new game'''

    def __init__(self):
        self.board = None
        self.player1 = None
        self.player2 = None
        self.chance = None

    def register_player1(self, player):
        self.player1 = player
        print(self.player1)
        print("\n")
        print("is registered!")

    def register_player2(self, player):
        # Check if this player's name and marker are unique
        if player.name == self.player1.name:
            print("Player1 used this name already, please use a different name")
            return

        if player.marker == self.player1.marker:
            print("Player1 used this marker already, plaease use a different marker")
            return

        self.player2 = player

    def start(self):
        self.board = np.zeros((3,3), dtype = int).astype(str)
        self.player_dict = {self.player1.name:self.player1, self.player2.name:self.player2} #This dict is used to pull up players based on name

        print(self)

        print("Player1 - please place your marker")
        self.chance = self.player1.name # Register the current player name to chance


    def place_marker(self, player_name, row, col):
        ''' player_name - player_name that is set to play the round
            row - row number of a 3X3 numpy matrix
            col - column number of a 3x3 numpy matrix'''
        

        if (self.player1.name != player_name) or (self.player2.name != player_name):
            print("Player name has to be from one of the registered users")
            print("It is {}'s chance to play".format(self.chance))
            return

        if self.chance != player.name:
            print("Only {} is allowed to place the marker".format(self.chance))
            return
            

        if self.board[row][col] != 0:
            print("Thats not a vacant spot. You can't place your marker there")
            return
        else:
            self.board[row][col] = self.player_dict[player_name].marker 
                


        if self.is_game_over():
            print("{} - Wins!".format(player_name))
            print(self)
            return

        if self.is_board_full():
            print("Its a tie!")
            print(self)
            return

        self.switch_chance()
            
    
    def switch_chance(self):
        if self.chance == self.player1.name:
            self.chance = self.player2.name
        else:
            self.chance = self.player2.name

        print("Its {} chance to play now".format(self.chance))


    def is_game_over(self):
        
        for i in range(3):
            # Horizontal check
            if all(self.board[i,:] == self.player_dict[self.chance].marker):
                return True
            # Vertical check
            if all(self.board[:,i] == self.player_dict[self.chance].marker):
                return True
        

        # Diagonal check
        if all(np.diagonal(self.board) == self.player_dict[self.chance].marker):
            return True

        if all(np.flipud(self.board).diagonal == self.player_dict[self.chance].marker):
            return True

        return False
        


    def is_board_full(self):
        return not any(np.ravel(self.board) == '0')
        

    def __repr__(self):
        game_info = "Current state of the board: {}".format(self.board)
        player_info = "{} \n {}".format(repr(self.player1), repr(self.player2))
        return "{} \n {}".format(game_info, player_info)

    