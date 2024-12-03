class Board():
    BLANK=0
    WHITE=1
    BLACK=2
    def __init__(self):
        self.turn=self.WHITE
        self.outputIndex={}
        self.board=[self.BLANK,self.BLANK,self.BLANK,
                    self.BLANK,self.BLANK,self.BLANK,
                    self.BLANK,self.BLANK,self.BLANK]
        self.availableMoves=[]

        self.outputIndex['(6,3)'] =0
        self.outputIndex['(7,4)'] =1
        self.outputIndex['(8,5)'] =2
        self.outputIndex['(3,0)'] =3
        self.outputIndex['(4,1)'] =4
        self.outputIndex['(5,2)'] =5

        self.outputIndex['(0,3)'] =6
        self.outputIndex['(1,4)'] =7
        self.outputIndex['(2,5)'] =8
        self.outputIndex['(3,6)'] =9
        self.outputIndex['(4,7)'] =10
        self.outputIndex['(5,8)'] =11

        self.whiteCaptures={
            3:[1],
            4:[0,2],
            5:[1],
            6:[4],
            7:[3,5],
            8:[4]
        }
        self.blackCaptures={
            0:[4],
            1:[3,5],
            2:[4],
            3:[7],
            4:[6,8],
            5:[7]
        }
    def setStartingPosition(self):
        self.board=[self.BLACK,self.BLACK,self.BLACK,
                    self.BLANK,self.BLANK,self.BLANK,
                    self.WHITE,self.WHITE,self.WHITE]
    def generateMoves(self,currentPosition):
        moves=[]
        if not self.availableMoves:
            if self.turn==self.WHITE:
                if self.board[currentPosition-3]==self.BLANK:
                    moves.append(currentPosition-3)
                for capture in self.whiteCaptures[currentPosition]:
                    if self.board[capture]==self.BLACK:
                        moves.append(capture)
            if self.turn==self.BLACK:
                if self.board[currentPosition+3]==self.BLANK:
                    moves.append(currentPosition+3)
                for capture in self.blackCaptures[currentPosition]:
                    if self.board[capture]==self.WHITE:
                        moves.append(capture)
        self.availableMoves=moves
        return moves
    def applyMove(self,move):
        currentPosition=move[0]
        nextPosition=move[1]
        if nextPosition in self.generateMoves(currentPosition):
            self.availableMoves=[]
            self.board[currentPosition]=self.BLANK
            self.board[nextPosition]=self.turn
            if self.turn==self.WHITE:
                self.turn=self.BLACK
            else:
                self.turn=self.WHITE
    def isTerminal(self):
        if not self.availableMoves:
            if self.turn==self.WHITE:
                return (True,self.BLACK)
            elif self.turn==self.BLACK:
                return (True,self.WHITE)
        if self.WHITE in self.board[:2]:
            return (True,self.WHITE)
        elif self.BLACK in self.board[6:8]:
            return (True,self.BLACK)
        return (False,None)