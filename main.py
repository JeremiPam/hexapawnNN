import keras.src.saving
from keras import Model,Input
from fastapi.middleware.cors import CORSMiddleware
import hexaPawn
import numpy as np
from miniMax import mini_max
from typing import Union
from fastapi import FastAPI
import os
from pydantic import BaseModel
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

class MoveCreate(BaseModel):
    first:int
    target:int
class setNewGame(BaseModel):
    setNewGame:bool

def max_value_move_index(model, board):
    moves=model.predict(np.array(board.toNetworkInput(), ndmin=2,dtype=np.float32))[0][0]
    max=np.argmax(moves)
    while not (list(board.getMoveByOutputIndex(max)) in board.generateMoves()):
        moves[max]=0
        max = np.argmax(moves)
    return max

def update_data(pos,wins,moves,board,move):
    pos.append(board.toNetworkInput())
    wins.append([mini_max(board,move,0,5)])
    move_list = [0] * 28
    move_list[board.getNetworkOutputIndex(tuple(move))] = 1
    moves.append(move_list)

def play_game(board,data,model):
    positions=[]
    winners=[]
    moves=[]
    def update_data(pos,wins,moves,board,move):
        pos.append(board.toNetworkInput())
        wins.append([mini_max(board,move,0,5)])
        move_list = [0] * 28
        move_list[board.getNetworkOutputIndex(tuple(move))] = 1
        moves.append(move_list)
    computer_turn=board.turn*(-1)
    while (not board.isTerminal()[0]):
        print(np.array(board.getPosition()).reshape(3, 3), board.generateMoves())

        print('Enter index of your move:')
        move = input()
        board.applyMove(board.generateMoves()[int(move)])
        if board.isTerminal()[0]:
            print(np.array(board.getPosition()).reshape(3, 3),board.isTerminal()[1], ' wins!')
            break

        computer_move=board.getMoveByOutputIndex(max_value_move_index(model, board))
        print(np.array(board.getPosition()).reshape(3, 3))
        if mini_max(board,computer_move,0,10) != computer_turn:
            best_move=board.generateMoves()[0]
            for move in board.generateMoves():
                if mini_max(board,move,0,10)==computer_turn:
                    best_move=move
                    break
            update_data(data['positions'], data['winners'], data['moves'], board, best_move)


        board.applyMove(computer_move)
        if board.isTerminal()[0]:
            print(np.array(board.getPosition()).reshape(3, 3),board.isTerminal()[1], ' wins!')
            break

model=keras.src.saving.load_model('hexapawn_model.keras')
data={'positions':[],
      'moves':[],
      'winners':[]}
game='y'
board=hexaPawn.Board()
board.setStartingPosition()
# while(game=='y'):
#     game=input('press y to play')
#     board.setStartingPosition()
#     play_game(board,data,model)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["Content-Type"],
)


@app.get("/position")
async def root():
    return {"winner": board.isTerminal()[1],
            'board':board.getPosition(),
            'moves':board.generateMoves()}
@app.post("/move")
async def get_move(move : MoveCreate):
    computer_turn = board.turn * (-1)
    board.applyMove([move.first,move.target])
    computer_move = board.getMoveByOutputIndex(max_value_move_index(model, board))
    if mini_max(board, computer_move, 0, 10) != computer_turn:
        best_move = board.generateMoves()[0]
        for move in board.generateMoves():
            if mini_max(board, move, 0, 10) == computer_turn:
                best_move = move
                break
        update_data(data['positions'], data['winners'], data['moves'], board, best_move)
    board.applyMove(computer_move)
@app.post("/newGame")
async def set_new_game(game : setNewGame):
    board.setStartingPosition()
    if data.get('positions'):
        opt = keras.optimizers.Adam(learning_rate=0.05)
        model.compile(optimizer=opt, loss={'valueOut': 'mean_squared_error', 'policyHead': 'categorical_crossentropy'})
        model.fit(np.array(data['positions'], dtype=np.float32),
                  [np.array(data['moves'], dtype=np.float32), np.array(data['winners'], dtype=np.float32)], epochs=3,
                  batch_size=32)
    for key in data:
        data[key].clear()