import pygame
import pandas
import sys
from pygame.locals import *
from ship import Ship
from asteroid import Asteroid
import random
import json
import time

pygame.init()
screen_info = pygame.display.Info()
width = screen_info.current_w
height = screen_info.current_h
size = (width, height)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
clock = pygame.time.Clock()
# player = Ship((width // 2, height // 2))
# asteroids = pygame.sprite.Group()
# asteroid_count = 8
asteroids = None
asteroid_count = None
player = None


def init():
  global asteroid_count
  global asteroids
  global player
  player = Ship((width // 2, height // 2))
  asteroids = pygame.sprite.Group()
  asteroid_count = 8
  asteroids.empty()
  for i in range (asteroid_count):
    ran_x = random.randint(50, width - 50)
    ran_y = random.randint(50, height - 50)
    ran_size = random.randint(15, 120)
    asteroids.add(Asteroid((ran_x, ran_y), ran_size))

def main():
  init()
  while True:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit(0)
      if event.type == pygame.KEYDOWN:
        if event.key ==   pygame.K_LEFT:
          player.speed[0] = -2
        elif event.key ==   pygame.K_RIGHT:
          player.speed[0] = +2
        elif event.key ==   pygame.K_DOWN:
          player.speed[1] = 2
        elif event.key ==   pygame.K_UP:
          player.speed[1] = -2  
      if event.type == pygame.KEYUP:
        if event.key ==   pygame.K_LEFT:
          player.speed[0] = 0  
        elif event.key ==   pygame.K_RIGHT:
          player.speed[0] = 0 
        elif event.key ==   pygame.K_DOWN:
          player.speed[1] = 0
        elif event.key ==   pygame.K_UP:
          player.speed[1] = 0      
    screen.fill((0, 0, 0))
    player.update()
    asteroids.update()
    asteroids.draw(screen)
    was_hit = pygame.sprite.spritecollide(player, asteroids, True)
    if was_hit:
      print("Oh no! The ship was hit!!!")
      player.health -= 20
      Heartsremaining = player.health // 20
      print("One heart lost. You have", Heartsremaining, "/5 hearts remaining.")
      if player.health == 0:
        print("Game over. :(")
        print("Restarting...")
        time.sleep(3)
        init()
      
    screen.blit(player.image, player.rect)
    pygame.display.update()

if __name__ == '__main__':
  main()


#  {
#  "player": {"Level1":{"health": 40, "speed": 2},"Level2":{"health": 100, "speed": 5},"Level3":{"health": 200, "speed": 10}}, "asteroid":{"damage": 20}
#  }