# Tic-Tac-Toe
This project aims to create pieces for creating a Tic-Tac-Toe game. Two important classes that are implemeted are Game and Player class.<br/>
The best and the easiest way to install the package is to use
<code>pip install tittactoeadarbha</code>
The following is the expected workflow of how the pieces are assimilated
* Create a game object and register player1 and player2 to that game,
  * from tictactoe_adarbha import Game
  * from tictactoe_adarbha import Player
  * p1 = Player('p1','X')
  * p2 = Player('p2','_')
  * g = Game()
  * g.register_player1(p1)
  * g.register_player2(p2)
* Start the game
  * g.start()
* Play the game
  * g.place_marker('p1',0,0)
  * .
  * .
  * .
* Keep playing until either p1 or p2 wins or its a draw