from constants import SCREEN_HEIGHT
from pygame import mixer, Rect, sprite, Surface

class Enemy(sprite.Sprite):
  DOWN_SOUND = mixer.Sound('resources/sound/enemy1_down.wav')
  DOWN_SOUND.set_volume(0.3)

  def __init__(self, full_img: Surface, init_pos):
    sprite.Sprite.__init__(self)
    enemy_down_imgs = []
    enemy_down_imgs.append(full_img.subsurface(Rect(267, 347, 57, 43)))
    enemy_down_imgs.append(full_img.subsurface(Rect(873, 697, 57, 43)))
    enemy_down_imgs.append(full_img.subsurface(Rect(267, 296, 57, 43)))
    enemy_down_imgs.append(full_img.subsurface(Rect(930, 697, 57, 43)))
    self.image = full_img.subsurface(Rect(534, 612, 57, 43)).convert_alpha()
    self.down_imgs = enemy_down_imgs
    self.rect = self.image.get_rect()
    self.rect.topleft = init_pos
    self.speed = 2
    self.down_index = 0

  def move(self):
    self.rect.top += self.speed
    return self.rect.top > SCREEN_HEIGHT

  def draw_down(self, screen):
    screen.blit(self.down_imgs[self.down_index // 2], self.rect)
    self.down_index += 1
    if self.down_index == 1:
      Enemy.DOWN_SOUND.play()
    return True if self.down_index > 7 else False

