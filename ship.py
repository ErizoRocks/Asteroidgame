import pygame

class Ship(pygame.sprite.Sprite):

  def __init__(self, pos):
    super().__init__()
    self.image = pygame.image.load("RocketImage2.png")
    self.image = pygame.transform.smoothscale(self.image, (30, 65))
    self.image = pygame.transform.rotate(self.image, -90)
    self.rect = self.image.get_rect()
    self.rect.center = pos
    self.health = 100
    self.speed = pygame.math.Vector2(0, 0)

  def update(self):
    self.rect.move_ip(self.speed)