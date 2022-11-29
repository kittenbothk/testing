#/bin/python

from time import sleep
from future import *
from sugar import *
import robotbit

x = 0
y = 0


def detect():
  global x,y

  if PIR("P0").value():
    if TOFDistance().value() < 300:
      x = TOFDistance().value()
      sleep(1)
      y = TOFDistance().value()
      if x > y:
        welcome()



def welcome():
  global x,y

  buzzer.melody(CORRECT)
  screen.fill((0, 119, 255))
  screen.textCh("歡迎光臨",30,50,2,(255, 255, 255))
  screen.refresh()
  for count in range(3):
    robot.geekServo2kg(1, 90)
    sleep(0.2)
    robot.geekServo2kg(1, 0)
    sleep(0.2)
  screen.clear()



robot = robotbit.RobotBit()

robot.geekServo2kg(1, 0)

while True:
  detect()


