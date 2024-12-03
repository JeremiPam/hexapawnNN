import hexaPawn
board=hexaPawn.Board()
board.setStartingPosition()
print(board.getPosition())

board.applyMove((7,4))
board.applyMove((0,4))
board.applyMove((8,5))
print(board.getPosition())
print(board.isTerminal())

