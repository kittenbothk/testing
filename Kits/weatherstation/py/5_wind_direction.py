from future import *
from sugar import *
import math

east = 0
south = 0
west = 0
north = 0
angle = 0
direction = 0
light_P1 = Light('P1')


east = 0
south = 0
west = 0
north = 0
screen.sync = 0
screen.fill((0, 0, 0))
while True:
  angle = light_P1.value()
  if (math.fabs(angle - east)) < 30:
    direction = 'EAST'
  if (math.fabs(angle - south)) < 30:
    direction = 'SOUTH'
  if (math.fabs(angle - west)) < 30:
    direction = 'WEST'
  if (math.fabs(angle - north)) < 30:
    direction = 'NORTH'
  screen.text('Direction:',5,10,2,(255, 255, 255))
  screen.text(direction,5,30,2,(255, 255, 255))
