import copy
import hexaPawn
from miniMax import mini_max
from os import environ
environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import keras
from keras.src.layers import Dense
from keras import Input,Model
import numpy as np
import tensorflow.keras.backend as K

board=hexaPawn.Board()
board.setStartingPosition()
def get_training_data(board,positions,moves,winners):
    if board.isTerminal()[0]:
        return
    for move in board.generateMoves():
        positions.append(board.toNetworkInput())
        moves_list = [0] * 28
        moves_list[board.getNetworkOutputIndex(tuple(move))] = 1
        moves.append(moves_list)
        winners.append(mini_max(board, move, 0, 5))
        temp=copy.deepcopy(board)
        temp.applyMove(move)
        get_training_data(temp,positions,moves,winners)
temp_pos=[]
temp_moves=[]
temp_win=[]
get_training_data(board,temp_pos,temp_moves,temp_win)

positions=np.array(temp_pos,ndmin=2)
moves=np.array(temp_moves,ndmin=2)
winners=np.array(temp_win,ndmin=2).T

inp=Input(shape=(21,))
l1=Dense(128,activation='relu')(inp)
l2=Dense(128,activation='relu')(l1)
l3=Dense(128,activation='relu')(l2)

policyOut=Dense(28,name='policyHead',activation='softmax')(l3)
valueOut=Dense(1,name='valueOut',activation='tanh')(l3)

model=Model(inp,[policyOut,valueOut])
model.compile(optimizer='SGD',loss={'valueOut':'mean_squared_error','policyHead':'categorical_crossentropy'})
model.fit(positions,[moves,winners],epochs=10,batch_size=32)
board_test=hexaPawn.Board()
board_test.setStartingPosition()
board_test.applyMove(board_test.generateMoves()[0])
board_test.applyMove(board_test.generateMoves()[0])
board_test.applyMove(board_test.generateMoves()[0])
print(model.predict(np.array(board_test.toNetworkInput(),ndmin=2)))



