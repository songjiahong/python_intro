from pygame import Rect, sprite, Surface

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 600

class Player(sprite.Sprite):
  PLAYER_RECT = []
  PLAYER_RECT.append(Rect(0,99,102,126))
  PLAYER_RECT.append(Rect(165,360,102,126))
  PLAYER_RECT.append(Rect(165,234,102,126))
  PLAYER_RECT.append(Rect(330,624,102,126))
  PLAYER_RECT.append(Rect(330,498,102,126))
  PLAYER_RECT.append(Rect(432,624,102,126))

  def __init__(self, full_img: Surface):
    sprite.Sprite.__init__(self)
    self.full_img = full_img
    self.image = []
    for i in range(len(Player.PLAYER_RECT)):
      self.image.append(full_img.subsurface(Player.PLAYER_RECT[i]).convert_alpha())
    self.rect = Player.PLAYER_RECT[0]
    self.rect.topleft = [200, 400]
    self.speed = 8

  def draw(self, screen, index):
    screen.blit(self.image[index], self.rect)

  def move_up(self):
    self.rect.top -= self.speed
    if self.rect.top < 0:
      self.rect.top = 0
  
  def move_down(self):
    self.rect.top += self.speed
    if self.rect.top > SCREEN_HEIGHT - self.rect.height:
      self.rect.top = SCREEN_HEIGHT - self.rect.height