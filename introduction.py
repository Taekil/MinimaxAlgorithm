"""
https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/
minimax algorithm in Game Theory set1 
introduction

minMax -> backtracking algorithm
Backtracking? https://www.geeksforgeeks.org/introduction-to-backtracking-data-structure-and-algorithm-tutorials/
Decision
Optimization
Enumeration

Solution Vector
Constraints

Maximizer or Minimizer
"""

# a simple Pyshon 3 program to find
# maximum score that maximizing player can get. 

import math

def minimax(curDepth, NodeIndex, maxTurn, scores, targetDepth):
    
    # curDepth: the current depth in the game tree
    # base case : targetDepth reached. 
    if (curDepth == targetDepth):
        # return the score associated with the NodeIndex. 
        # evaluaating the leaf nodes of the game tree.  
        return scores[NodeIndex]
    
    # maxTurn == True
    # the code check wheter it's the maximizing player's turn. 
    if (maxTurn):
        # the minimizing player's turn.  
        return max(minimax(curDepth+1, NodeIndex*2, False, scores, targetDepth),
                   minimax(curDepth+1, NodeIndex*2+1, False, scores, targetDepth)
                   )
    else:
        # maximizing player's turn. 
        # if maximizing palyer's turn, the funciton calculates the max value
        # betweeen the scores. 
        # for the left child node(nodexIndex*2)
        # and right child node(nodeIndex*2 + 1)
        # the depth is increased by 1 and the turn is switched player's turn
        # the function calculate the minimum value between the score
        return min(minimax(curDepth+1, NodeIndex*2, True, scores, targetDepth),
                   minimax(curDepth+1, NodeIndex*2+1, True, scores, targetDepth)
                   )

"""
https://www.geeksforgeeks.org/introduction-to-evaluation-function-of-minimax-algorithm-in-game-theory/
Evaluation Function

what is "Evaluation"?

We need to implement a function that calculates the value of the board 
depending on the placement of peices on the board. 

Heuristic Function or Evaluation Function

The basic idea behind the evaluation function is to give,
    1) a high value for a board if the maximiser turn 
    or 
    2) a low value for the board if the minimizer turn. 

For this scenario to elt us consider X as the maximizer, and 
O as the minizer. 

if X wins on the board we give it a positive value of +10 

if O wins on the board we give it a negative value of -10

if no one has won or the game results in a draw then we give a
value of +0

we could have choose any positive/negative. the the sake of simplicity, 
we chose 10 and shall use lowercase 'x' and lowercase 'o' to represent
the players and the underscore '_' to represent a blank space on the board. 
if we represent our board as a 3X3 2D character matrix, like char board[3][3]
then we have to check each row, each column, and the diagonals to check if 
either of the players has gotten 3 in a row. 
"""
# function for tic tac to game
# return a value based on who is winning
# b[3][3] is the tic-tac-toe board

def evaluate(b):
    # checking for rows for X or O victory
    for row in range(0,3):
        if b[row][0] == b[row][1] and b[row][1] == b[row][2]:
            if b[row][0] == 'x':
                return 10
            elif b[row][0] == 'o':
                return -10
    # checking for columns for X or O victory
    for col in range(0,3):
        if b[0][col] == b[1][col] and b[1][col] == b[2][col]:
            if b[0][col] == 'x':
                return 10
            elif b[0][col] == 'o':
                return -10
    
    # checking for diagonals for x or o victory
    if b[0][0] == b[1][1] and b[1][1] == b[2][2]:
        if b[0][0] == 'x':
            return 10
        elif b[0][0] == 'o':
            return -10
    if b[0][2] == b[1][1] and b[1][1] == b[2][0]:
        if b[0][2] == 'x':
            return 10
        elif b[0][2] == 'o':
            return -10

    # Else if none of them have won then return 0    
    return 0
"""
purpose of evaluation function.


difference between evaluation function and heuristic funcntion. 

"""