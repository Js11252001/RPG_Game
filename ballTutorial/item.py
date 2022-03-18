import pygame


class Item:
    def __init__(self, imageName, speed, width, height):
        self.object = pygame.image.load(imageName)
        self.speed = speed
        self.width = width
        self.height = height
        self.rect = self.object.get_rect()
    
    def move(self):
        rect = self.rect.move(self.speed)
        if rect.left < 0 or rect.right > self.width:
            self.speed[0] = -self.speed[0]
        if rect.top < 0 or rect.bottom > self.height:
            self.speed[1] = -self.speed[1]     