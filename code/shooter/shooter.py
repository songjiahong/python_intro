import pygame
pygame.init()

from player import Player, SCREEN_WIDTH, SCREEN_HEIGHT

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Air shooter')
clock = pygame.time.Clock()
background = pygame.image.load('resources/image/background.png').convert()
plane_img = pygame.image.load('resources/image/shoot.png').convert_alpha()
player = Player(plane_img)
shoot_frequency = 0
running = True
speed = 5
while running:
  clock.tick(45)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  key_pressed = pygame.key.get_pressed()
  if key_pressed[pygame.K_UP]:
    player.move_up()
  elif key_pressed[pygame.K_DOWN]:
    player.move_down()
  elif key_pressed[pygame.K_LEFT]:
    player.move_left()
  elif key_pressed[pygame.K_RIGHT]:
    player.move_right()
  
  shoot_frequency += 1
  if shoot_frequency >= 15:
    shoot_frequency = 0
  
  if shoot_frequency % 15 == 0:
    player.shoot()
  
  player.move_bullets()
  screen.fill(0)
  screen.blit(background, (0,0))
  player.draw(screen, shoot_frequency // 8)
  player.bullets.draw(screen)
  pygame.display.update()