# pomodoro timer


""" DONE:
    # CREATED POMODORO WINDOW
    # DISPLAYED TEXT FOR TIME: PAUSE, RESUME, RESTART BUTTON
    # TIME CONTINUES AFTER HITTING PAUSE AS IF IT WEREN'T HIT
    # PAUSE: STOPS @ CURRENT TIME DISPLAY & IF CLICKED AGAIN --> RESUMES FROM CURRENT TIME
    # RESTART: ZEROS OUT TIME & RESTARTS TIME
    # CREATED MENU OPTION FOR 25 study x 5 break x 20 break min & worked out logic to execute it
    # CREATED MENU OPTION FOR 30 study x 10 break x 20 break min & worked out logic to execute it



# NEED TO GET DONE:
    # CREATE A SOUND TO RING ONCE BREAK_TIME HITS & TIMER ENDS
    # MAKE THE DISPLAY TEXT FOR 'BREAK' / 'STUDY' STAY LONGER ON THE SCREEN
    # MAKE IT COOLER LOOKING (NOT NECESSARY, BUT IT WOULD BE PRIDDY COO)

"""

import pygame

import time

from pygame import font


#initialize pygame library
pygame.init()


# set screen dimensions & initialize screen object [playing area]
screen = pygame.display.set_mode([300,300])

# set caption for window
pygame.display.set_caption('Pomodoro Timer')


# key methods from pygame.locals for event detection
from pygame.locals import (

    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP,
    KEYDOWN,
    QUIT,

)


# creating button object
class button:

    def __init__(self, size, color):

        self.SURFACE = pygame.Surface(size)
        self.SURFACE.fill(color)
        self.rect = self.SURFACE.get_rect() # initialize button object
        
        
    

# set font object
def setFont(name, size):
    pygame.font.init()
    font = pygame.font.SysFont(name, size)
    return font

stop = 0
        

pauseButton = button((70,30),(200,200,0)) # yellow pause button
menuButton = button((70,30),(0, 255,0)) # green menu button
restartButton = button((70,30), (244,30,230)) # purple restart button


# menu / loop option buttons
twenty5_Button = button((190,40), (255,0,0)) # red 25 min timer x 5 min break
thirty10_Button = button((190,40), (0, 255, 0)) # green 30 min timer x 10 min break

# for time
secs, mins, hours = 0,0,0

timeList = []

# IMPORTANT: KEEP FLAG / TRIGGER DECLARATION OUT OF WHILE LOOP FOR CONTROL
flag = '' # operation flag
paused = 0 # pause flag
menu = 0 # menu flag

# counter for 25 x 5 loop to toggle time intervals 
twenty5Count = 1

# counter for 30 x 10 loop to toggle time intervals
thirty10Count = 1

# counter for time loop to toggle 'RESTART' 
setCount = 0

# countDown flag bool
countDown = False

# countDown2 flag bool
countDown2 = False

clock = pygame.time.Clock()

# main game loop
run = True
while run:

    # by default # sets completed --> 0
    setCount = 0

    black = (0,0,0)
    screen.fill(black)

    x,y = pygame.mouse.get_pos()

    # setting font style
    font = setFont('bahnschrift',50)

    # button font
    butFont = setFont('bahnschrift',12)

    # menu option font
    menuFont = setFont('bahnschrift', 25)

    # end font
    endFont = setFont('bahnschrift', 18)

    # setting text for pause, menu, and restart text
    pauseText = butFont.render('PAUSE', True, (0,0,0))
    menuText = butFont.render('MENU', True, (0,0,0))
    restartText = butFont.render('RESTART', True, (0,0,0))

    # setting text for menu-option buttons
    twentyText = menuFont.render('25 MIN X 5 MIN', True, (0,0,0))
    thirtyText = menuFont.render('30 MIN X 10 MIN', True, (0,0,0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        # check if click has been made since last iter
        if event.type == pygame.MOUSEBUTTONUP:

            # menu is not triggered
            if menu == False:
                # 'pause' button is clicked
                if (30 < x < 120 and 170 < y < 200) and event.button == 1:
                    flag = 'PAUSE'

                    if paused: # clock is already paused & pause is clicked again
                        flag = 'START' # start clock
                        paused = False # no longer paused

                # 'menu' button is clicked --> menu trigger
                if (180 < x < 255 and 170 < y < 200) and event.button == 1:
                    flag = 'MENU'

                # 'restart' button is clicked --> resume
                if (30 < x < 120 and 230 < y < 260) and event.button == 1:
                    flag = 'RESTART'

            # menu is triggered
            if menu == True:
                # 25 min x 5 break button is clicked
                if (50 < x < 240 and 10 < y < 50) and event.button == 1:
                    flag = 'TWENTY5BYFIVE'

                # 30 min x 10 break button is clicked
                if (50 < x < 240 and 100 < y < 140) and event.button == 1:
                    flag = 'THIRTYBY10'
                



        
    # display cursor coordinates for testing
    print(pygame.mouse.get_pos())
    
    # game time starts
    start = time.time()

    x,y = pygame.mouse.get_pos()
    
    click = pygame.mouse.get_pressed()[0]

    # check if re-start has been triggered
    if(secs == 0 and mins == 0 and hours == 0):
        flag = 'START'

    # check for 25 x 5 min break trigger
    if(secs == 0 and mins == 0 and hours == 0 and countDown == True):
        flag = 'COUNTDOWN'

    # check for 30 x 10 min break trigger
    if(secs == 0 and mins == 0 and hours == 0 and countDown2 == True):
        flag = 'COUNTDOWN2'


    # check for pause flag
    if(secs == 1.1 and mins == 1.1 and hours == 0):
        flag == 'PAUSE'

    # setting text for hour : minute : second display
    secondDisplay = font.render('{:02d}'.format(int(secs)), True, (255,255,255))
    minuteDisplay = font.render('{:02d}'.format(int(mins)), True, (255,255,255))
    hourDisplay = font.render('{:02d}'.format(int(hours)), True, (255,255,255))

    # break display for count down & pomodoro loops
    breakDisplay = font.render('BREAK', True, (255, 0 , 0))

    # study display for count down & pomodoro loops
    studyDisplay = font.render('STUDY', True, (0, 200, 250))

    # end display for count down & pomodoro loops
    endDisplay = endFont.render('TO RESTART NAVIGATE TO MENU', True, (0, 200, 0))

    # if not menu ---> regular display
    if menu == False:

         # literally draw the hour : minute : second display
        screen.blit(secondDisplay, (190,90))
        screen.blit(minuteDisplay, (120,90))
        screen.blit(hourDisplay, (50,90))

            # literally draw the start & stop button
        screen.blit(pauseButton.SURFACE, (40, 170))
        screen.blit(menuButton.SURFACE, (180, 170))
        screen.blit(restartButton.SURFACE, (40, 230))

            # write text on start & stop buttons
        screen.blit(pauseText, (55,175))
        screen.blit(menuText, (190,175))
        screen.blit(restartText, (55, 235))

        if flag == 'PAUSE':
            paused = True
        elif flag == 'RESTART':
            secs, mins, hours = 0,0,0
        elif flag == 'START':
            # parameterizing seconds & converting to minutes & hours
            secs+=(.25)
            time.sleep(.25) # more responsive

            if secs == 60:
                secs = 0
                mins += 1

            if mins == 60:
                mins = 0
                hours += 1
        
        elif flag == 'COUNTDOWN':
            
            screen.fill(black)

            # literally draw the hour : minute : second display
            screen.blit(secondDisplay, (190,90))
            screen.blit(minuteDisplay, (120,90))
            screen.blit(hourDisplay, (50,90))

            # toggle start button to say 'SKIP'
            restartText = butFont.render('SKIP', True, (0,0,0))
            screen.blit(restartButton.SURFACE, (40, 230))
            screen.blit(restartText, (55, 235))

            secs-=(.25)
            time.sleep(.25)

            # countdown to 0 min
            if secs <= 0:
                secs = 59
                mins -= 1
            
            # once 25 min over --> 5 min break
            # IDEA: DISPLAY --> '5 MINUTE BREAK' TEXT
            if mins < 0:
                
                secs = 0
                mins = 0

                if(setCount < 1):
                
                    # study time -- 25 min
                    if twenty5Count%2 == 1 and twenty5Count != 7:
                        mins = 25
                        secs = 0
                        screen.blit(studyDisplay, (70, 20))

                    # 20 min break -- larger
                    elif twenty5Count == 6:
                        mins = 20
                        secs = 0
                        screen.blit(breakDisplay, (70, 20))

                    # if set --> end loop
                    elif twenty5Count == 7:
                        setCount+=1
                        twenty5Count = 0
                        screen.blit(endDisplay, (5, 20))

                    #  5 mins break -- regular
                    elif twenty5Count%2 == 0:
                        mins = 5
                        secs = 0
                        screen.blit(breakDisplay, (70, 20))

                    twenty5Count+=1

            # once set is complete, exit countDown mode
            if setCount == 1:

                countDown = False

        
        elif flag == 'COUNTDOWN2':

            screen.fill(black)

            # literally draw the hour : minute : second display
            screen.blit(secondDisplay, (190,90))
            screen.blit(minuteDisplay, (120,90))
            screen.blit(hourDisplay, (50,90))

            # toggle start button to say 'SKIP'
            restartText = butFont.render('SKIP', True, (0,0,0))
            screen.blit(restartButton.SURFACE, (40, 230))
            screen.blit(restartText, (55, 235))

            secs-=(.25)
            time.sleep(.25)

            # countdown to 0 min
            if secs <= 0:
                secs = 59
                mins -= 1
            
            # once 30 min over --> 10 min break
            # IDEA: DISPLAY --> '5 MINUTE BREAK' TEXT
            if mins < 0:
                
                secs = 0
                mins = 0

                if(setCount < 1):
                
                    # study time -- 30 min
                    if thirty10Count%2 == 1 and thirty10Count != 7:
                        mins = 30
                        secs = 0
                        screen.blit(studyDisplay, (70, 20))

                    # 20 min break -- larger
                    elif thirty10Count == 6:
                        mins = 20
                        secs = 0
                        screen.blit(breakDisplay, (70, 20))

                    # if set --> end loop
                    elif thirty10Count == 7:
                        setCount+=1
                        thirty10Count = 0
                        screen.blit(endDisplay, (5, 20))

                    #  10 mins break -- regular
                    elif thirty10Count%2 == 0:
                        mins = 10
                        secs = 0
                        screen.blit(breakDisplay, (70, 20))

                    thirty10Count+=1

            # once set is complete, exit countDown2 mode
            if setCount == 1:

                countDown2 = False


            
            


            
            # after 3 sets of 25 min work + 2 sets of 5 min break + 1 set of 20 min break
            # RESTART APP --> BY COUNTING REGULARLY FROM ZERO


                


        
        # before menu click --> false, after menu click --> true
        elif flag == 'MENU':
            menu = True

        # timer for 25 min x 5 min
        elif flag == 'TWENTY5BYFIVE':
            secs, mins, hours, countDown = 0,0,0,True

        # timer for 30 min x 10 min
        elif flag == 'THIRTYBY10':
            secs, mins, hours, countDown2 = 0,0,0,True
            
    
    # menu is displaying
    if menu == True:

        # black out full timer
        screen.fill(black)
        
        # literally draw the menu option buttons
        screen.blit(twenty5_Button.SURFACE, (50, 10))
        screen.blit(thirty10_Button.SURFACE, (50, 100))
        
        # draw the menu text onto the menu option buttons
        screen.blit(twentyText, (55, 10))
        screen.blit(thirtyText, (55, 100))

        # user clicks 25 min x 5 min break
        if flag == 'TWENTY5BYFIVE':

            # exit menu & run menu-false condition
            menu = False

        # user clicks 30 min x 10 min break
        elif flag == 'THIRTYBY10':

            # exit menu & run menu-false condition
            menu = False



        # MENU IDEA:
        # -- CREATE MORE OPTIONS FROM BLACKED OUT TIMER FOR LOOP / BREAK INTERVALS
        # -- ONCE OPTION IS CLICKED, UPDATE TIMER W/TIMER AMOUNT
        # -- COUNT UNTIL TIME HIT --> SOUND --> BREAK
        


    # update screen
    pygame.display.update()

# running false --> quit
pygame.quit()

