import pygame

WIDTH, HEIGHT = 1024, 768

FPS = 60

'''color'''
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREY = (40, 40, 40)
YELLOW = (255, 255, 0)

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

'''player setting'''
PLAYER_SPEED = 300
PLAYER_ROATATE_SPEED = 250
PLAYER_IMAGE = "manBlue_gun.png"
PLAYER_HIT_RECT = pygame.Rect(0, 0, 30, 30)
