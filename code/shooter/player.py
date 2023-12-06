from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from pygame import Rect, sprite, Surface
from bullet import Bullet

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
    self.rect = Rect(Player.PLAYER_RECT[0])
    self.rect.topleft = [200, 400]
    self.speed = 8
    self.bullets = sprite.Group()
    self.down_index = 16

  def shoot(self):
    bullet = Bullet(self.full_img, self.rect.midtop)
    self.bullets.add(bullet)

  def move_bullets(self):
    for bullet in self.bullets:
      if bullet.move():
        self.bullets.remove(bullet)

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

  def move_left(self):
    self.rect.left -= self.speed
    if self.rect.left < 0:
      self.rect.left = 0
  
  def move_right(self):
    self.rect.left += self.speed
    if self.rect.left > SCREEN_WIDTH - self.rect.width:
      self.rect.left = SCREEN_WIDTH - self.rect.width

  def draw_down(self, screen):
    screen.blit(self.image[self.down_index // 8], self.rect)
    self.down_index += 1
    return self.down_index > 47