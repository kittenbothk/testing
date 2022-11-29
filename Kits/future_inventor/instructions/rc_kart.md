# 無人小車

![](../images/car.jpg)

模擬一部小車，可以使用搖桿控制或者利用物聯網控制。

## 組裝說明書

[組裝說明書下載(右鍵->另存為)](https://github.com/kittenbothk/kittenbothk/raw/master/Kits/future_inventor/instructions/pdf/rc_kart.pdf)

## 參考接線

![](../images/rc_kart_wire.png)

### 參考程式

### KittenBlock參考程式

![](../images/rc_kart_code.png)

[參考程式下載(右鍵->另存為)](https://github.com/kittenbothk/kittenbothk/raw/master/Kits/future_inventor/instructions/sb3/rc%20kart.sb3)

### Python參考程式

    #/bin/python
    
    from time import sleep
    from future import *
    from sugar import *
    import robotbit

    x = 0
    y = 0
    
    
    def indicator():
      global x,y
    
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

[參考程式下載(右鍵->另存為)](https://github.com/kittenbothk/kittenbothk/raw/master/Kits/future_inventor/instructions/py/kart.py)

## 模型玩法

1. 使用搖桿控制小車