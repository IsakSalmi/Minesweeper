import Minesweeper.Config as Config
import random

class MinesweeperEngien:
    def __init__(self):
        self.GameBoard = []
        self.DisplayBoard = []
        self.Mines = Config.MINES
        self.GameStatus = True
        self.Win = False
    
    def fillBoard(self):
        for r in range(Config.DEMANTION):
            self.DisplayBoard.append([])
            self.GameBoard.append([])
            for c in range(Config.DEMANTION):
                self.GameBoard[r].append('-')
                self.DisplayBoard[r].append('-')  
    
    def GetBoard(self):
        return self.DisplayBoard
    
    def SelectSQ(self, sr, sc):
        if self.GameBoard[sr][sc] == '-':
            self.DisplayBoard[sr][sc] = '0'
        elif self.GameBoard[sr][sc] != '*':
            self.DisplayBoard[sr][sc] = self.GameBoard[sr][sc]
        else:
            self.displayMines()
            self.GameStatus = False
            
        if self.GameStatus:
            directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
            AvSQ = []
            if(self.GameBoard[sr][sc] == '-'):
                AvSQ.append((sr,sc))
            while len(AvSQ) != 0:
                r = AvSQ[0][0]
                c = AvSQ[0][1]
                for d in directions:
                    endRow = r + d[0]
                    endCol = c + d[1]
                    if endRow >= 0 and endRow < Config.DEMANTION and endCol >= 0 and endCol < Config.DEMANTION:
                        if self.GameBoard[endRow][endCol] == '-':
                            AvSQ.append((endRow,endCol))
                            self.GameBoard[endRow][endCol] = '0'
                            self.DisplayBoard[endRow][endCol] = '0'
                        elif self.GameBoard[endRow][endCol] != '*':
                            self.DisplayBoard[endRow][endCol] = self.GameBoard[endRow][endCol]
                AvSQ.pop(0)

        
        if self.won():
            self.Win = True
    
    
    def won(self):
        coutn = 0
        for r in range(Config.DEMANTION):
            for c in range(Config.DEMANTION):
                if self.DisplayBoard[r][c] == '-' or self.DisplayBoard[r][c] == 'F':
                    coutn += 1
                    
        if coutn == Config.MINES:
            return True
        return False    
        
    def ResetGame(self):
        self.DisplayBoard = []
        self.GameBoard = []
        self.fillBoard()
        self.GameStatus = True
        self.Win = False    

    def createBoard(self,sr,sc):
        directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        Mines = 0
        while Mines < self.Mines:
            r = random.randint(0,Config.DEMANTION-1)
            c = random.randint(0,Config.DEMANTION-1)
            if  (r != sr and c != sc)  and self.GameBoard[r][c] != '*':
                self.GameBoard[r][c] = '*'
                for d in directions:
                    endRow = r + d[0]
                    endCol = c + d[1]
                    if endRow >= 0 and endRow < Config.DEMANTION and endCol >= 0 and endCol < Config.DEMANTION:
                        if self.GameBoard[endRow][endCol] == '-':
                            self.GameBoard[endRow][endCol] = '1'
                        elif self.GameBoard[endRow][endCol] == '*':
                            pass
                        else:
                            temp = self.GameBoard[endRow][endCol]
                            temp = int(temp)
                            temp += 1
                            temp = str(temp)
                            self.GameBoard[endRow][endCol] = temp
                Mines += 1

    def PrintGameboard(self):
        for r in range(Config.DEMANTION):
            print(self.GameBoard[r])

    def flagSQ(self, r, c):
        if self.DisplayBoard[r][c] == '-':
            self.DisplayBoard[r][c] = 'F'
    
    def displayMines(self):
        for r in range(Config.DEMANTION):
            for c in range(Config.DEMANTION):
                if self.GameBoard[r][c] == '*':
                    self.DisplayBoard[r][c] = '*'
    
    
        


