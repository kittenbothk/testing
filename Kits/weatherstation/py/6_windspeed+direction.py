from future import *
from sugar import *

angle = 0
flag = 0
sum2 = 0
x = 0
radius = 0
circumference = 0
direction = 0
distance = 0
speed = 0
hall_P1 = Hall('P1')


screen.sync = 0
angle = 0
flag = 1
sum2 = 0
x = 0
radius = 6
circumference = ((2 * 3.14) * radius) / 100
direction = 'North'
while True:
  sleep(0.01)
  x += 0.01
  if (int(x)) == 5:
    distance = sum2 * circumference
    speed = distance / 5
    x = 0
    sum2 = 0
  if hall_P1.value() == 0:
    if bool(flag):
      sum2 += 1
      flag = 0
  else:
    flag = 1
  angle = sensor.heading()
  if angle > 337 and angle < 23:
    direction = 'North'
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
  screen.fill((0, 0, 0))
  screen.text(str(speed)+'m/s',5,10,2,(255, 255, 255))
  screen.text(str(direction),5,35,2,(255, 255, 255))
  screen.text(str(angle),5,60,2,(255, 255, 255))
  screen.refresh()
