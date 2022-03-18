from asyncio.windows_events import NULL
from item import Item
import pygame

class drawItem(Item):
    def __init__(self, speed, width, height, surface):
        self.speed = speed
        self.width = width
        self.height = height
        self.screen = surface
        self.rect = NULL

    def drawBall(self, color, pos, radius):
        self.rect = pygame.draw.circle(self.screen, color, pos, radius)

    

