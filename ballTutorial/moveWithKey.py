import sys, pygame
from turtle import speed
from item import *
pygame.init()

size = width, height = 640, 480
faceSpeed = [2, 2]
ballSpeed = [1, 1]
gray = (156, 156, 156)
white = (255, 255, 255)

screen = pygame.display.set_mode(size)

ball = Item("intro_ball.gif", [2,2], size[0], size[1])
face = Item("smiley.png", [2,2], size[0], size[1])

isRunning = True
speed = 16
while isRunning:
  site = [0,0]
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            site[1] -= speed
        if event.key == pygame.K_s:
            site[1] += speed
        if event.key == pygame.K_a:
            site[0] -= speed
        if event.key == pygame.K_d:
            site[0] += speed
        if event.key == pygame.K_UP:
            speed *= 2
        if event.key == pygame.K_DOWN:
            speed /= 2
            

  # ball.move()
  # face.move()
  
  ball.rect = ball.rect.move(site)

  screen.fill(white)

  screen.blit(ball.object, ball.rect)
  # screen.blit(face.object, face.rect)
  pygame.display.flip()