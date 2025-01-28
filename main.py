from keras.models import load_model
import keras
import hexaPawn
import numpy as np
from miniMax import mini_max


def max_value_move_index(model, board):
    moves=model.predict(np.array(board.toNetworkInput(), ndmin=2))[0][0]
    max=np.argmax(moves)
    while not (tuple(board.getMoveByOutputIndex(max)) in board.generateMoves()):
        moves[max]=0
        max = np.argmax(moves)
    return max


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
            print(best_move)

        board.applyMove(computer_move)
        if board.isTerminal()[0]:
            print(np.array(board.getPosition()).reshape(3, 3),board.isTerminal()[1], ' wins!')
            break

model=load_model('hexapawn_model.keras')
board=hexaPawn.Board()
data={'positions':[],
      'moves':[],
      'winners':[]}
game='y'
board.setStartingPosition()
while(game=='y'):
    game=input('press y to play')
    board.setStartingPosition()
    play_game(board,data,model)
    if data.get('positions'):
        opt = keras.optimizers.Adam(learning_rate=0.05)
        model.compile(optimizer=opt, loss={'valueOut': 'mean_squared_error', 'policyHead': 'categorical_crossentropy'})
        model.fit(np.array(data['positions']),[np.array(data['moves']),np.array(data['winners'])],epochs=3,batch_size=32)
    for key in data:
        data[key]=[]

