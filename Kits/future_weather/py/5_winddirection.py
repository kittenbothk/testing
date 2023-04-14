from future import *

angle = 0
direction = 0


while True:
  angle = sensor.heading()
  if angle > 337 and angle < 23:
    direction = 'north'
  if angle > 22 and angle < 68:
    direction = 'Northeast'
  if angle > 67 and angle < 112:
    direction = 'East'
  if angle > 111 and angle < 158:
    direction = 'Southeast'
  if angle > 157 and angle < 203:
    direction = 'South'
  if angle > 202 and angle < 248:
    direction = 'Southwest'
  if angle > 247 and angle < 293:
    direction = 'West'
  if angle > 292 and angle < 338:
    direction = 'Northwest'
  screen.clear()
  screen.text(str(direction),5,10,2,(255, 255, 255))
  screen.text(str(angle),5,35,2,(255, 255, 255))
  sleep(0.3)
