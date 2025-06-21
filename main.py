# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
  """
  This function serves as the entry point for the application
  and prints a starting message.
  """
  pygame.init()
  clock = pygame.time.Clock()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
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
    player.update(dt)
    player.draw(screen)
    pygame.display.flip()
    # limit the frames to 60 per second
    dt = clock.tick(60) / 1000.0
if __name__ == "__main__":
  # This standard Python construct ensures that the main() function is called
  # only when the script is executed directly.
  main()
