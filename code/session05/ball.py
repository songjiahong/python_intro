import pygame
import sys
import random
import math

# Initialize pygame
pygame.init()
WIDTH, HEIGHT = 400, 300
BALL_RADIUS = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))

image = pygame.image.load("ball.png").convert_alpha()
image = pygame.transform.scale(image,(BALL_RADIUS,BALL_RADIUS))
ball_x = WIDTH // 2
ball_y = HEIGHT - BALL_RADIUS
ball_speed = 0
angle_radians = 0

clock = pygame.time.Clock()
# game loop
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        # Jump when spacebar is pressed
        ball_speed = 5
        angle_radians = random.uniform(0, math.pi)
  # draw the background
  screen.fill((255, 255, 255))
  # Update ball position
  ball_x += ball_speed * math.cos(angle_radians)
  ball_y += ball_speed * math.sin(angle_radians)
  # Prevent the ball from going out of the screen
  if HEIGHT - BALL_RADIUS < ball_y:
    ball_y = HEIGHT - BALL_RADIUS
    angle_radians = -angle_radians
  elif ball_y < 0:
    ball_y = 0
    angle_radians = -angle_radians
  elif ball_x < 0:
    ball_x = 0
    angle_radians = math.pi - angle_radians
  elif WIDTH - BALL_RADIUS < ball_x:
    ball_x = WIDTH - BALL_RADIUS
    angle_radians = math.pi - angle_radians
  # draw the ball
  screen.blit(image, (ball_x, ball_y))  
  pygame.display.flip()
  clock.tick(60)

pygame.quit()
sys.exit()