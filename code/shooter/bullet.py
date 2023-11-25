from pygame import mixer,Rect, sprite, Surface

class Bullet(sprite.Sprite):

  def __init__(self, full_img: Surface, init_pos):
    sprite.Sprite.__init__(self)
    self.image = full_img.subsurface(Rect(1004, 987, 9, 21)).convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.midbottom = init_pos
    self.speed = 10
    BULLET_SOUND = mixer.Sound('resources/sound/bullet.wav')
    BULLET_SOUND.set_volume(0.3)
    BULLET_SOUND.play()

  def move(self):
    self.rect.top -= self.speed
    return self.rect.bottom < 0
