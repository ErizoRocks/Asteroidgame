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

asteroids = None
asteroid_count = None
player = None

timer = None
score_font = pygame.font.SysFont("truetype", 30)
test = score_font.render('Test', False, (255, 255, 255),(0, 0, 0))

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
    Level = 1
    S = int(json.load(open('game.json', 'rb'))['Speed'])
    S *= int(Level)

    clock.tick(60)
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit(0)
      if event.type == pygame.KEYDOWN:
        if event.key ==   pygame.K_LEFT:
          player.speed[0] = - int(S)
        elif event.key ==   pygame.K_RIGHT:
          player.speed[0] = +int(S)
        elif event.key ==   pygame.K_DOWN:
          player.speed[1] = + int(S)
        elif event.key ==   pygame.K_UP:
          player.speed[1] = -int(S)  
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
    screen.blit(test, (30, 30))
    pygame.display.update()

if __name__ == '__main__':
  main()



