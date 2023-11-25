import pygame
from player import Player, SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()

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
  shoot_frequency += 1
  if shoot_frequency >= 15:
    shoot_frequency = 0
  screen.fill(0)
  screen.blit(background, (0,0))
  player.draw(screen, shoot_frequency // 8)
  pygame.display.update()