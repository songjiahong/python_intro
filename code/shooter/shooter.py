import pygame

pygame.init()

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Air shooter')
clock = pygame.time.Clock()
background = pygame.image.load('resources/image/background.png').convert()
plane_img = pygame.image.load('resources/image/shoot.png').convert_alpha()
plane_rect = pygame.Rect(0, 99, 102, 126)
img = plane_img.subsurface(plane_rect).convert_alpha()
plane_rect.topleft = [200, 400]
running = True
speed = 5
while running:
  clock.tick(45)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  key_pressed = pygame.key.get_pressed()
  if key_pressed[pygame.K_UP]:
    plane_rect.top -= speed
    if plane_rect.top < 0:
      plane_rect.top = 0
  elif key_pressed[pygame.K_DOWN]:
    plane_rect.top += speed
    if plane_rect.top > SCREEN_HEIGHT - plane_rect.height:
      plane_rect.top = SCREEN_HEIGHT - plane_rect.height
  elif key_pressed[pygame.K_LEFT]:
    plane_rect.left -= speed
    if plane_rect.left < 0:
      plane_rect.left = 0
  elif key_pressed[pygame.K_RIGHT]:
    plane_rect.left += speed
    if plane_rect.left > SCREEN_WIDTH - plane_rect.width:
      plane_rect.left = SCREEN_WIDTH - plane_rect.width
      
  screen.fill(0)
  screen.blit(background, (0,0))
  screen.blit(img, plane_rect)
  pygame.display.update()