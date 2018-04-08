import pygame, random, sys
from pygame.locals import *


FPS = 10
WINDOWWIDTH = 960
WINDOWHEIGHT = 720
CELLSIZE = 30
assert WINDOWWIDTH % CELLSIZE == 0, 'Window width must be a multiple of cell size.'
assert WINDOWHEIGHT % CELLSIZE == 0, 'Window height must be a multiple of cell size.'
NUM_CELLS_X = WINDOWWIDTH // CELLSIZE
NUM_CELLS_Y = WINDOWHEIGHT // CELLSIZE

BGCOLOR = (0,0,0)
YELLOW = (255,255,0)
PAPAYA = (255,239,213)

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Pacman')

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
        run_game()
    return True

def draw_screen():
    obstacle_position = [[15,15],[16,15],[17,15],[18,15],[19,15],[20,15],[21,15],[22,15]]
    for i in range(NUM_CELLS_X):
        left_bound = [0,i]
        right_bound = [31,i]
        obstacle_position.append(left_bound)
        obstacle_position.append(right_bound)
    for i in range(NUM_CELLS_X):
        top_bound = [i,0]
        down_bound = [i, 23]
        obstacle_position.append(top_bound)
        obstacle_position.append(down_bound)
    DISPLAYSURF.fill(BGCOLOR)
    for i in obstacle_position:
        pygame.draw.rect(DISPLAYSURF, YELLOW, (i[0]*CELLSIZE,i[1]*CELLSIZE, CELLSIZE, CELLSIZE))
    pygame.display.update()
    
    
def run_game():
    draw_screen()



    
if __name__ == '__main__':
    main()
