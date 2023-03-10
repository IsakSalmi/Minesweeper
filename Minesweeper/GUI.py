import pygame as p
import Minesweeper.Config as Config
import Minesweeper.MinesweeperEngien as Engien
import Minesweeper.MinnesweeperAI as AI

BOARD_HIGHT = Config.BOARD_HIGHT
BOARD_WIDTH = Config.BOARD_WIDTH
MAX_FPS = Config.MAX_FPS
DIMENTION = Config.DEMANTION
SQ_SIZE = Config.SQ_SIDE 

ENABLEAI = Config.ENABLE_AI

Flag_image = p.transform.scale(p.image.load("Image/Flag.png"), (SQ_SIZE-4, SQ_SIZE-4))
Bomb_image = p.transform.scale(p.image.load("Image/Bomb.png"), (SQ_SIZE-4, SQ_SIZE-4))

p.init()


def StartGame():
    
    gs = Engien.MinesweeperEngien()
    gsAI = AI.AI()
    gs.fillBoard()
    FirstClick = False
    
    Screen = p.display.set_mode((BOARD_WIDTH,BOARD_HIGHT))
    Clock = p.time.Clock()
    Screen.fill(p.Color('Black'))
    start = False
    meny = True
    
    while meny:
        for e in p.event.get():
            if e.type == p.QUIT:
                meny = False
            elif e.type == p.MOUSEBUTTONDOWN:
                if  (BOARD_WIDTH-50)/2< p.mouse.get_pos()[0] < (BOARD_WIDTH-50)/2 + 100 and BOARD_HIGHT/2-100 < p.mouse.get_pos()[1] < (BOARD_HIGHT/2-100) + 30:
                    start = True
                    meny = False
                
        drawStartScreen(Screen)
        Clock.tick(MAX_FPS)
        p.display.flip()
    
    while start:
        
        for e in p.event.get():
            if e.type == p.QUIT:
                start = False
            elif e.type == p.KEYDOWN:
                if e.key == p.K_r:
                    gs.ResetGame()
                    FirstClick = False
            elif e.type == p.MOUSEBUTTONDOWN:
                if gs.GameStatus and not(ENABLEAI):
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
                
        if ENABLEAI and gs.GameStatus:
            Move = gsAI.BestMove(gs)
            if FirstClick == False: 
                    gs.createBoard(Move[0],Move[1])
                    FirstClick = True
                    gs.PrintGameboard()
            gs.SelectSQ(Move[0],Move[1])
        drawGameState(Screen,gs)
        Clock.tick(MAX_FPS)
        p.display.flip()
 
 
        
def drawGameState(screen,gs):
    Board = gs.GetBoard()
    font = p.font.SysFont('Arial', 10)
    for r in range(DIMENTION):
        for c in range(DIMENTION):
            if Board[r][c] == '-':
                p.draw.polygon(screen, (53, 171, 57), (((SQ_SIZE * c, SQ_SIZE * r),(SQ_SIZE * c, SQ_SIZE * (r+1)),((SQ_SIZE * (c+1), SQ_SIZE * r)))))
                p.draw.polygon(screen, (6, 66, 8), (((SQ_SIZE * c, SQ_SIZE * (r+1)),(SQ_SIZE * (c+1), SQ_SIZE * r),((SQ_SIZE * (c+1), SQ_SIZE * (r+1))))))
                
                p.draw.rect(screen, (31, 128, 34), p.Rect(SQ_SIZE * c + 4, SQ_SIZE * r + 4, SQ_SIZE-7, SQ_SIZE-7))
            elif Board[r][c] == 'F':
                screen.blit(Flag_image, p.Rect(SQ_SIZE * c+4, SQ_SIZE * r, SQ_SIZE, SQ_SIZE))
            elif Board[r][c] == '*':
                screen.blit(Bomb_image, p.Rect(SQ_SIZE * c+4, SQ_SIZE * r, SQ_SIZE, SQ_SIZE))
            elif Board[r][c] == '0':
                p.draw.rect(screen, p.Color('Black'), p.Rect(SQ_SIZE * c, SQ_SIZE * r, SQ_SIZE+1, SQ_SIZE+1))
            else:
                textObject = font.render(Board[r][c], 0, p.Color('white'))
                textLocation = p.Rect((SQ_SIZE * c + (SQ_SIZE/4)), (SQ_SIZE * r + (SQ_SIZE/4)), (2 * SQ_SIZE * c), (2 * SQ_SIZE * r))
                p.draw.rect(screen,p.Color("Black"),p.Rect(SQ_SIZE * c, SQ_SIZE * r, SQ_SIZE+1, SQ_SIZE+1))
                screen.blit(textObject, textLocation)
                
    if gs.GameStatus == False:
        font = p.font.SysFont('Helvitica', 32, True, False)
        textObject = font.render("Game Over", 0, p.Color('Red'))
        textLocation = p.Rect(0, 0, BOARD_WIDTH, BOARD_HIGHT).move(BOARD_WIDTH / 2 - textObject.get_width() / 2, BOARD_HIGHT / 2 - textObject.get_height() / 2)
        screen.blit(textObject, textLocation)
        
    elif gs.Win == True:
        font = p.font.SysFont('Helvitica', 32, True, False)
        textObject = font.render("You won :)", 0, p.Color('Red'))
        textLocation = p.Rect(0, 0, BOARD_WIDTH, BOARD_HIGHT).move(BOARD_WIDTH / 2 - textObject.get_width() / 2, BOARD_HIGHT / 2 - textObject.get_height() / 2)
        screen.blit(textObject, textLocation)
        
        
def drawStartScreen(Screen):
    Screen.fill((6, 66, 8))
    drawButton(Screen,"start",BOARD_WIDTH/2-50,BOARD_HIGHT/2-100,100,30)   
        
        
def drawButton(screen,text,x1,y1,x2,y2):
    font = p.font.SysFont('Helvitica', 30, True, False)
    textObject = font.render(text, 0, p.Color('Black'))
    textLocation = p.Rect(x1, y1, x2, y2)
    p.draw.circle(screen, p.Color("Gray"), [x1+x2, (y1+(y1+y2))/2], y2/2)
    p.draw.circle(screen, p.Color("Gray"), [x1, (y1+(y1+y2))/2], y2/2)
    p.draw.rect(screen,p.Color("Gray"),textLocation)
    screen.blit(textObject, textObject.get_rect(center = textLocation.center))