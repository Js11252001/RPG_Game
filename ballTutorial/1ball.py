import sys, pygame
from item import *
pygame.init()

size = width, height = 640, 480
faceSpeed = [5, 5]
ballSpeed = [2, 2]
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 120)
backgroundColor = (100, 100, 100)

screen = pygame.display.set_mode(size)

ball = Item("intro_ball.gif", size, ballSpeed)
face = Item("smileyTiny.png", size, faceSpeed)

testSurface = pygame.Surface((50,50))
testRect = pygame.Rect(0, 0, 50, 50)
test = pygame.draw.rect(testSurface, blue, testRect)

isRunning = True
while isRunning:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()
  
  ball.move()
  face.move()
  

  screen.fill(backgroundColor)
  ball.blit(screen)
  face.blit(screen)
  screen.blit(testSurface, testRect)
  pygame.display.flip()


