from future import *
from sugar import *

flag = 0
sum2 = 0
x = 0
radius = 0
circumference = 0
distance = 0
speed = 0
hall_P1 = Hall('P1')


screen.sync = 0
flag = 1
sum2 = 0
x = 0
radius = 6
circumference = ((2 * 3.14) * radius) / 100
while True:
  sleep(0.01)
  x += 0.01
  if (int(x)) == 5:
    distance = sum2 * circumference
    speed = distance / 5
    screen.fill((0, 0, 0))
    screen.text(str(speed)+'m/s',5,10,2,(255, 255, 255))
    screen.refresh()
    x = 0
    sum2 = 0
  if hall_P1.value() == 0:
    if bool(flag):
      sum2 += 1
      flag = 0
  else:
    flag = 1
