# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_state
from logger import log_event 
import sys

def main():
  """
  This function serves as the entry point for the application
  and prints a starting message.
  """
  pygame.init()
  clock = pygame.time.Clock()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()

  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable)

  AsteroidField()

  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  player.add(updatable, drawable)
  
  dt = 0

  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  BLACK = (0, 0, 0)
  number = 5
  while number > 0:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    screen.fill(BLACK)

    updatable.update(dt)

    for asteroid in asteroids:
      if player.collides_with(asteroid):
        log_event("player_hit")
        print("Game over!")
        sys.exit()

    for sprite in drawable:
      sprite.draw(screen)

    pygame.display.flip()
    # limit the frames to 60 per second
    dt = clock.tick(60) / 1000.0
    log_state()
if __name__ == "__main__":
  # This standard Python construct ensures that the main() function is called
  # only when the script is executed directly.
  main()
