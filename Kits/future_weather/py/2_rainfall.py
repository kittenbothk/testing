from future import *
from sugar import *

height = 0
area = 0
depth = 0
volume = 0
rainfall = 0
tofDis = TOFDistance()


height = 19.0
area = 8.5 * 8.5
while True:
  depth = height - tofDis.value() / 10
  volume = area * depth
  rainfall = (volume / area) / 10
  screen.clear()
  screen.text('depth:',5,10,1,(255, 255, 255))
  screen.text(depth+'cm',5,30,1,(255, 255, 255))
  screen.text('volume:',5,50,1,(255, 255, 255))
  screen.text(volume+'ml',5,70,1,(255, 255, 255))
  screen.text('rainfall:',5,90,1,(255, 255, 255))
  screen.text(rainfall+'mm',5,110,1,(255, 255, 255))
  sleep(0.3)
