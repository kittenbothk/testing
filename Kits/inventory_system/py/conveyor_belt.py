from future import *
from robotbit import RobotBit
from sugar import *
from time import sleep
from mqttsimple import MQTTClient

id=''
item=''
msg=''
mc_prefix='_dn=,_dsn=,'

koi_count=0
asr_count=0

def probeCallback():
    global koi_count
    global asr_count
    rb.motor(1,1)
    screen.clear()
    id=RFID().uuid()
    print(id)
    screen.text(id,5,40,2,(255,255,255))
    item=RFID().read(1, 1)
    print(item)
    screen.text(item,5,10,2,(255,255,255))
    msg=item+'.'+id
    print(mc_prefix+msg)
    makercloud.publish("",str(mc_prefix+'item='+msg))
    sleep(1)
    if (item=='koi'):
        koi_count+=1
        makercloud.publish("",mc_prefix+'koi_count='+str(koi_count))
    elif (item=='asr'):
        asr_count+=1
        makercloud.publish("",mc_prefix+'asr_count='+str(asr_count))
    rb.motor(1,-50)
    sleep(2)

rb=RobotBit()

wifi.connect('','')
sleep(3)
makercloud=MQTTClient("mqtt.makercloud.io", "clientID")
makercloud.connect()

makercloud.publish("",mc_prefix+'asr_count='+str(asr_count))
sleep(1)
makercloud.publish("",mc_prefix+'koi_count='+str(koi_count))

screen.clear()

while True:
    if sensor.btnValue('a'):
        rb.motor(1,-50)
    if sensor.btnValue('b'):
        rb.motor(1,0)
    RFID().probe(probeCallback if 'probeCallback' in dir() else None)
    sleep(0.2)