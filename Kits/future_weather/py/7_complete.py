from sugar import *
from future import *
import math
from radio import Radio

volume = 0
rainfall = 0
msg = 0
timecount = 0
temp = 0
height = 0
hpa = 0
i = 0
area = 0
distance = 0
speed = 0
flag = 0
light = 0
angle = 0
sum2 = 0
circumference = 0
j = 0
direction = 0
radius = 0
k = 0
depth = 0
env2 = ENV2()
hall_P1 = Hall('P1')
r = Radio()
tofDis = TOFDistance()

def map2(x, in_min, in_max, out_min, out_max):
  return ((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)
def Windspeed():
  global volume,rainfall,msg,timecount,temp,height,hpa,i,area,distance,speed,flag,light,angle,sum2,circumference,j,direction,radius,k,depth
  sleep(0.01)
  timecount += 0.01
  if (int(timecount)) == 5:
    distance = sum2 * circumference
    speed = distance / 5
    timecount = 0
    sum2 = 0
  if hall_P1.value() == 0:
    if bool(flag):
      sum2 += 1
      flag = 0
  else:
    flag = 1

def Rainfall():
  global volume,rainfall,msg,timecount,temp,height,hpa,i,area,distance,speed,flag,light,angle,sum2,circumference,j,direction,radius,k,depth
  rainfall = height - tofDis.value()
  volume = area * (rainfall / 10)
  volume = math.floor(volume) + math.floor((volume % 1) * 100) / 100

def LightDirection():
  global volume,rainfall,msg,timecount,temp,height,hpa,i,area,distance,speed,flag,light,angle,sum2,circumference,j,direction,radius,k,depth
  msg = r.read()
  if bool(msg):
    i = 1
    while not msg[int(i - 1)] == ',':
      i += 1
    light = str()
    j = i + 1
    while not j == len(msg) + 1:
      light = light+msg[int(j - 1)]
      j += 1
    light = str(map2(int(light), 0, 4095, 0, 100))
    direction = str()
    k = 1
    while not k == i:
      direction = direction+msg[int(k - 1)]
      k += 1

def Atmosphere():
  global volume,rainfall,msg,timecount,temp,height,hpa,i,area,distance,speed,flag,light,angle,sum2,circumference,j,direction,radius,k,depth
  env2.update()
  temp = env2.read_temp()[0]
  hpa = env2.read_pres()



# TODO: radioinit
r.channel = 12
screen.sync = 0
while True:
  angle = 0
  flag = 1
  sum2 = 0
  timecount = 0
  radius = 6
  circumference = ((2 * 3.14) * radius) / 100
  height = 140
  area = 8.5 * 8.5
  depth = 0
  volume = 0
  rainfall = 0
  temp = 0
  hpa = 0
  light = 0
  while True:
    Atmosphere()
    Windspeed()
    Rainfall()
    LightDirection()
    screen.fill((0, 0, 0))
    screen.text('Wind:'+str(speed)+'m/s',5,10,1,(255, 255, 255))
    screen.text('Volume: '+str(volume)+'ml',5,20,1,(255, 255, 255))
    screen.text('Rainfall: '+str(rainfall)+'mm',5,30,1,(255, 255, 255))
    screen.text('Temp: '+str(temp)+' C',5,40,1,(255, 255, 255))
    screen.text('hPa: '+str(hpa),5,50,1,(255, 255, 255))
    screen.text('Light:'+str(light),5,60,1,(255, 255, 255))
    screen.text(str(direction),5,70,1,(255, 255, 255))
    screen.refresh()
