from typing import List

import pygame

from os import path
from game_core.player import Player
from game_core.setting import *
from game_core.tilemap import Map, Camera
from game_core.wall import Wall


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Game!")
        self.new()
        self.clock = pygame.time.Clock()
        self.delay_time = 0
        pygame.key.set_repeat(500, 100)
        self.load_data()
        self.isRunning = True

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(path.dirname(__file__), "image")
        self.map = Map(path.join(game_folder, "map_big.txt"))
        self.player_image = pygame.transform.scale(pygame.image.load(path.join(img_folder, PLAYER_IMAGE)).convert_alpha(),(TILESIZE,TILESIZE))
        pass

    def new(self):
        # initialize all variables and do all setup for a new game
        self.load_data()
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == "1":
                    Wall(self, col, row)
                if tile == "P":
                    self.player = Player(self, col, row)
        self.camera = Camera(self.map.width, self.map.height)

    def update(self):
        self.all_sprites.update()
        self.camera.update(self.player)
        pass

    def draw(self):
        self.screen.fill(BLACK)
        self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        # pygame.draw.rect(self.screen, WHITE,self.player.hit_rect, 1)
        pygame.display.flip()

    def event(self):
        # catch all event here
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.isRunning = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.isRunning = False
                pass

    def draw_grid(self):
        for x in range(0,WIDTH,TILESIZE):
            pygame.draw.line(self.screen, DARKGREY, (x,0),(x,HEIGHT))
        for y in range(0,HEIGHT,TILESIZE):
            pygame.draw.line(self.screen, DARKGREY, (0,y),(WIDTH,y))
        pass
