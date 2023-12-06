from board import Board
from stone import Stone
import pygame

# The configuration
cell_size = 28
cols = 12
rows = 22
maxfps = 30
colors = [
  (0, 0, 0),
  (35, 35, 35),
  (146, 202, 73),
  (255, 85, 85),
  (100, 200, 115),
  (120, 108, 245),
  (255, 140, 50),
  (50, 120, 52),
  (150, 161, 218),
]

class TetrisGame(object):
  def __init__(self):
    pygame.init()
    self.width = cell_size*(cols+6)
    self.height = cell_size*rows
    self.screen = pygame.display.set_mode((self.width, self.height))
    self.bground_grid = [[ 1 if x%2==y%2 else 0 for x in range(cols)] for y in range(rows)]
    self.next_stone = Stone(cols)
    self.init_game()

  def init_game(self):
    self.new_stone()
    self.board = Board(cols, rows)
    pygame.time.set_timer(pygame.USEREVENT+1, 1000)

  def new_stone(self):
    self.stone = self.next_stone
    self.next_stone = Stone(cols)

  def draw_matrix(self, matrix, offset):
    offx, offy = offset
    for y, row in enumerate(matrix):
      for x, val in enumerate(row):
        if val:
          pygame.draw.rect(
            self.screen,
            colors[val],
            pygame.Rect(
              (offx+x) * cell_size,
              (offy+y) * cell_size,
              cell_size, cell_size),
            0)

  def drop(self, rows = 1):
    self.stone.drop(rows)
    if self.board.check_collision(self.stone):
      self.board.merge_board(self.stone)
      self.new_stone()

  def drop_to_bottom(self):
    while not self.board.check_collision(self.stone):
      self.stone.drop()
    self.board.merge_board(self.stone)
    self.new_stone()

  def rotate_stone(self):
    new_stone = self.stone.rotate_clockwise()
    if not self.board.check_collision(new_stone):
      self.stone = new_stone

  def quit(self):
    pygame.quit()

  def run(self):
    running = True
    clock = pygame.time.Clock()
    while running:
      self.screen.fill((0,0,0))
      self.draw_matrix(self.bground_grid, (0,0))
      self.draw_matrix(self.board.matrix, (0,0))
      self.draw_matrix(self.stone.shape, (self.stone.col, self.stone.row))
      self.draw_matrix(self.next_stone.shape, (cols+1,2))

      pygame.display.update()

      for evt in pygame.event.get():
        if evt.type == pygame.USEREVENT+1:
          self.drop()
        elif evt.type == pygame.QUIT:
          running = False
          self.quit()
        elif evt.type == pygame.KEYDOWN:
          if evt.key == pygame.K_LEFT:
            self.stone.move(-1)
          elif evt.key == pygame.K_RIGHT:
            self.stone.move(1)
          elif evt.key == pygame.K_UP:
            self.rotate_stone()
          elif evt.key == pygame.K_DOWN:
            self.drop()
          elif evt.key == pygame.K_RETURN or evt.key == pygame.K_SPACE:
            self.drop_to_bottom()

      clock.tick(maxfps)

game = TetrisGame()
game.run()