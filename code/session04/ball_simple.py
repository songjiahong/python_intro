import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 300
WHITE = (255, 255, 255)
BALL_RADIUS = 20
JUMP_STRENGTH = 1  # Jump strength

# Create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bump the Ball")

# Ball properties
ball_x = WIDTH // 2
ball_y = BALL_RADIUS
ball_speed_y = 0

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
        ball_speed_y = JUMP_STRENGTH

  # Update ball position
  ball_y += ball_speed_y

  # Prevent the ball from going out of the screen
  if HEIGHT - BALL_RADIUS < ball_y:
    ball_y = HEIGHT - BALL_RADIUS
    ball_speed_y = -ball_speed_y
  elif ball_y < BALL_RADIUS:
    ball_y = BALL_RADIUS
    ball_speed_y = -ball_speed_y

  # Draw the background
  screen.fill(WHITE)

  # Draw the ball
  pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), BALL_RADIUS)

  pygame.display.flip()

  # clock.tick(60)

# Quit the game
pygame.quit()
sys.exit()
