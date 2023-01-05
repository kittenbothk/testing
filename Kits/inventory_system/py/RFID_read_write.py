from future import *
import sugar
from time import sleep

rfid = sugar.RFID()

while 1:
    if sensor.btnValue('a'):
        rfid.write(1, 1, 'ITEM')
        sleep(1)
    elif sensor.btnValue('b'):
        print(rfid.read(1, 1))
        sleep(1)
