"""
https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/

alpha-beta pruning - not enw algorithm, but rather an optimization technique
for the minimax algorithm. 

it reduces the compuation time by a huge factor. 

this allows us to search much faster and even go into deeper levels
in the game tree. 

it cuts off branches in the game treee which need not be searched because
there already exists a better move available. 

it is called alpha-beta pruning because it passes 2 extra parameters in the 
minimax function, namely alpha and beta. 

let's define the parameters alpha and beta. 

Alpha is the best value that the maximizer currently can guarantee at that level
or above. 
Beta is the best value that the minimizer currently can guarantee at that level or
below. 
"""

"""
Pseudo-Code:
function minimax(node, depth, inMaximizingPlayer, alpha, beta):
    if node is a leaf node:
        return value of the nodes
    
    if isMaximizingPalyer:
        bestVal = -INFINITY
        for each child node:
            value = minimax(node, depth+1, false, alpha, beta)
            bestVal = max(bestVal, value)
            alpha = max(alpha, bestVal)
            if beta <= alpha:
                break
    
        return bestVal
    
    else:
        bestVal = +INFINITY
        for each child node:
            value = minimax(node, depth+1, true, alpha, beta)
            bestVal = min(bestVal, value)
            beta = min(beta, bestVal)
            if beta <= alpha:
                break
        return bestVal

# calling the function for the first time. 
minimax(0, 0, -INFINITY, +INFINITY)



"""
