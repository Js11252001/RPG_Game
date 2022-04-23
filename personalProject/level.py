import pygame
from setting import *
from support import *
from tile import Tile
from player import Player
from random import choice

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
        layouts = {
            'boudary': importCSVLayout('./map/map_FloorBlocks.csv'),
            'grass': importCSVLayout('./map/map_Grass.csv'),
			'object': importCSVLayout('./map/map_Objects.csv'),
        }
        graphics = {
			'grass': importFolder('./graphics/grass'),
			'objects': importFolder('./graphics/objects')
		}
        for style,layout in layouts.items():
            for rowIndex, row in enumerate(layout):
                for colIndex, col in enumerate(row):
                    if col != '-1':
                        x = colIndex * TILESIZE
                        y = rowIndex * TILESIZE
                        if style == 'boudary':
                            Tile((x,y), [self.obstacleSprite], 'invisible')
                        if style == 'grass':
                            randomGrassImage = choice(graphics['grass'])
                            Tile((x,y),[self.visibleSprite,self.obstacleSprite],'grass',randomGrassImage)
                        if style == 'object':
                            surf = graphics['objects'][int(col)]
                            Tile((x,y),[self.visibleSprite,self.obstacleSprite],'object',surf)

        self.player = Player((2000, 1650), [self.visibleSprite], self.obstacleSprite)

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

        # creating the floor
        self.floorSurf = pygame.image.load('./graphics/tilemap/ground.png').convert()
        self.floorRect = self.floorSurf.get_rect(topleft = (0,0))
    
    def customDraw(self, player):

        # get offset
        self.offset.x = player.rect.centerx - self.halfWidth
        self.offset.y = player.rect.centery - self.halfHeight

        # draw the floor
        floorOffsetPos = self.floorRect.topleft - self.offset 
        self.displaySurface.blit(self.floorSurf, floorOffsetPos)

        # sort by y so that player have overlap
        for sprite in sorted(self.sprites(), key = lambda sprite : sprite.rect.centery):
            offsetPos = sprite.rect.topleft - self.offset
            self.displaySurface.blit(sprite.image, offsetPos)