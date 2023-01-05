from time import sleep
from future import *
from sugar import *
def probeCallback():
  global x
    
  screen.fill((0, 0, 0))
  screen.text(str("Place RFID Tag"),5,10,1,(0, 119, 255))
  screen.text(str(RFID().uuid()),5,30,2,(0, 119, 255))
  screen.refresh()

x = 0

screen.sync = 0

screen.fill((0, 0, 0))

screen.text(str("Place RFID Tag"),5,10,1,(0, 119, 255))

screen.refresh()

sleep(1)

while True:
  RFID().probe(probeCallback if 'probeCallback' in dir() else None)
  sleep(0.2)