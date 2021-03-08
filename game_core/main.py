import pygame
from game_core.game import Game
from game_core.setting import *

pygame.init()
game = Game()

while game.isRunning:
    game.delay_time = game.clock.tick(FPS)/1000 # ？？？
    # print(game.delay_time)
    game.event()
    game.update()
    game.draw()
    game.clock.tick(FPS)

pygame.quit()