import sys, pygame
from item import *
pygame.init()

size = width, height = 640, 480
ballSpeed = [0, 0]
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 120)
backgroundColor = (100, 100, 100)

screen = pygame.display.set_mode(size)

ball = Item("intro_ball.gif", size, ballSpeed)

testSurface = pygame.Surface((50,50))
testRect = pygame.Rect(0, 0, 50, 50)
test = pygame.draw.rect(testSurface, blue, testRect)

isRunning = True
while isRunning:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        ball.moveAmount((-10,0))
      if event.key == pygame.K_RIGHT:
        ball.moveAmount((10,0))
      if event.key == pygame.K_UP:
        ball.moveAmount((0,-10))
      if event.key == pygame.K_DOWN:
        ball.moveAmount((0,10))
    
  if pygame.mouse.get_pressed()[0] == 1:
    mouse_position = pygame.mouse.get_pos()
    if ( ball.rect.collidepoint( mouse_position ) ): 
      is_ball_move = True
  else:
    is_ball_move = False
  
  if is_ball_move:
    moveAmount = list(pygame.mouse.get_rel())
    #print(mouse_position)
    #ball.moveAmount(moveAmount)
    ball.moveToPosition(mouse_position)
  
  '''if pygame.key.get_pressed():
    print(pygame.key.name())'''
  

  screen.fill(backgroundColor)
  ball.blit(screen)
  screen.blit(testSurface, testRect)
  pygame.display.flip()


