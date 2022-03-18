import sys, pygame
pygame.init()

size = width, height = 640, 480
faceSpeed = [2, 2]
ballSpeed = [1, 1]
gray = (156, 156, 156)
white = (255, 255, 255)

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
face = pygame.image.load("smiley.png")
ballRect = ball.get_rect()
faceRect = face.get_rect()

isRunning = True
while isRunning:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()

  ballRect = ballRect.move(ballSpeed)
  if ballRect.left < 0 or ballRect.right > width:
    ballSpeed[0] = -ballSpeed[0]
  if ballRect.top < 0 or ballRect.bottom > height:
    ballSpeed[1] = -ballSpeed[1]

  faceRect = faceRect.move(faceSpeed)
  if faceRect.left < 0 or faceRect.right > width:
    faceSpeed[0] = -faceSpeed[0]
  if faceRect.top < 0 or faceRect.bottom > height:
    faceSpeed[1] = -faceSpeed[1]

  screen.fill(white)
  screen.blit(ball, ballRect)
  screen.blit(face, faceRect)
  pygame.display.flip()