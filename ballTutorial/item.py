import pygame


class Item:
    def __init__(self, imageName, speed, width, height):
        self.object = pygame.image.load(imageName)
        self.speed = speed
        self.width = width
        self.height = height
        self.rect = self.object.get_rect()
    
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > self.width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > self.height:
            self.speed[1] = -self.speed[1]     