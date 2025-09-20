from pygame import *

class GameSprite(sprite.Sprite):
  def __init__(self, p_image, p_x, p_y, p_width, p_height, p_speed):
    super().__init__()

    self.image = transform.scale(image.load(p_image), (p_width, p_height))
    self.speed = p_speed
    self.rect = self.image.get_rect()
    self.rect.x = p_x
    self.rect.y = p_y
  def reset(self, window):
    window.blit(self.image ,(self.rect.x, self.rect.y))

class Player(GameSprite):
  def update_1(self):
    keys = key.get_pressed()
    if keys[K_w] and self.rect.y > 5:
      self.rect.y -= self.speed
    if keys[K_s] and self.rect.y < (500-65):
      self.rect.y += self.speed

  def update_2(self):
    keys = key.get_pressed()
    if keys[K_UP] and self.rect.y >5:
      self.rect.y -= self.speed
    if keys[K_DOWN] and self.rect.y < (500-65):
      self.rect.y += self.speed