import pygame as p
import Minesweeper.Config as Config
import Minesweeper.MinesweeperEngien as Engien


BOARD_HIGHT = Config.BOARD_HIGHT
BOARD_WIDTH = Config.BOARD_WIDTH
MAX_FPS = Config.MAX_FPS
DIMENTION = Config.DEMANTION
SQ_SIZE = Config.SQ_SIDE 

p.init()


def StartGame():
    
    gs = Engien.MinesweeperEngien()
    FirstClick = False
    
    Screen = p.display.set_mode((BOARD_WIDTH,BOARD_HIGHT))
    Clock = p.time.Clock()
    Screen.fill(p.Color('Black'))
    start = True
    while start:
        
        for e in p.event.get():
            if e.type == p.QUIT:
                start = False
            elif e.type == p.MOUSEBUTTONDOWN:
                if gs.GameStatus:
                    if e.button == 1:
                        location = p.mouse.get_pos()
                        col = int(location[0] // SQ_SIZE)
                        row = int (location[1] // SQ_SIZE)
                        if FirstClick == False: 
                            gs.createBoard(row,col)
                            FirstClick = True
                        gs.PrintGameboard()
                        gs.SelectSQ(row,col)
                    elif e.button == 3:
                        location = p.mouse.get_pos()
                        col = int(location[0] // SQ_SIZE)
                        row = int (location[1] // SQ_SIZE)
                        gs.flagSQ(row,col)
                
                
        drawGameState(Screen,gs)
        Clock.tick(MAX_FPS)
        p.display.flip()
        
        
        
def drawGameState(screen,gs):
    Board = gs.GetBoard()
    font = p.font.SysFont('Arial', 30)
    for r in range(DIMENTION):
        for c in range(DIMENTION):
            if Board[r][c] == '-':
                p.draw.rect(screen, p.Color('Gray'), p.Rect(SQ_SIZE * c, SQ_SIZE * r, SQ_SIZE+1, SQ_SIZE+1))
            elif Board[r][c] == 'F':
                p.draw.rect(screen, p.Color('Red'), p.Rect(SQ_SIZE * c, SQ_SIZE * r, SQ_SIZE+1, SQ_SIZE+1))
            elif Board[r][c] == '0':
                p.draw.rect(screen, p.Color('Black'), p.Rect(SQ_SIZE * c, SQ_SIZE * r, SQ_SIZE+1, SQ_SIZE+1))
            else:
                textObject = font.render(Board[r][c], 0, p.Color('white'))
                textLocation = p.Rect((SQ_SIZE * c), (SQ_SIZE * r), (SQ_SIZE + SQ_SIZE * c), (SQ_SIZE + SQ_SIZE * r))
                p.draw.rect(screen,p.Color("Black"),p.Rect(SQ_SIZE * c, SQ_SIZE * r, SQ_SIZE+1, SQ_SIZE+1))
                screen.blit(textObject, textLocation)
