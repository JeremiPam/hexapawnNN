import copy

import hexaPawn
def miniMax(boardState,move,currDepth,targetDepth):
    board=copy.deepcopy(boardState)
    board.applyMove(move)
    if board.isTerminal()[0] or currDepth==targetDepth:
        return board.isTerminal()[1]
    if board.turn==1:
        best=-1000
        for move in board.generateMoves():
            evaluation=miniMax(board,move,currDepth+1,targetDepth)
            best=max(evaluation,best)
        return best
    if board.turn==-1:
        best=1000
        for move in board.generateMoves():
            evaluation = miniMax(board, move,currDepth+1,targetDepth)
            best = min(evaluation, best)
        return best
board=hexaPawn.Board()
board.setStartingPosition()
print(board.getPosition())
print('ruchy',board.generateMoves(),board.turn)
board.applyMove(board.generateMoves()[0])
print(board.generateMoves())
#board.applyMove(board.generateMoves()[1])
print(board.isTerminal())
print(board.getPosition(),board.generateMoves(),board.turn)
print(miniMax(board,board.generateMoves()[2],0,5))
# board.applyMove(board.generateMoves()[0])
# print('ruchy',board.generateMoves(),board.turn)
# board.applyMove(board.generateMoves()[0])
# print('ruchy',board.generateMoves(),board.turn)
# print(board.getPosition(),board.generateMoves(),board.turn)
# board.applyMove((8,5))
# print('ruchy2',board.generateMoves(),board.turn,board.isTerminal())

