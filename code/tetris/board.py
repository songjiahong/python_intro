from stone import Stone

class Board:
  def __init__(self, col_size, row_size):
    self.col_size = col_size
    self.matrix = [[0 for x in range(col_size)] for y in range(row_size)]
    self.matrix += [[ 1 for x in range(col_size)]]

  def check_collision(self, stone: Stone):
    for cy, row in enumerate(stone.shape):
      for cx, cell in enumerate(row):
        try:
          if cell and self.matrix[ cy + stone.row ][ cx + stone.col ]:
            return True
        except IndexError:
          return True
    return False
  
  def is_row_full(self, row):
    for x in range(self.col_size):
      if not self.matrix[row][x]:
        return False
    return True

  def is_row_empty(self, row):
    for x in range(self.col_size):
      if self.matrix[row][x]:
        return False
    return True
  
  def remove_row(self, row):
    current_row = row
    while current_row > 1:
      if self.is_row_empty(current_row - 1):
        break
      self.matrix[current_row] = self.matrix[current_row -1][:]
      current_row -= 1

  def merge_board(self, stone: Stone):
    full_rows = []
    for cy, row in enumerate(stone.shape):
      for cx, val in enumerate(row):
        self.matrix[cy+stone.row-1][cx+stone.col] += val
      if self.is_row_full(cy+stone.row-1):
        full_rows.append(cy+stone.row-1)
    if len(full_rows) > 0:
      for row in full_rows:
        self.remove_row(row)