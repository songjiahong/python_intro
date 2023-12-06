import pygame
pygame.init()

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from enemy import Enemy
from player import Player
import random

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Air shooter')
clock = pygame.time.Clock()
background = pygame.image.load('resources/image/background.png').convert()
plane_img = pygame.image.load('resources/image/shoot.png').convert_alpha()
pygame.mixer.music.load('resources/sound/game_music.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)
game_over_sound = pygame.mixer.Sound('resources/sound/game_over.wav')
game_over_sound.set_volume(0.3)
game_over = pygame.image.load('resources/image/gameover.png')
enemies = pygame.sprite.Group()
enemies_down = pygame.sprite.Group()
enemy_frequency = 0
is_plane_hit = False
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
  
  if not is_plane_hit:
    if shoot_frequency % 15 == 0:
      player.shoot()
    shoot_frequency += 1
    if shoot_frequency >= 15:
      shoot_frequency = 0
  if enemy_frequency % 50 == 0:
    enemy_pos = [random.randint(0, SCREEN_WIDTH - 57), 0]
    enemy = Enemy(plane_img, enemy_pos)
    enemies.add(enemy)
  enemy_frequency += 1
  if enemy_frequency >= 100:
    enemy_frequency = 0
  
  player.move_bullets()
  for eny in enemies:
    if eny.move():
      enemies.remove(eny)
    elif pygame.sprite.collide_circle(eny, player):
      enemies_down.add(eny)
      enemies.remove(eny)
      game_over_sound.play()
      is_plane_hit = True
      break

  enemies_down_temp = pygame.sprite.groupcollide(enemies, player.bullets, 1, 1)
  for down_enemy in enemies_down_temp:
    enemies_down.add(down_enemy)
  
  screen.fill(0)
  screen.blit(background, (0,0))
  if is_plane_hit:
    if player.draw_down(screen):
      running = False
  else:
    player.draw(screen, shoot_frequency // 8)

  for down_enemy in enemies_down:
    if down_enemy.draw_down(screen):
      enemies_down.remove(down_enemy)

  player.bullets.draw(screen)
  enemies.draw(screen)
  pygame.display.update()

screen.blit(game_over, (0, 0))
while 1:
  for evt in pygame.event.get():
    if evt.type == pygame.QUIT:
      pygame.quit()
      exit()

  pygame.display.update()
