#/bin/python

from time import sleep
from future import *
from sugar import *
import robotbit

数字 = 0
位数 = 0
设定密码 = 0
输入密码 = 0
单位密码 = 0
x = 0
y = 0


def indicator():
  global 数字,位数,设定密码,输入密码,单位密码,x,y

  if Joystick().value('x') > 50:
    neopix.setColor(2, (255, 255, 0))
    neopix.update()
    sleep(0.1)
    neopix.setColorAll((0,0,0))
  if Joystick().value('x') < -50:
    neopix.setColor(0, (255, 255, 0))
    neopix.update()
    sleep(0.1)
    neopix.setColorAll((0,0,0))



def valmap(x, in_min, in_max, out_min, out_max):
    return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)


robot = robotbit.RobotBit()

robot.geekServo2kg(1, 90)

neopix=NeoPixel("P7",3)

while True:
  robot.geekServo2kg(1, valmap(Joystick().value('x'), 100, -100, 110, 80))
  robot.motor(1,valmap(Joystick().value('y'), -255, 255, 60, -60))
  indicator()


