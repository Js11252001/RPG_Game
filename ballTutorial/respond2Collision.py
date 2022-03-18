import sys, pygame
from item import *
pygame.init()

size = width, height = 1280, 960
gray = (156, 156, 156)
white = (255, 255, 255)

screen = pygame.display.set_mode(size)

ball = Item("intro_ball.gif", [1,1], size[0], size[1])
face = Item("smileyTiny.png", [2,1], size[0], size[1])

isRunning = True
while isRunning:
  mouseX = pygame.mouse.get_pos()[0]
  mouseY = pygame.mouse.get_pos()[1]  
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()

  if ball.rect.contains(face.rect):
      
  ball.move()
  face.move()
  
  screen.fill(white)

  screen.blit(ball.object, ball.rect)
  screen.blit(face.object, face.rect)
  pygame.display.flip()