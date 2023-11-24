import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 300
WHITE = (255, 255, 255)
BALL_RADIUS = 20

# Create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bump the Ball")

# Ball properties
ball_x = WIDTH // 2
ball_y = BALL_RADIUS
ball_speed = 0
angle_radians = 0

clock = pygame.time.Clock()

# Game loop
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        # Jump when spacebar is pressed
        ball_speed = 2
        angle_radians = random.uniform(0, math.pi)

  # Update ball position
  ball_x += ball_speed * math.cos(angle_radians)
  ball_y += ball_speed * math.sin(angle_radians)

  # Prevent the ball from going out of the screen
  if HEIGHT - BALL_RADIUS < ball_y:
    ball_y = HEIGHT - BALL_RADIUS
    angle_radians = -angle_radians
  elif ball_y < BALL_RADIUS:
    ball_y = BALL_RADIUS
    angle_radians = -angle_radians
  elif ball_x < BALL_RADIUS:
    ball_x = BALL_RADIUS
    angle_radians = math.pi - angle_radians
  elif WIDTH - BALL_RADIUS < ball_x:
    ball_x = WIDTH - BALL_RADIUS
    angle_radians = math.pi - angle_radians

  # Draw the background
  screen.fill(WHITE)

  # Draw the ball
  pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), BALL_RADIUS)

  pygame.display.flip()

  clock.tick(60)

# Quit the game
pygame.quit()
sys.exit()
