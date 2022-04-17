import pygame
from setting import *
from tile import Tile
from player import Player

class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # spriteGruop setup
        self.visibleSprite = pygame.sprite.Group()
        self.obstacleSprite = pygame.sprite.Group()

        # sprite setup
        self.createMap()

    def createMap(self):
        for rowIndex, row in enumerate(WORLD_MAP):
            for colIndex, col in enumerate(row):
                x = colIndex * TILESIZE
                y = rowIndex * TILESIZE
                if col == 'x':
                    Tile((x,y), [self.visibleSprite, self.obstacleSprite])
                if col == 'p':
                    self.player = Player((x,y), [self.visibleSprite], self.obstacleSprite)

    def run(self):
        # update & draw
        self.visibleSprite.draw(self.display_surface)
        self.visibleSprite.update()