# Imports
import pygame
import math
import random

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "My Awesome Picture"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
RED = (255, 0, 0)
GREEN = (40, 173, 17)
BLUE = (40, 55, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125 , 0)
YELLOW = (250, 255, 0)
BROWN = (191, 91, 28)

''' make snow'''
snow = []
for i in range(200):
    x = random.randrange(0,800)
    y = random.randrange(0,400)
    r = random.randrange(1,5)
    snow.append([x, y, r, r])


def darw_cloud(x, y):
    pygame.draw.ellipse(screen, WHITE, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])


    
# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # Game logic (Check for collisions, update points, etc.)
    ''' leave this section alone for now ''' 

    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLUE)
    pygame.draw.rect(screen, GREEN, [0, 450, 1300, 300])
    pygame.draw.rect(screen, BROWN, [400, 250, 300, 200])
    pygame.draw.polygon(screen, BLACK, [[350, 250], [550, 150], [750, 250]])
    pygame.draw.rect(screen, YELLOW, [510, 325, 80, 125])
    pygame.draw.rect(screen, WHITE, [420, 275, 75, 75])
    pygame.draw.rect(screen, WHITE, [600, 275, 75, 75])
    pygame.draw.line(screen, BLACK, [460, 275], [460, 350], 2)
    pygame.draw.line(screen, BLACK, [495, 312.5], [420, 312.5], 2)
    pygame.draw.line(screen, BLACK, [637, 275], [637, 350], 2)
    pygame.draw.line(screen, BLACK, [674, 312.5], [600, 312], 2)

    '''snow'''
    for s in snow:
        pygame.draw.ellipse(screen, WHITE, s)

    y = 380
    for x in range (5, 800, 30):
        post = [[x+5, y], [x+10, y+5], [x+10, y+40], [x, y+40]]

    

    ''' angles for arcs are measured in radians (a pre-cal topic) '''
    pygame.draw.arc(screen, YELLOW, [100, 100, 200, 200], 0, math.pi*2, 100)


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
