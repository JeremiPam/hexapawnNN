import copy

import miniMax as mm
import hexaPawn
from miniMax import mini_max

# from os import environ
# environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
# import keras
# from keras.src.layers import Dense
# from keras import Input

outcomes={'position':[],
          'move':[],
          'winner':[]}
board=hexaPawn.Board()
board.setStartingPosition()
def get_training_data(board,outcomes):
    if board.isTerminal()[0]:
        return
    for move in board.generateMoves():
        outcomes['position'].append(board.getPosition())
        outcomes['move'].append(move)
        outcomes['winner'].append(mini_max(board, move, 0, 5))
        temp=copy.deepcopy(board)
        temp.applyMove(move)
        get_training_data(temp,outcomes)
get_training_data(board,outcomes)



