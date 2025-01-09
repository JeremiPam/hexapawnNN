import copy

import hexaPawn
def minimax(boardState, move, currDepth, targetDepth,alpha=-1000,beta=1000):
    board=copy.deepcopy(boardState)
    board.applyMove(move)
    if board.isTerminal()[0] or currDepth==targetDepth:
        return board.isTerminal()[1]
    if board.turn==1:
        best=-1000
        for move in board.generateMoves():
            evaluation=minimax(board, move, currDepth + 1, targetDepth,alpha,beta)
            best=max(evaluation,best)
        return best
    if board.turn==-1:
        best=1000
        for move in board.generateMoves():
            evaluation = minimax(board, move, currDepth + 1, targetDepth,alpha,beta)
            best = min(evaluation, best)
        return best
board=hexaPawn.Board()
board.setStartingPosition()
print(board.getPosition())
print(board.toNetworkInput())
print(board.getPosition())
print('ruchy',board.generateMoves(),board.turn)
board.applyMove((7,4))
print(board.getPosition())
print('ruchy',board.generateMoves(),board.turn)
print(minimax(board, board.generateMoves()[3], 0, 10))

# board.applyMove(board.generateMoves()[0])
# print('ruchy',board.generateMoves(),board.turn)
# board.applyMove(board.generateMoves()[0])
# print('ruchy',board.generateMoves(),board.turn)
# print(board.getPosition(),board.generateMoves(),board.turn)
# board.applyMove((8,5))
# print('ruchy2',board.generateMoves(),board.turn,board.isTerminal())

