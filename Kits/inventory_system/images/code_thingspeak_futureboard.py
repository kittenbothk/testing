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
    robotbit_count += 1
    mqtt.publish("channels//publish", str("field1=")+str(robotbit_count))
  else:
    if id in koi_tags:
      koi_count += 1
      mqtt.publish("channels//publish", str("field2=")+str(koi_count))
    else:
      if id in armourbit_tags:
        armourbit_count += 1
        mqtt.publish("channels//publish", str("field3=")+str(armourbit_count))
  sleep(1)
  screen.fill((0, 0, 0))
  screen.text(str("Place RFID Tag"),5,10,1,(0, 119, 255))
  screen.text(str(id),5,30,2,(0, 119, 255))
  screen.refresh()




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

mqtt = mqttsimple.MQTTClient("mqtt3.thingspeak.com", "id",user=str("name"), password=str("password"),port=1883)
mqtt.connect()

screen.sync = 0

screen.fill((0, 0, 0))

screen.text(str("Place RFID Tag"),5,10,1,(0, 119, 255))

screen.refresh()

mqtt.publish("channels//publish", str("field1=")+str(robotbit_count))

sleep(1)

mqtt.publish("channels//publish", str("field2=")+str(koi_count))

sleep(1)

mqtt.publish("channels//publish", str("field3=")+str(armourbit_count))

sleep(1)

while True:
  if sensor.btnValue('a'):
    robot.motor(1,170)
  if sensor.btnValue('b'):
    robot.motor(1,0)
  RFID().probe(probeCallback if 'probeCallback' in dir() else None)
  sleep(0.5)


