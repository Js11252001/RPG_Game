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
f = pygame.font.SysFont(['方正粗黑宋简体','microsoftsansserif'],50)
text = f.render("YOU DIE",True,(255,0,0),(255,255,255))
textRect =text.get_rect() 

ball = Item("intro_ball.gif", [2,2], size[0], size[1])
face = Item("smiley.png", [2,2], size[0], size[1])

isRunning = True
speed = 16
speed1 = 16
while isRunning:
  site = [0,0]
  site1 = [0, 0]
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
        if event.key == pygame.K_h:
            site1[1] -= speed1
        if event.key == pygame.K_j:
            site1[1] += speed1
        if event.key == pygame.K_k:
            site1[0] -= speed1
        if event.key == pygame.K_l:
            site1[0] += speed1

  screen.fill(white)          
  if ball.rect.left >= 0 and ball.rect.right <= width and ball.rect.bottom >= 0 and ball.rect.top <= ball.height:    
    ball.rect = ball.rect.move(site)
  else:
    textRect.center = (300,200)
    screen.blit(text,textRect)
  
  # face dot't add bound check
  face.rect = face.rect.move(site1)

  screen.blit(ball.object, ball.rect)
  screen.blit(face.object, face.rect)
  pygame.display.flip()