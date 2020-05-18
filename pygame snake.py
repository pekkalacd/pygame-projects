# a snake game using the pygame library


# WHAT'S DONE:
    # CREATED SNAKE OBJECT
    # SNAKE IS CONTROLLED BY ARROW KEYS & CONTAINED WITHIN  WINDOW
    # IF SNAKE HITS WALL --> LOSE
    # APPLE CREATED @ RANDOM LOCATION
    # IF APPLE IS EATEN ---> NEW APPLE GENERATED @ RANDOM LOCATION
    # NUMBER OF APPLES EATEN IS COUNTED IN YUMDISPLAY
    # 'YUM!' POPS UP AT RANDOM WHEN APPLE IS EATEN
    # SNAKE GROWS AFTER EACH APPLE EATEN
    # ROTATION OF SNAKE IS SOMEWHAT GOOD


# WHAT NEEDS TO BE DONE:

    # GHOST DRIVER --> CURRENTLY, THE USER CONTROLS THE MOVEMENT OF THE SNAKE. IF USER STOPS, SNAKE STOPS.
    # THERE NEEDS TO BE A GHOST_DRIVER THAT AUTOMATICALLY PROPELS THE SNAKE IN THE DIRECTION OF TRAVEL
    # PLAY AGAIN FEATURE
    # MULTIPLE LEVELS
    # MINES ADDED IN @ RANDOM --> IF SNAKE HITS MINE --> LOSE
    # PORTAL SPACE --> IF SNAKE ENTERS PORTAL SPACE, NEW MAP OPENS UP W/NEW SPRITES.
    




# import pygame library
import pygame

# import font module from pygame library
from pygame import font

# import pygame.locals as namespace for access to key calls
from pygame.locals import (

    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,

)

# import random for apple drop
import random

# construct snake object as 'player' 
class Snake(pygame.sprite.Sprite):

    # init attributes
    def __init__(self):

        self.SURFACE = pygame.Surface((25,25)) # small block
        self.SURFACE.fill((0, 255, 105)) # neon green
        self.rect = self.SURFACE.get_rect()
        
    # moving
    def update(self, pressed_keys, SCREEN_WIDTH, SCREEN_HEIGHT,modUp):

        
        # up key pressed --> move rectangle up
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -(2+modUp))

        # down key pressed --> move rectangle down
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, (2+modUp))
            

        # left key pressed --> move rectangle left
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-(2+modUp),0)

        # right key pressed --> move rectangle right
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip((2+modUp),0)


        # boundary conditions to keep user from going off screen
        
        if self.rect.left < 0: # limit user's movement to left bound of window
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH: # limit user's movement to right bound of window
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0: # limit user's movement to top bound of window
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT: # limit user's movement to bottom of window
            self.rect.bottom = SCREEN_HEIGHT

    

# set font style & size
def setFont(name, size):
    pygame.font.init() # initialize font module
    font = pygame.font.SysFont(name, size) # create instance of font object
    return font


# create random apple block to eat
class Apple:

    def __init__(self):

        import random
        
        self.SURFACE = pygame.Surface((15,15)) # apple block size
        self.SURFACE.fill((255, 0, 0)) # color: red
        self.rect = self.SURFACE.get_rect() # initialize apple object

        # randomize coordinates of apple object
        x_coor = random.randint(0,487)
        y_coor = random.randint(0,487)
        self.rect.center = (x_coor, y_coor)



# play again box
class playAgain:

    def __init__(self):
        self.SURFACE = pygame.SURFACE((30,30)) # play again box
        self.SURFACE.fill((0,100,100))
        self.rect = self.SURFACE.get_rect()
        
        
        

# initialize pygame library
pygame.init()


# window dimension
screenWidth = 500
screenHeight = 500

# initialize screen object containing window dimensions
screen = pygame.display.set_mode([screenWidth, screenHeight])


# window title
pygame.display.set_caption('Snake Game')


# initiate snake / player object
snake = Snake()

# initiate apple object @ a random location
apple = Apple()


# set up game clock to moderate game speed
clock = pygame.time.Clock()

# counter for loop --> multiplies the length of the snake & serves as addition module
snakeLen = .17

# yumCount for yumDisplay
yumCount=0


# by default --> modUp {difficulty modulator} set to zero, but increments over time {faster movements w/ each yum!}
modUp = 0

# by default --> running
running = True
while running:

    # for each thing the user does (pygame.event.get() pulls from istream) 
    for event in pygame.event.get():

        # if a key is pressed --> take care of snake rotations 
        if event.type == KEYDOWN:

            if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_LEFT):
                snake.SURFACE = pygame.transform.scale(snake.SURFACE, (int(25+snakeLen), 25)) # width larger than height
                snake.SURFACE = pygame.transform.rotate(snake.SURFACE, 0)

            if (event.key == pygame.K_UP) or (event.key == pygame.K_DOWN):
                snake.SURFACE = pygame.transform.scale(snake.SURFACE, (25, int(25+snakeLen))) # invert dimensions
                snake.SURFACE = pygame.transform.rotate(snake.SURFACE, 180)
                
                        
            # and if the key is the ESC key --> break loop
            if event.key == K_ESCAPE:
                running = False

        # if the user clicks 'x' in window --> break loop 
        if event.type == pygame.QUIT:
            running = False

    # get all the keys pressed by user
    pressed_keys = pygame.key.get_pressed()

    # move according to the keys that are pressed 
    snake.update(pressed_keys, screenWidth, screenHeight, modUp)

    # x & y coordinates of position of apple
    x_apple = apple.rect.center[0]
    y_apple = apple.rect.center[1]

    # x & y-coordinates of position of snake
    x_snake = snake.rect.center[0]
    y_snake = snake.rect.center[1]

    # color specification
    black = (0,0,0)
    
    # fill screen with black after each movement & by default
    screen.fill(black)

    # set yum counter display
    font2 = setFont('bahnschrift',20)
    yumDisplay = font2.render('YUM COUNT = {}'.format(yumCount), True, (255,255,255))
    screen.blit(yumDisplay, (30,30))


    # check if the snake 'eats' apple
    if abs(x_snake - x_apple) <= (30+(snakeLen*.1)) and abs(y_snake - y_apple) <= (30+(snakeLen*.1)):
        apple.SURFACE.fill((0,0,0)) # fill the current apple surface w/ black
        pygame.transform.scale(snake.SURFACE, (int(25+snakeLen), 25)) # snake grows w/ each apple eaten by snakeLen

        apple = Apple() # create new apple

        # create yum font to display after each apple is 'eaten'
        x_coor = random.randint(30,400) # randomize x coordinate
        y_coor = random.randint(30,400) # randomize y coordinate

        # set yum display
        font = setFont('bahnschrift',40)
        yumFont = font.render('YUM!', True, (255,105,180)) # hot pink YUM!
        screen.blit(yumFont, (x_coor,y_coor))
        screen.blit(snake.SURFACE, snake.rect)
        pygame.display.update()
        yumCount+=1
        modUp+=.25 # incremement by .1 --> +.1 amt 'harder' --> faster movements per apple eaten
        snakeLen+=5# increment size of snake by 1.5
        clock.tick(15) # buffer low
        

        

    # check if user hits a 'wall' of window --> crashed
    if (x_snake == 487 or y_snake == 487):
        apple.SURFACE.fill((255,255,255))
        screen.fill((255,255,255)) # overwrite apple w/ screen
        font = setFont('bahnschrift', 40)
        crashedFont = font.render('YOU HAVE CRASHED', True, (255,0,0))
        screen.blit(crashedFont, (70,200))
        running = False
        


    # draw the apple on the screen
    screen.blit(apple.SURFACE, apple.rect)

    # draw the snake on the screen
    screen.blit(snake.SURFACE, snake.rect)

    # flip the display --> send configuration to video card to display
    pygame.display.flip()

    # 60 frames per second displayed
    clock.tick(60)

# continue to do all of the above, until the user clicks 'x' in corner, then quit.
pygame.quit()
    

