from sugar import *
from future import *
import math
import time

rainfall = 0
timeOut = 0
light = 0
angle = 0
volume = 0
temp = 0
flag = 0
height = 0
distance = 0
hpa = 0
sum2 = 0
direction = 0
area = 0
speed = 0
radius = 0
timeIn = 0
circumference = 0
north = 0
west = 0
depth = 0
south = 0
east = 0
southeast = 0
southwest = 0
northwest = 0
northeast = 0
env2 = ENV2()
hall_P1 = Hall('P1')
light_P0 = Light('P0')
tofDis = TOFDistance()

def setUp():
  global rainfall,timeOut,light,angle,volume,temp,flag,height,distance,hpa,sum2,direction,area,speed,radius,timeIn,circumference,north,west,depth,south,east,southeast,southwest,northwest,northeast
  angle = 0
  flag = True
  sum2 = 0
  radius = 6
  circumference = ((2 * 3.14) * radius) / 100
  height = 135
  area = 8.5 * 8.5
  depth = 0
  volume = 0
  rainfall = 0
  temp = 0
  hpa = 0
  light = 0
  east = 140
  southeast = 320
  south = 490
  southwest = 624
  west = 670
  northwest = 710
  north = 760
  northeast = 830
  timeIn = time.ticks_ms()

def direction():
  global rainfall,timeOut,light,angle,volume,temp,flag,height,distance,hpa,sum2,direction,area,speed,radius,timeIn,circumference,north,west,depth,south,east,southeast,southwest,northwest,northeast
  angle = light_P0.value()
  if (math.fabs(angle - north)) < 30:
    direction = 'North'
  if (math.fabs(angle - west)) < 30:
    direction = 'West'
  if (math.fabs(angle - south)) < 30:
    direction = 'South'
  if (math.fabs(angle - east)) < 30:
    direction = 'East'

def Windspeed():
  global rainfall,timeOut,light,angle,volume,temp,flag,height,distance,hpa,sum2,direction,area,speed,radius,timeIn,circumference,north,west,depth,south,east,southeast,southwest,northwest,northeast
  timeOut = time.ticks_ms()
  if (timeOut - timeIn) >= 5000:
    distance = sum2 * circumference
    speed = distance / 5
    timeIn = time.ticks_ms()
    sum2 = 0
  if hall_P1.value() == 0:
    flag = True
  if not hall_P1.value() == 0:
    if bool(flag):
      sum2 += 1
      flag = False

def Rainfall():
  global rainfall,timeOut,light,angle,volume,temp,flag,height,distance,hpa,sum2,direction,area,speed,radius,timeIn,circumference,north,west,depth,south,east,southeast,southwest,northwest,northeast
  rainfall = height - tofDis.value()
  volume = area * (rainfall / 10)
  volume = math.floor(volume) + math.floor((volume % 1) * 100) / 100

def LightDirection():
  global rainfall,timeOut,light,angle,volume,temp,flag,height,distance,hpa,sum2,direction,area,speed,radius,timeIn,circumference,north,west,depth,south,east,southeast,southwest,northwest,northeast
  light = sensor.getLight()

def Atmosphere():
  global rainfall,timeOut,light,angle,volume,temp,flag,height,distance,hpa,sum2,direction,area,speed,radius,timeIn,circumference,north,west,depth,south,east,southeast,southwest,northwest,northeast
  env2.update()
  temp = env2.read_temp()[0]
  hpa = env2.read_pres()



setUp()
screen.sync = 0
while True:
  Atmosphere()
  Windspeed()
  Rainfall()
  LightDirection()
  direction()
  screen.fill((0, 0, 0))
  screen.text('Wind:'+str(speed)+'m/s',5,10,1,(255, 255, 255))
  screen.text('Volume: '+str(volume)+'ml',5,20,1,(255, 255, 255))
  screen.text('Rainfall: '+str(rainfall)+'mm',5,30,1,(255, 255, 255))
  screen.text('Temp: '+str(temp)+' C',5,40,1,(255, 255, 255))
  screen.text('hPa: '+str(hpa),5,50,1,(255, 255, 255))
  screen.text('Light:'+str(light),5,60,1,(255, 255, 255))
  screen.text(direction,5,70,1,(255, 255, 255))
  screen.refresh()
