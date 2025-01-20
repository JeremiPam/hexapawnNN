import copy
def mini_max(boardState, move, currDepth, targetDepth, alpha=-1000, beta=1000):
    board=copy.deepcopy(boardState)
    board.applyMove(move)
    if board.isTerminal()[0] or currDepth==targetDepth:
        return board.isTerminal()[1]
    if board.turn==1:
        best=-1000
        for move in board.generateMoves():
            evaluation=mini_max(board, move, currDepth + 1, targetDepth, alpha, beta)
            best=max(evaluation,best)
        return best
    if board.turn==-1:
        best=1000
        for move in board.generateMoves():
            evaluation = mini_max(board, move, currDepth + 1, targetDepth, alpha, beta)
            best = min(evaluation, best)
        return best