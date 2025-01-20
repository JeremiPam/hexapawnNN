from bidict import bidict
class Board():
    BLANK=0
    WHITE=1
    BLACK=-1
    def __init__(self):
        self.turn=self.WHITE
        self.outputIndex=bidict({})
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

        self.outputIndex['(6,4)']=12
        self.outputIndex['(7,3)'] =13
        self.outputIndex['(7,5)'] =14
        self.outputIndex['(8,4)'] =15
        self.outputIndex['(3,1)'] =16
        self.outputIndex['(4,0)'] =17
        self.outputIndex['(4,2)'] =18
        self.outputIndex['(5,1)'] =19

        self.outputIndex['(0,4)'] =20
        self.outputIndex['(1,3)'] =21
        self.outputIndex['(1,5)'] =22
        self.outputIndex['(2,4)'] =23
        self.outputIndex['(3,7)'] =24
        self.outputIndex['(4,6)'] =25
        self.outputIndex['(4,8)'] =26
        self.outputIndex['(5,7)'] =27

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
    def getPosition(self):
        return self.board
    def setStartingPosition(self):
        self.board=[self.BLACK,self.BLACK,self.BLACK,
                    self.BLANK,self.BLANK,self.BLANK,
                    self.WHITE,self.WHITE,self.WHITE]
    def generateMoves(self):
        moves=[]
        currentPositions=[index for index,e in enumerate(self.board) if e==self.turn]
        for p in currentPositions:
            if self.turn == self.WHITE:
                if self.board[p-3]==self.BLANK:
                    moves.append([p,p-3])
                for capture in self.whiteCaptures[p]:
                    if self.board[capture]==self.BLACK:
                        moves.append([p,capture])
            if self.turn==self.BLACK:
                if self.board[p+3]==self.BLANK:
                    moves.append([p,p+3])
                for capture in self.blackCaptures[p]:
                    if self.board[capture]==self.WHITE:
                        moves.append([p,capture])
        self.availableMoves=moves
        return moves
    def applyMove(self,move):
        currentPosition=move[0]
        nextPosition=move[1]
        tmp=[]
        for e in self.generateMoves():
            tmp.append(e[1])
        if self.board[currentPosition]==self.BLANK or self.board[currentPosition]!=self.turn or nextPosition not in tmp:
            raise Exception('wrong move passed!')


        self.board[currentPosition]=self.BLANK
        self.board[nextPosition]=self.turn
        if self.turn==self.WHITE:
            self.turn=self.BLACK
        else:
            self.turn=self.WHITE
    def isTerminal(self):

        availableMoves=self.generateMoves()
        currentTurn=self.turn

        if not availableMoves:
            if currentTurn==self.WHITE:
                return (True,self.BLACK)
            else:
                return (True,self.WHITE)
        if self.WHITE in self.board[:3]:
            return (True,self.WHITE)
        if self.BLACK in self.board[6:9]:
            return (True,self.BLACK)
        return (False,self.BLANK)
    def toNetworkInput(self):
        networkVector=[]
        for i in self.board:
            if i==self.WHITE:
                networkVector.append(1)
            else:
                networkVector.append(0)
        for i in self.board:
            if i==self.BLACK:
                networkVector.append(1)
            else:
                networkVector.append(0)
        if self.turn==self.WHITE:
            for i in range(3):
                networkVector.append(0)
        elif self.turn==self.BLACK:
            for i in range(3):
                networkVector.append(1)
        return networkVector
    def getNetworkOutputIndex(self,move):
        return self.outputIndex[str(move).replace(' ','')]
    def getMoveByOutputIndex(self,index):
        str=self.outputIndex.inv[index]
        ints=[int(str[1]),int(str[3])]
        return tuple(ints)
