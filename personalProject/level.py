import pygame
from setting import *
from tile import Tile
from player import Player

class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # spriteGruop setup
        self.visibleSprite = YSortCameraGroup()
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
        self.visibleSprite.customDraw(self.player)
        self.visibleSprite.update()

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        # general setup
        super().__init__()
        self.displaySurface = pygame.display.get_surface()
        self.halfWidth = self.displaySurface.get_size()[0] / 2
        self.halfHeight = self.displaySurface.get_size()[1] / 2
        self.offset = pygame.math.Vector2()
    
    def customDraw(self, player):

        # get offset
        self.offset.x = player.rect.centerx - self.halfWidth
        self.offset.y = player.rect.centery - self.halfHeight
        for sprite in self.sprites():
            offsetPos = sprite.rect.topleft - self.offset
            self.displaySurface.blit(sprite.image, offsetPos)