import pygame
import pandas
import sys
from pygame.locals import QUIT
from ship import Ship
from asteroid import Asteroid
import random
import time
from timercode import Timer

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
game_font = pygame.font.SysFont("truetype", 50)
level = 1
player_speed = None
level_image = None


def init():
  global asteroid_count
  global asteroids
  global player
  global timer
  global player_speed
  global level_image
  level_image = game_font.render(str(level), False, (244,123,116), (0, 0, 0))
  player_speed = level * 2
  player = Ship((width // 2, height // 2))
  asteroids = pygame.sprite.Group()
  timer = Timer(20*level)
  asteroid_count = level * 5
  asteroids.empty()
  for i in range (asteroid_count):
    ran_x = random.randint(50, width - 50)
    ran_y = random.randint(50, height - 50)
    ran_size = random.randint(15, 60*level - level*10)
    asteroids.add(Asteroid((ran_x, ran_y), ran_size))

def main():
  init()
  global level
  while True:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit(0)
      if event.type == pygame.KEYDOWN:
        if event.key ==   pygame.K_LEFT:
          player.speed[0] = -player_speed
        elif event.key ==   pygame.K_RIGHT:
          player.speed[0] =  player_speed
        elif event.key ==   pygame.K_DOWN:
          player.speed[1] =  player_speed
        elif event.key ==   pygame.K_UP:
          player.speed[1] = -player_speed
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
    if level == 5:
      Finalmessage = "You win! Game over!!!!!"
      Finalmessage_image = game_font.render(Finalmessage, False, (244,123,116), (0, 0, 0))  
      screen.blit(Finalmessage_image, (width //2, height //2))
      time.sleep(5)
      quit()
    if timer.is_finished():
      print("Level passed!")
      level += 1
      init()
    if was_hit:
      print("Oh no! The ship was hit!!!")
      player.health -= 20
      Heartsremaining = player.health // 20
      print("One heart lost. You have", Heartsremaining, "/5 hearts remaining.")
      if player.health == 0:
        print("Game over. :(")
        print("Restarting...")
        level = 1
        time.sleep(3)
        init()
      
    screen.blit(player.image, player.rect)
    screen.blit(timer.get_image(game_font), (30, 30))
    screen.blit(level_image, (width - 30, 30))
    pygame.display.update()

if __name__ == '__main__':
  main()



