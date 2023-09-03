"""
TicTacToe game apply the minMaxAlgorithm
TicTacToe game apply alphabetaPruning
"""
"""
https://www.geeksforgeeks.org/finding-optimal-move-in-tic-tac-toe-using-minimax-algorithm-in-game-theory/
Finding optimal move in Tic-Tac-Toe Using Minmax Algorithm in Game Theory
"""

# AUTHOR TAEKIL OH
# DATE SEP 3rd 2023
# PURPOSE main file for TicTacToe Game
# TicTacToe.py

# create board 
# the size of board is 3 X 3
class GameBoard:
    # initilizing the game board.
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def display_board(self):
        # self.board list of lists.
        # each row represents a horizontal row on the game board. 
        for row in self.board:
            # join(): a string method used to concatenate (join) a sequence
            # of strings with a specified separator into a sing string. 
            print("|".join(row))
            print("-----")

class Player:
    def __init__(self):
        pass

    @staticmethod
    def player_turn_deciding():
        # get input: player's turn is 'X' or 'O'
        while True:
            try:
                decision = input("Enter the Turn(X or O):")
                if decision == 'O' or decision == 'X':
                    return decision
                else:
                    print("Invalid Input, try again")
            except ValueError:
                print("Invalid input.")
    
    @staticmethod
    def get_player_input(GameBoard):
        while True:
            try:
                # get the number of row and col for the location. 
                row = int(input("Enter row(0, 1, or 2): "))
                col = int(input("Enter col(0, 1, or 2)"))
                if 0 <= row <= 2 and 0 <= row <= 2 and GameBoard[row][col] == ' ':
                    return row, col
                else:
                    print("Invalid Input, try again")
            except ValueError:
                print("Invalid input. Enter Numbers for Row and Column")

class AI:
    def __init__(self):
        return

class playing:
    def __init__(self):
        GameBoard = GameBoard()
        Player = Player()
        AI = AI()
    
    def firstTurnToDecidePlayerSymbol():
        Player.player_turn_deciding()

    
game = GameBoard()
game.display_board()
