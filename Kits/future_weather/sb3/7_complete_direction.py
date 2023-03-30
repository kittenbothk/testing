from future import *
from radio import Radio

r = Radio()

direction = 0
light = 0
angle = 0


direction = 0
r = Radio()
r.channel = 12
screen.sync = 0
while True:
  light = sensor.getLight()
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
  screen.fill((0, 0, 0))
  screen.text((str(direction)),5,10,2,(255, 255, 255))
  screen.text(('Angle:'+str(angle)),5,35,2,(255, 255, 255))
  screen.text(('Light:'+str(light)),5,60,2,(255, 255, 255))
  screen.refresh()
  r.send((str(direction)+str(',')+str(light)))
  sleep(0.3)
