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

# image flipping
def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

def load_sprite_sheets(dir1, dir2, width, height, direction= False):
    path = join("assets", dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))]
    
    all_sprites = {}
    
    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()
        
        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))
            
        if direction:
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
        else:
            all_sprites[image.replace(".png", "") ] = sprites
            
    return all_sprites
            
            

# define the player class
class Player(pygame.sprite.Sprite):
    RED = (255, 0, 0)
    # set Gravity
    GRAVITY = 1
    
    # load sprites
    SPRITES = load_sprite_sheets("Players", "NinjaFrog", 32, 32, True)
    
    #object initialization
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        #set the x and y velocity of the player
        self.x_velocity = 0
        self.y_velocity = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
        self.fall_count = 0
        
    def move(self, displacement_x, displacement_y):
        self.rect.x += displacement_x
        self.rect.y += displacement_y
        
    def move_left(self, velocity):
        self.x_velocity = -velocity
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0
        
    def move_right(self, velocity):
        self.x_velocity = velocity
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0
            
    def update(self, fps):
        # self.y_velocity += min(1, (self.fall_count / fps) * self.GRAVITY)
        
        self.move(self.x_velocity, self.y_velocity)
        
        self.fall_count += 1
        
    def draw(self, window):
        # pygame.draw.rect(window, self.RED, self.rect)
        self.sprite = self.SPRITES["idle_" + self.direction][0]
        window.blit(self.sprite, (self.rect.x, self.rect.y))

# generate the background
def get_background(name):
    #load the images in background folder
    image = pygame.image.load(join("assets", "Backgrounds", name))
    # get the width and height of the tiles while ignoring the x and y
    _, _, width, height = image.get_rect()
    # create an empty list of tiles
    tiles = []
    
    # determine the number of tiles needed for the width and height
    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            # pos of the tiles
            pos = (i * width, j * height)
            tiles.append(pos)
            
    return tiles, image

# define the draw function
def draw(window, background, bg_image, player):
    for tile in background:
        # add image to window
        window.blit(bg_image, tile)
    player.draw(window)
    pygame.display.update()

# Handle player movement
def handle_movement(player):
    keys = pygame.key.get_pressed()
    
    player.x_velocity = 0
    
    if keys[pygame.K_LEFT]:
        player.move_left(VELOCITY)
    if keys[pygame.K_RIGHT]:
        player.move_right(VELOCITY)

# main function
def main(window):
    # establish the clock
    clock = pygame.time.Clock()
    # set the level background
    background, bg_image = get_background("Pyramid.jpg")
    
    #init player
    player = Player(100,100,50,50)
    
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
        
        player.update(FPS)
        handle_movement(player)    
        draw(window, background, bg_image, player)
    pygame.quit()
    quit()


#exicutes the mainfunction if it exists
if __name__ == "__main__":
    main(window)
    
