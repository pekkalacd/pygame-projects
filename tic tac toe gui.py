"""
MODULES
"""

import pygame
from pygame import font
from pygame.locals import (

    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP,
    KEYDOWN,
    QUIT,

)

"""
WINDOW CREATION
"""

# initializing pygame library
pygame.init()

# building window / screen 
window = pygame.display.set_mode([400, 600])

# setting title of window / screen
pygame.display.set_caption('Tic Tac Toe')

"""
TIC-TAC-TOE GRID & OBJECTS 
"""

# building blocks used to create the frame of the tic tac toe board
class block:

    def __init__(self, location, size, color):
        self.SURFACE = pygame.Surface(size)
        self.SURFACE.fill(color)
        self.rect = self.SURFACE.get_rect()
        self.rect.center = location

# set font style & size of buttons & X / O objects
def setFont(name, size):
    pygame.font.init()
    font = pygame.font.SysFont(name, size)
    return font


# grid color
MINT = (170,240,209)

# grid construction
RIGHT_BAR = block((240,205), (10, 300), MINT)
LEFT_BAR = block((130, 205), (10, 300), MINT)
HORZ_BAR1 = block((190, 145), (300, 10), MINT)
HORZ_BAR2 = block((190, 255), (300, 10), MINT)


# displays letter on grid
X = setFont('comicsansms', 80).render('X', True, (255, 0, 0))
O = setFont('comicsansms', 80).render('O', True, (255, 0, 0))

# win & tie text
you_text = setFont('comicsansms', 40).render('YOU', True, (0, 100, 255))
win_text = setFont('comicsansms', 40).render('WIN!', True, (0, 255, 0))
tie_text = setFont('comicsansms', 40).render('TIE', True, (0, 233, 100))


check = input('X or O?\n')
if check.lower() == 'x':
    sign = [X, 0]
    sign2 = [O, 0]
    
elif check.lower() == 'o':
    sign = [O, 0]
    sign2 = [X, 0]


"""
GAME LOOP SETTINGS
"""

# flags to check for wining combinations
# 'top','mid','bot' --> player 1's sign [X or O]
# 'top2','mid2', 'bot2' --> player 2's sign [X or O]
top_left, top_middle, top_right = False, False, False 
top2_left, top2_middle, top2_right = False, False, False
mid_left, mid_middle, mid_right = False, False, False
mid2_left, mid2_middle, mid2_right = False, False, False
bot_left, bot_middle, bot_right = False, False, False
bot2_left, bot2_middle, bot2_right = False, False, False


# flag to check for win / tie
WIN, TIE = False, False

# counter for the # of turns
turns = 0

# number of spaces occupied
spaces = 0



run = True
while run:

    # mouse movements
    x,y = pygame.mouse.get_pos()

    if sign[0] == X:
        
        # display counters on screen
        X_count = setFont('comicsansms', 40).render('X = {}'.format(sign[1]), True, (255, 255, 255))
        O_count = setFont('comicsansms', 40).render('O = {}'.format(sign2[1]), True, (255, 255, 255))

    elif sign[0] == O:
        # display counters on screen
        X_count = setFont('comicsansms', 40).render('X = {}'.format(sign2[1]), True, (255, 255, 255))
        O_count = setFont('comicsansms', 40).render('O = {}'.format(sign[1]), True, (255, 255, 255))

    # reset board after win 
    if WIN or TIE:
        top_left, top2_left, top_middle, top2_middle, top_right, top2_right = False, False, False, False, False, False
        mid_left, mid2_left, mid_middle, mid2_middle, mid_right, mid2_right = False, False, False, False, False, False
        bot_left, bot2_left, bot_middle, bot2_middle, bot_right, bot2_right = False, False, False, False, False, False
        pygame.time.delay(2000)
        window.fill((0,0,0))
        WIN, TIE, spaces = False, False, 0

    # default screen         
    if not WIN:
        
        # display the grid on the screen
        window.blit(LEFT_BAR.SURFACE, LEFT_BAR.rect)
        window.blit(RIGHT_BAR.SURFACE, RIGHT_BAR.rect)
        window.blit(HORZ_BAR1.SURFACE, HORZ_BAR1.rect)
        window.blit(HORZ_BAR2.SURFACE, HORZ_BAR2.rect)
        window.blit(X_count, (50, 400))
        window.blit(O_count, (200, 400))
        

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False


        if event.type == pygame.MOUSEBUTTONUP:

            turns+=1

            # player 1 -- chooser of X & O -- goes on odd turns
            if(turns%2==1):
                player1 = True
                player2 = False

            # player 2 -- goes on even turns  
            elif(turns%2==0):
                player1 = False
                player2 = True


            # top left space clicked
            if (40 <= x <= 120 and 60 <= y <= 140):

                if not top_left and not top2_left:
                
                    if(player1):
                        window.blit(sign[0], (50,40))
                        top_left = True

                    elif(player2):
                        window.blit(sign2[0], (50,40))
                        top2_left = True


                    spaces+=1

            # top middle space clicked
            if (135 <= x <= 235 and 60 <= y <= 140):

                if not top_middle and not top2_middle:

                    if(player1):
                        window.blit(sign[0], (150, 40))
                        top_middle = True

                    elif(player2):
                        window.blit(sign2[0], (150, 40))
                        top2_middle = True

                    spaces+=1
                
            # top right space clicked
            if (245 <= x <= 330 and 60 <= y <= 140):

                if not top_right and not top2_right:
                    
                    if(player1):
                        window.blit(sign[0], (250, 40))
                        top_right = True
                        
                    elif(player2):
                        window.blit(sign2[0], (250, 40))
                        top2_right = True

                    spaces+=1

            # middle left space clicked
            if (40 <= x <= 120 and 150 <= y <= 250):

                if not mid_left and not mid2_left:
                
                    if(player1):
                        window.blit(sign[0], (50, 140))
                        mid_left = True
                        
                    elif(player2):
                        window.blit(sign2[0], (50, 140))
                        mid2_left = True

                    spaces+=1

            # middle mid space clicked
            if (135 <= x <= 235 and 150 <= y <= 250):

                if not mid_middle and not mid2_middle:

                    if(player1):
                        window.blit(sign[0], (150, 140))
                        mid_middle = True
                        
                    elif(player2):
                        window.blit(sign2[0], (150, 140))
                        mid2_middle = True

                    spaces+=1

            # middle right space clicked
            if (245 <= x <= 330 and 150 <= y <= 250):

                if not mid_right and not mid2_right:

                    if(player1):
                        window.blit(sign[0], (250, 140))
                        mid_right = True
                        
                    elif(player2):
                        window.blit(sign2[0], (250, 140))
                        mid2_right = True

                    spaces+=1
                    
            # bottom left space clicked
            if (40 <= x <= 120 and 260 <= y <= 360):

                if not bot_left and not bot2_left:

                    if(player1):
                        window.blit(sign[0], (50, 240))
                        bot_left = True
                            
                    elif(player2):
                        window.blit(sign2[0], (50, 240))
                        bot2_left = True

                    spaces+=1

            # bottom middle space clicked
            if (135 <= x <= 235 and 260 <= y <= 360):

                if not bot_middle and not bot2_middle:

                    if(player1):
                        window.blit(sign[0], (150, 240))
                        bot_middle = True
                        
                    elif(player2):
                        window.blit(sign2[0], (150, 240))
                        bot2_middle = True

                    spaces+=1

            # bottom right space clicked
            if (245 <= x <= 330 and 260 <= y <= 360):

                if not bot_right and not bot2_right:

                    if(player1):
                        window.blit(sign[0], (250, 240))
                        bot_right = True
                        
                    elif(player2):
                        window.blit(sign2[0], (250, 240))
                        bot2_right = True

                    spaces+=1




        """
        CHECK FOR WINS
        """

        # top horizontal row filled --> win
        if((top_left and top_middle and top_right) or (top2_left and top2_middle and top2_right)):

            if(top_left and top_middle and top_right):
                sign[1]+=1
            elif(top2_left and top2_middle and top2_right):
                sign2[1]+=1
                
            WIN = True

        # mid horizontal row filled --> win
        if((mid_left and mid_middle and mid_right) or (mid2_left and mid2_middle and mid2_right)):

            if(mid_left and mid_middle and mid_right):
                sign[1]+=1
            elif(mid2_left and mid2_middle and mid2_right):
                sign2[1]+=1
                
            WIN = True

        # bottom horizontal row filled --> win
        if((bot_left and bot_middle and bot_right) or (bot2_left and bot2_middle and bot2_right)):

            if(bot_left and bot_middle and bot_right):
                sign[1]+=1
            elif(bot2_left and bot2_middle and bot2_right):
                sign2[1]+=1
                
            WIN = True

        # left vertical column filled --> win
        if((top_left and mid_left and bot_left) or (top2_left and mid2_left and bot2_left)):

            if(top_left and mid_left and bot_left):
                sign[1]+=1
            elif(top2_left and mid2_left and bot2_left):
                sign2[1]+=1
                
            WIN = True

        # mid vertical column filled --> win
        if((top_middle and mid_middle and bot_middle) or (top2_middle and mid2_middle and bot2_middle)):

            if(top_middle and mid_middle and bot_middle):
                sign[1]+=1
            elif(top2_middle and mid2_middle and bot2_middle):
                sign2[1]+=1
                
            WIN = True

        # right vertical column filled --> win
        if((top_right and mid_right and bot_right) or (top2_right and mid2_right and bot2_right)):

            if(top_right and mid_right and bot_right):
                sign[1]+=1
            elif(top2_right and mid2_right and bot2_right):
                sign2[1]+=1
                
            WIN = True

        # left diagonal filled --> win
        if((top_left and mid_middle and bot_right) or (top2_left and mid2_middle and bot2_right)):

            if(top_left and mid_middle and bot_right):
                sign[1]+=1
            elif(top2_left and mid2_middle and bot2_right):
                sign2[1]+=1
                
            WIN = True

        # right diagonal filled --> win
        if((top_right and mid_middle and bot_left) or (top2_right and mid2_middle and bot2_left)):

            if(top_right and mid_middle and bot_left):
                sign[1]+=1
            elif(top2_right and mid2_middle and bot2_left):
                sign2[1]+=1
                
            WIN = True



        # Someone wins --> display 'WIN'
        if WIN:
            window.blit(win_text, (55, 500))
                
        
        # tie game --> 9 spaces occupied & no win
        if not WIN and spaces >= 9:
            window.blit(tie_text,(55, 500))
            TIE = True
            
                        
    

    pygame.display.update()

# USER CLICKS 'X' --> QUIT
pygame.quit()

            
