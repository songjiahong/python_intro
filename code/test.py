import pygame
import sys

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))

transparent_color = pygame.Color(255, 0, 0, 255)
# Game loop
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Draw the background
  screen.fill((0, 255, 255))

  # Draw the ball
  pygame.draw.circle(screen, transparent_color, (200, 150), 20)

  pygame.display.flip()

# Quit the game
pygame.quit()
sys.exit()
