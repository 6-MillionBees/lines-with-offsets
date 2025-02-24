# Arden Boettcher
# 2/11/25
# Pygame Template

import pygame
import config
pygame.init()


# Setting up the window
screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption("PLACEHOLDER")

# Setting up the clock
clock = pygame.time.Clock()

# Event handling
def main_events():
  for event in pygame.event.get():
    # Quits the game when you press the x
    if event.type == pygame.QUIT:
      return False
  return True


def draw_offset_lines(surface, color, start_pos, end_pos, offset, weight, num_of_lines):
  for x in range(num_of_lines):
    pygame.draw.line(surface, color, start_pos, end_pos, weight)
    start_pos = config.add(start_pos, offset)
    end_pos = config.add(end_pos, offset)


# Main loop
def main():
  # The bool for the main loop
  running = True

  while running:

    # Call events / update running
    running = main_events()

    # Fills window
    screen.fill(config.WHITE)

    # Draws lines
    draw_offset_lines(screen, config.BLUE, (20, 50), (30, 5), config.OFFSET, 2, 10)

    # Updates the Display
    pygame.display.flip()

    # Limits the framerate
    clock.tick(config.FPS)

  # Close the pygame modules
  pygame.quit()


# Calls the code
if __name__ == "__main__":
  main()
