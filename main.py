import pygame
import math
import random
import os

# import from os what we need to navigate the directory
from os import listdir
from os.path import join, isfile

# initialize pygame
pygame.init()

# set up title caption
pygame.display.set_caption("My Platformer")

# Set up the colors that I may or maynot use
RED = (255, 0, 0)
ORANGE = (235, 137, 52)
YELLOW = (235, 216, 52)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 52, 235)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# The width and height constants
WIDTH = 960
HEIGHT = 540

# set frames per second
FPS = 60

#player velocity 
VELOCITY = 5


#create the pygame window
window = pygame.display.set_mode((WIDTH, HEIGHT))


# main function
def main(window):
    # establish the clock
    clock = pygame.time.Clock()
    
    # Running boolean
    run = True
    
    # our gameloop
    while run:
        # set the clock ticks to FPS
        clock.tick(FPS)
        
        # event listening
        for event in pygame.event.get():
            # test if the player wants to quit
            if event.type == pygame.QUIT:
                run = False
                break
            
    pygame.quit()
    quit()


#exicutes the mainfunction if it exists
if __name__ == "__main__":
    main(window)
    
