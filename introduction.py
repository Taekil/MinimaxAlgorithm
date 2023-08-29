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
        return scores[NodeIndex]
    
    #
    if (maxTurn): 
        return max(minimax(curDepth+1, NodeIndex*2, False, scores, targetDepth),
                   minimax(curDepth+1, NodeIndex*2+1, False, scores, targetDepth)
                   )
    else:
        return min(minimax(curDepth+1, NodeIndex*2, True, scores, targetDepth),
                   minimax(curDepth+1, NodeIndex*2+1, True, scores, targetDepth)
                   )


