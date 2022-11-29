# 智慧停車場

模擬智能停車場，自動打開閘門讓汽車駛進或駛出，自動檢測停車場的空位數量。

![](../images/parking.jpg)

## 組裝說明書

[組裝說明書下載(右鍵->另存為)](https://github.com/kittenbothk/kittenbothk/raw/master/Kits/future_inventor/instructions/pdf/parking.pdf)

## 參考接線

![](../images/parking_wire.png)

## 參考程式

### KittenBlock參考程式

![](../images/parking_code.png)

[參考程式下載(右鍵->另存為)](https://github.com/kittenbothk/kittenbothk/raw/master/Kits/future_inventor/instructions/sb3/parking.sb3)

### Python參考程式

    #/bin/python

    from time import sleep
    from future import *
    from sugar import *
    import robotbit
    import time
    
    x = 0
    last_state = 0
    curr_state = 0
    start_time = 0
    end_time = 0
    time = 0
    
    
    
    last_state = Tracker("P2").value() == 1
    
    curr_state = Tracker("P2").value() == 1
    
    start_time = 0
    
    end_time = 0
    
    robot = robotbit.RobotBit()
    
    robot.geekServo2kg(1, 180)
    
    screen.clear()
    
    screen.text(str("Parking Available"),5,10,1,(0, 119, 255))
    
    LED("P0").state('OFF')
    
    LED("P1").state('ON')
    
    while True:
      curr_state = Tracker("P2").value() == 1
      if not last_state == curr_state:
        if curr_state == 1 and last_state == 0:
          end_time = time.ticks_ms()
          robot.geekServo2kg(1, 90)
          buzzer.melody(NOTICE)
          screen.clear()
          time = (round((end_time - start_time) / 1000))
          screen.text(str(str("Time: ")+str(time)),5,10,2,(0, 119, 255))
          screen.text(str(str("Fee: ")+str(time * 10)),5,30,2,(0, 119, 255))
          screen.text(str("Thank You"),5,50,2,(0, 119, 255))
          sleep(5)
          robot.geekServo2kg(1, 180)
        if curr_state == 0 and last_state == 1:
          start_time = time.ticks_ms()
          buzzer.melody(POWER_UP)
        last_state = curr_state
        if curr_state == 1:
          screen.clear()
          screen.text(str("Parking Available"),5,10,1,(0, 119, 255))
          LED("P0").state('OFF')
          LED("P1").state('ON')
        else:
          screen.clear()
          screen.text(str("Not Available"),5,10,1,(0, 119, 255))
          LED("P0").state('ON')
          LED("P1").state('OFF')
      else:
        if TOFDistance().value() < 50 and curr_state == 1:
          robot.geekServo2kg(1, 90)
          buzzer.melody(BA_DING)
          sleep(5)
          robot.geekServo2kg(1, 180)

[參考程式下載(右鍵->另存為)](https://github.com/kittenbothk/kittenbothk/raw/master/Kits/future_inventor/instructions/py/parking.py)


## 模型玩法

將小車放到閘門前，閘門就會打開。將小車泊到泊車位，門口的紅色LED會亮起。

當停車位已滿，閘門就不會打開讓其他車駛入。將車子駛離泊車位，閘門就會自動打開並且計算泊車費用。