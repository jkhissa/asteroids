# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
  """
  This function serves as the entry point for the application
  and prints a starting message.
  """
  pygame.init()
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  BLACK = (0, 0, 0)
  number = 5
  while number > 0:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    screen.fill(BLACK)
    pygame.display.flip()

if __name__ == "__main__":
  # This standard Python construct ensures that the main() function is called
  # only when the script is executed directly.
  main()
