#/bin/python

from time import sleep
from future import *
from sugar import *
import robotbit

angle = 0
end_time = 0
z = 0


def countdown():
  global angle,end_time,z

  if sensor.btnValue('a'):
    LED("P1").state('ON')
    LED("P2").state('OFF')
    while not (end_time == 0):
      sleep(1)
      end_time += -1
      angle += 1
      screen.clear()
      screen.fill((0, 0, 0))
      screen.textCh(str(end_time)+str("min"),5,10,2,(0, 255, 0))
      screen.refresh()
      robot.geekServo2kg(1, angle * 12)
      if end_time == 0:
        LED("P1").state('OFF')
        LED("P2").state('ON')
        while not sensor.btnValue('b'):
          buzzer.melody(CORRECT)
          sleep(0.2)
    LED("P1").state('OFF')
    LED("P2").state('OFF')



def valmap(x, in_min, in_max, out_min, out_max):
    return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)


robot = robotbit.RobotBit()

screen.sync = 0

LED("P1").state('OFF')

LED("P2").state('OFF')

while True:
  angle = (round(valmap(Angle("P0").value(), 0, 4095, 180, 0) / 12))
  end_time = (round(valmap(Angle("P0").value(), 0, 4095, 0, 15)))
  robot.geekServo2kg(1, angle * 12)
  screen.fill((0, 0, 0))
  screen.textCh(str(end_time)+str("min"),5,10,2,(255, 0, 0))
  screen.refresh()
  countdown()


