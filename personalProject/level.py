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

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacleSprite:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0: # move right
                        self.rect.rigjt = sprite.rect.left
                    if self.direction.x < 0: # move left
                        self.rect.left = sprite.rect.right
        
        if direction == 'vertical':
            for sprite in self.obstacleSprite:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0: # move down
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0: # move up
                        self.rect.top = sprite.rect.bottom

    def run(self):
        # update & draw
        self.visibleSprite.draw(self.display_surface)
        self.visibleSprite.update()