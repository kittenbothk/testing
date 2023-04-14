from sugar import *
from future import *

temp = 0
hpa = 0
env2 = ENV2()


while True:
  env2.update()
  temp = env2.read_temp()[0]
  hpa = env2.read_pres()
  screen.clear()
  screen.text('temp:',5,10,1,(255, 255, 255))
  screen.text(str(temp),5,35,1,(255, 255, 255))
  screen.text('hpa:',5,60,1,(255, 255, 255))
  screen.text(str(hpa),5,85,1,(255, 255, 255))
  screen.refresh()
