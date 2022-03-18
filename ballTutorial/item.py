import pygame


class Item:
    def __init__(self, imageName, speed, height, width):
        self.object = pygame.image.load(imageName)
        self.speed = speed
        self.width = width
        self.height = height
        self.rect = self.object.get_rect()
    
    def move(self):
        faceRect = self.rect.move(self.speed)
        if faceRect.left < 0 or faceRect.right > self.width:
            self.speed[0] = -self.speed[0]
        if faceRect.top < 0 or faceRect.bottom > self.height:
            self.speed[1] = -self.speed[1]        