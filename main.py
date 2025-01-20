from keras.models import load_model
import hexaPawn
import numpy as np

model=load_model('hexapawn_model.keras')
board=hexaPawn.Board()
board.setStartingPosition()
def max_index(model,board):
    moves_str=board.generateMoves()
    moves_indices=[]
    for move in moves_str:
        moves_indices.append(board.getNetworkOutputIndex(tuple(move)))
    max=0
    for move in moves_indices:
        if model.predict(np.array(board.toNetworkInput(), ndmin=2))[0][0][move] > max:
            max=move
    return max
def min_index(model,board):
    moves_str = board.generateMoves()
    moves_indices = []
    for move in moves_str:
        moves_indices.append(board.getNetworkOutputIndex(tuple(move)))
    min = 1
    for move in moves_indices:
        if model.predict(np.array(board.toNetworkInput(), ndmin=2))[0][0][move] < min:
            min = move
    return min

while(not board.isTerminal()[0]):
    print(board.getPosition(),board.generateMoves())
    print('Enter index of your move:')
    move=input()
    board.applyMove(board.generateMoves()[int(move)])
    if board.isTerminal()[0]:
        print(board.isTerminal()[1],' wins!')
        break
    print('computer move:',board.getMoveByOutputIndex(max_index(model,board)))
    board.applyMove(board.getMoveByOutputIndex(max_index(model,board)))
    if board.isTerminal()[0]:
        print(board.isTerminal()[1],' wins!')
        break
