import pygame
from game_core.setting import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x # left of rectangle
        self.y = y # top of rectangle

    def update(self, *args, **kwargs) -> None:
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy
        pass

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x +dx and wall.y == self.y + dy:
                return True
        return False