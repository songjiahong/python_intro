import pygame
import sys

# Initialize pygame
pygame.init()
WIDTH, HEIGHT = 400, 300
BALL_RADIUS = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
ball_x = WIDTH // 2
ball_y = BALL_RADIUS
ball_speed_y = 0
clock = pygame.time.Clock()
# game loop
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        ball_speed_y = 2
  # draw the background
  screen.fill((255, 255, 255))
  ball_y += ball_speed_y
  if ball_y > HEIGHT - BALL_RADIUS:
    ball_y = HEIGHT - BALL_RADIUS
    ball_speed_y = -ball_speed_y
  elif ball_y < BALL_RADIUS:
    ball_y = BALL_RADIUS
    ball_speed_y = -ball_speed_y
  # draw the ball
  pygame.draw.rect(screen, (0,0,0), (0, 0, WIDTH, HEIGHT), 10)
  pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), BALL_RADIUS)
  pygame.display.flip()
  clock.tick(60)

pygame.quit()
sys.exit()