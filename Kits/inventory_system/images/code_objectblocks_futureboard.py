#/bin/python

from time import sleep
from future import *
from sugar import *
import mqttsimple
import robotbit
def probeCallback():
  global id,robotbit_count,koi_count,armourbit_count,msg

  id = RFID().uuid()
  if id in robotbit_tags:
    msg = "Robotbit."
    robotbit_count += 1
    mqtt.publish("/topic", robotbit_count)
  else:
    if id in koi_tags:
      msg = "KOI."
      koi_count += 1
      mqtt.publish("/topic", koi_count)
    else:
      if id in armourbit_tags:
        msg = "ArmourBit."
        armourbit_count += 1
        mqtt.publish("/topic", armourbit_count)
  sleep(1)
  screen.fill((0, 0, 0))
  screen.text(str("Place RFID Tag"),5,10,1,(0, 119, 255))
  screen.text(str(id),5,30,2,(0, 119, 255))
  screen.refresh()
  mqtt.publish("/topic", str(msg)+str(id))




id = 0
robotbit_count = 0
koi_count = 0
armourbit_count = 0
msg = 0
robotbit_tags = []
koi_tags = []
armourbit_tags = []



robotbit_tags.append("rfid")

koi_tags.append("rfid")

armourbit_tags.append("rfid")

armourbit_count = 0

koi_count = 0

robotbit_count = 0

robot = robotbit.RobotBit()

screen.sync = 1

wifi.connect(str("name"), "pwd")

mqtt = mqttsimple.MQTTClient("hub2.objectblocks.cc", "id",user=str("name"), password=str("password"),port=1883)
mqtt.connect()

screen.sync = 0

screen.fill((0, 0, 0))

screen.text(str("Place RFID Tag"),5,10,1,(0, 119, 255))

screen.refresh()

mqtt.publish("/topic", robotbit_count)

sleep(1)

mqtt.publish("/topic", koi_count)

sleep(1)

mqtt.publish("/topic", armourbit_count)

sleep(1)

while True:
  if sensor.btnValue('a'):
    robot.motor(1,170)
  if sensor.btnValue('b'):
    robot.motor(1,0)
  RFID().probe(probeCallback if 'probeCallback' in dir() else None)
  sleep(0.5)


