from random import randrange as rand

class Stone:
  # Define the shapes of the single parts, the value inside is the color index
  SHAPES = [
    [[2, 2, 2, 2]],
    [[3, 3, 3], [0, 3, 0]],
    [[0, 4, 4], [4, 4, 0]],
    [[5, 5, 0], [0, 5, 5]],
    [[6, 0, 0], [6, 6, 6]],
    [[0, 0, 7], [7, 7, 7]],
    [[8, 8], [8, 8]]
  ]

  def __init__(self, col_size, shape = None, col = None, row = None):
    self.shape = Stone.SHAPES[rand(len(Stone.SHAPES))][:] if shape == None else shape
    self.col_size = col_size
    self.col = int(col_size / 2 - len(self.shape[0]) / 2) if col == None else col
    self.row = 0 if row == None else row

  def drop(self, rows = 1):
    self.row += rows

  def move(self, delta_col):
    col = self.col + delta_col
    if col < 0:
      col = 0
    elif col > self.col_size - len(self.shape[0]):
      col = self.col_size - len(self.shape[0])
    self.col = col

  def rotate_clockwise(self):
    shape = [[self.shape[y][x]
      for y in range(len(self.shape))]
      for x in range(len(self.shape[0]) - 1, -1, -1)]
    return Stone(self.col_size, shape, self.col, self.row)