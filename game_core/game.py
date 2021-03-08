import pygame

from game_core.player import Player
from game_core.setting import *
from game_core.wall import Wall


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Game!")
        self.new()
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(50,25)
        self.load_data()
        self.isRunning = True

    def load_data(self):
        pass

    def new(self):
        # initialize all variables and do all setup for a new game
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.player = Player(self, 10, 10)
        for x in range(10, 20):
            Wall(self, x, 5)

    def update(self):
        self.all_sprites.update()
        pass

    def draw(self):
        self.screen.fill(BLACK)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
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
                if event.key == pygame.K_LEFT:
                    self.player.move(-1)
                if event.key == pygame.K_RIGHT:
                    self.player.move(1)
                if event.key == pygame.K_UP:
                    self.player.move(dy=-1)
                if event.key == pygame.K_DOWN:
                    self.player.move(dy=1)
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_ESCAPE]:
        #     self.isRunning = False
        # if keys[pygame.K_LEFT]:
        #     self.player.move(-1)
        # if keys[pygame.K_RIGHT]:
        #     self.player.move(1)
        # if keys[pygame.K_UP]:
        #     self.player.move(dy=-1)
        # if keys[pygame.K_DOWN]:
        #     self.player.move(dy=1)

        pass

    def draw_grid(self):
        for x in range(0,WIDTH,TILESIZE):
            pygame.draw.line(self.screen, DARKGREY, (x,0),(x,HEIGHT))
        for y in range(0,HEIGHT,TILESIZE):
            pygame.draw.line(self.screen, DARKGREY, (0,y),(WIDTH,y))
        pass
