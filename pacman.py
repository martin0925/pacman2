"""Pacman 2018
Martin Janecek & Terezie Hrubanova"""
import pygame, random, sys, time
from pygame.locals import *


FPS = 5
WINDOWWIDTH = 960
WINDOWHEIGHT = 720
CELLSIZE = 30
assert WINDOWWIDTH % CELLSIZE == 0, 'Window width must be a multiple of cell size.'
assert WINDOWHEIGHT % CELLSIZE == 0, 'Window height must be a multiple of cell size.'
NUM_CELLS_X = WINDOWWIDTH // CELLSIZE
NUM_CELLS_Y = WINDOWHEIGHT // CELLSIZE
GRID = []
SCORE = 0
MAXSCORE = 1

BGCOLOR = (0,0,0)
YELLOW = (255,255,0)
PAPAYA = (255,239,213)
SEAGREEN = (46,139,87)
RED = (255,0,0)
BLUE = (0,0,128)

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, GRID, SCORE,MAXSCORE
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Pacman')

    create_grid()
    welcome_screen()
    pygame.display.update()

    while True:
        was_key_pressed()



def welcome_screen():
    title_font = pygame.font.Font('freesansbold.ttf', 100)
    title_surface = title_font.render('PACMAN', True, YELLOW)
    title_rect = title_surface.get_rect()
    title_rect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)

    msg_font = pygame.font.Font('freesansbold.ttf', 25)
    msg = msg_font.render('Press any key to start', True, PAPAYA)
    msg_rect = msg.get_rect()
    msg_rect.center = (WINDOWWIDTH / 1.4, WINDOWHEIGHT / 1.1)



    DISPLAYSURF.fill(BGCOLOR)
    DISPLAYSURF.blit(title_surface, title_rect)
    DISPLAYSURF.blit(msg, msg_rect)

def terminate():
    pygame.quit()
    sys.exit

def was_key_pressed():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    key_up_events = pygame.event.get(KEYUP)
    if len(key_up_events) == 0:
        return
    if key_up_events[0].key == K_ESCAPE:
        terminate()
    if len(key_up_events)>0:
        pygame.event.get()
        run_game()

    return True

def create_grid():
    global MAXSCORE
    """
    V mrizce cisla reprezentuji, co na tom miste bude:
    1 - obstacle
    2 - food
    3 - pacman
    """
    for i in range(NUM_CELLS_X):
        y_list = []
        for j in range(NUM_CELLS_Y):
            y_list.append(0)
        GRID.append(y_list)

    for t in range(len(GRID)):
        for u in range(len(GRID[t])):
            if (GRID[t][u] == 0):
                GRID[t][u] = 2
                MAXSCORE+=1


    GRID[1][1] = 3

    return

def draw_screen():
    #HOTOVO
    obstacle_position = [[2,2],[3,2],[6,2],[8,2],[9,2],[10,2],[11,2],[12,2],[14,2],[15,2],[16,2],[17,2],[19,2],[20,2],[21,2],[22,2],[23,2],[25,2],[28,2],[29,2],
                         [2,3],[6,3],[8,3],[14,3],[15,3],[16,3],[17,3],[23,3],[25,3],[29,3],
                         [2,4],[4,4],[5,4],[6,4],[8,4],[10,4],[11,4],[12,4],[14,4],[15,4],[16,4],[17,4],[19,4],[20,4],[21,4],[23,4],[25,4],[26,4],[27,4],[29,4],
                         [2,5],[8,5],[10,5],[11,5],[12,5],[14,5],[15,5],[16,5],[17,5],[19,5],[20,5],[21,5],[23,5],[29,5],
                         [2,6],[4,6],[5,6],[6,6],[7,6],[8,6],[23,6],[24,6],[25,6],[26,6],[27,6],[29,6],
                         [10,7],[11,7],[14,7],[15,7],[16,7],[17,7],[20,7],[21,7],
                         [2,8],[4,8],[6,8],[7,8],[8,8],[10,8],[21,8],[23,8],[24,8],[25,8],[27,8],[29,8],
                         [2,9],[4,9],[6,9],[7,9],[8,9],[10,9],[13,9],[14,9],[17,9],[18,9],[21,9],[23,9],[24,9],[25,9],[27,9],[29,9],
                         [10,10],[13,10],[18,10],[21,10],
                         [2,11],[4,11],[6,11],[8,11],[15,11],[16,11],[24,11],[26,11],[28,11],
                         [3,12],[5,12],[7,12],[15,12],[16,12],[23,12],[25,12],[27,12],[29,12],
                         [10,13],[13,13],[18,13],[21,13],
                         [2,14],[4,14],[6,14],[7,14],[8,14],[10,14],[13,14],[14,14],[17,14],[18,14],[21,14],[23,14],[24,14],[25,14],[27,14],[29,14],
                         [2,15],[4,15],[6,15],[7,15],[8,15],[10,15],[21,15],[23,15],[24,15],[25,15],[27,15],[29,15],
                         [10,16],[11,16],[14,16],[15,16],[16,16],[17,16],[20,16],[21,16],
                         [2,17],[4,17],[5,17],[6,17],[7,17],[8,17],[23,17],[24,17],[25,17],[26,17],[27,17],[29,17],
                         [2,18],[8,18],[10,18],[11,18],[12,18],[14,18],[15,18],[16,18],[17,18],[19,18],[20,18],[21,18],[23,18],[29,18],
                         [2,19],[4,19],[5,19],[6,19],[8,19],[10,19],[11,19],[12,19],[14,19],[15,19],[16,19],[17,19],[19,19],[20,19],[21,19],[23,19],[25,19],[26,19],[27,19],[29,19],
                         [2,20],[6,20],[8,20],[14,20],[15,20],[16,20],[17,20],[23,20],[25,20],[29,20],
                         [2,21],[3,21],[6,21],[8,21],[9,21],[10,21],[11,21],[12,21],[14,21],[15,21],[16,21],[17,21],[19,21],[20,21],[21,21],[22,21],[23,21],[25,21],[28,21],[29,21],
                         ]
    for n in range(NUM_CELLS_Y):
        GRID[0][n] = 1
        GRID[31][n] = 1


    for m in range(NUM_CELLS_X):
        GRID[m][0] = 1
        GRID[m][23] = 1
    for k in obstacle_position:
        GRID[k[0]][k[1]] = 1


    DISPLAYSURF.fill(BGCOLOR)
    for i in range(NUM_CELLS_X):
        for j in range(NUM_CELLS_Y):
            if (GRID[i][j]==1):
                pygame.draw.rect(DISPLAYSURF, YELLOW, (i*CELLSIZE,j*CELLSIZE, CELLSIZE, CELLSIZE))

    msg_font = pygame.font.Font('freesansbold.ttf', 25)
    msg = msg_font.render(str(SCORE), True, BLUE)
    msg_rect = msg.get_rect()
    msg_rect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
    DISPLAYSURF.blit(msg, msg_rect)
    pygame.display.update()

def draw_pacman(position_x,position_y):
    #TODO, zatim jen provizorni
    pygame.draw.rect(DISPLAYSURF, SEAGREEN,(position_x*CELLSIZE, position_y*CELLSIZE, CELLSIZE-2, CELLSIZE-2))
    pygame.display.update()



def draw_food():
    #HOTOVO
    for q in range(len(GRID)):
        for w in range(len(GRID[q])):
           if (GRID[q][w] == 2):
                food=pygame.draw.rect(DISPLAYSURF, RED,(q*CELLSIZE+CELLSIZE * 3/8,w*CELLSIZE+CELLSIZE * 3/8,CELLSIZE/4, CELLSIZE/4))

def gameover_screen():
    if(SCORE == MAXSCORE):
        title_font = pygame.font.Font('freesansbold.ttf', 100)
        title_surface = title_font.render('YOU HAVE WON!', True, BLUE)
        title_rect = title_surface.get_rect()
        title_rect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)

        msg_font = pygame.font.Font('freesansbold.ttf', 25)
        msg = msg_font.render('Your score is: ' + str(SCORE), True, BLUE)
        msg_rect = msg.get_rect()
        msg_rect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 1.5)
    else:
        title_font = pygame.font.Font('freesansbold.ttf', 100)
        title_surface = title_font.render('GAME OVER', True, RED)
        title_rect = title_surface.get_rect()
        title_rect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)

        msg_font = pygame.font.Font('freesansbold.ttf', 25)
        msg = msg_font.render('Your score is: ' + str(SCORE), True, BLUE)
        msg_rect = msg.get_rect()
        msg_rect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 1.5)



    DISPLAYSURF.fill(BGCOLOR)
    DISPLAYSURF.blit(title_surface, title_rect)
    DISPLAYSURF.blit(msg, msg_rect)
    pygame.display.update()
    while True:
        if len(pygame.event.get(QUIT)) > 0:
            terminate()

    return

def winnerscreen():

    title_font = pygame.font.Font('freesansbold.ttf', 10)
    title_surface = title_font.render('CONGRATULATIONS!', True, BLUE)
    title_rect = title_surface.get_rect()
    title_rect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 1.2)



    DISPLAYSURF.blit(title_surface, title_rect)

    pygame.display.update()
    return True





def move(direction):
    global SCORE,MAXSCORE
    new_x = 0
    new_y = 0


    pacman_x,pacman_y = 1,1
    for q in range(len(GRID)):
        for w in range(len(GRID[q])):
            if (GRID[q][w] == 3):
                pacman_x,pacman_y = q,w

    if(direction == 0):
        new_x = pacman_x-1
        new_y = pacman_y

    elif(direction == 1):
        new_x = pacman_x+1
        new_y = pacman_y

    elif(direction == 2):
        new_x = pacman_x
        new_y = pacman_y-1

    elif(direction == 3):
        new_x = pacman_x
        new_y = pacman_y+1

    if (GRID[new_x][new_y] == 1):
        gameover_screen()
        #return False

    else:
        if (GRID[new_x][new_y] == 2):
            SCORE+=1

        GRID[pacman_x][pacman_y] = 0
        GRID[new_x][new_y] = 3

        draw_screen()
        draw_pacman(new_x, new_y)
        draw_food()
        if(SCORE==MAXSCORE):
            winnerscreen()

        pygame.display.update()
        FPSCLOCK.tick(FPS)

        #return True



def run_game():
    draw_screen()
    draw_pacman(1,1)
    draw_food()
    pygame.display.update()

    """
    directions:
    0 - left
    1 - right
    2 - up
    3 - down
    """


    direction = 5
    start_moving = False
    gamecontinue = True
    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                start_moving = True
                if event.key in (K_LEFT, K_a):
                    direction = 0
                elif event.key in (K_RIGHT, K_d):
                    direction = 1
                elif event.key in (K_UP, K_w):
                    direction = 2
                elif event.key in (K_DOWN, K_s):
                    direction = 3
                elif event.key == K_ESCAPE:
                    terminate()
        if (start_moving):
            #start_moving =
            move(direction)
            #if (start_moving == False):
                #break









if __name__ == '__main__':
    main()
