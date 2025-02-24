# Arden Boettcher
# 2/11/25
# Template Config

# Screen size constants
WIDTH = 500
HEIGHT = 500

# Framerate
FPS = 60

# Color Constants

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Offset
OFFSET = (10, 25)

def add(tuple1, tuple2):
  return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])

from random import randint

random_color = lambda: (randint(0, 255), randint(0, 255), randint(0, 255))