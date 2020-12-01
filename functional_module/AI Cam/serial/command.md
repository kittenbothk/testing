# KOI指令API

假如你想使用KOI的指令碼，你可以參照以下列表。

此處提供了Microbit的例子，假如你使用其他主控板請自行修改程式。

## KOI指令列表

### 返回版本號

指令：K0

作用：獲得KOI目前的版本

返回：目前版本號

    from microbit import *
    
    uart.init(baudrate=115200, tx=pin1, rx=pin2)
    uart.write('\n\n')
    sleep(1000)
    uart.write('K0\r\n')
    sleep(100)
    ret_list = []
    
    if uart.any():
        ret = str(uart.readline(), 'UTF-8')
        ret = ret.strip()
        ret_list = ret.split(' ')
        
    if len(ret_list)>1:
        display.scroll(ret_list[1])
        display.scroll(ret_list[2])

### 拍照與顯示圖片

指令：K1 name.jpg

作用：拍照

指令：K2 name.jpg

作用：顯示圖片

    from microbit import *

    uart.init(baudrate=115200, tx=pin1, rx=pin2)
    uart.write('\n\n')
    sleep(1000)

    while True:
        if button_a.is_pressed():
            uart.write('K2 pic.jpg\r\n')
        if button_b.is_pressed():
            uart.write('K1 pic.jpg\r\n')
            
### KOI按鍵

指令：K3

作用：KOI按鍵檢測

返回：A按鍵狀態，B按鍵狀態

    from microbit import *

    uart.init(baudrate=115200, tx=pin1, rx=pin2)
    uart.write('\n\n')
    sleep(1000)
    ret_list = []

    while True:
        uart.write('K3\r\n')
        sleep(1000)
        if uart.any():
            ret = str(uart.readline(), 'UTF-8')
            ret = ret.strip()
            ret_list = ret.split(' ')
        if len(ret_list)>1:
            display.scroll('A:')
            display.scroll(ret_list[1])
            display.scroll('B:')
            display.scroll(ret_list[2])
            
### 顯示字串

指令：K4 x y delay string

作用：在座標(x,y)顯示字串，delay代表時長

    from microbit import *

    uart.init(baudrate=115200, tx=pin1, rx=pin2)
    uart.write('\n\n')
    sleep(1000)
    uart.write('K4 0 0 1000 KOI\r\n')
    
### 改變屏幕方向

指令：K6 direction

作用：以direction改變屏幕方向，0代表前置；1代表橫置；2代表後置

    from microbit import *

    uart.init(baudrate=115200, tx=pin1, rx=pin2)
    uart.write('\n\n')
    sleep(1000)

    while True:
        if button_a.is_pressed() and button_b.is_pressed():
            uart.write('K6 2\r\n')
        if button_a.is_pressed():
            uart.write('K6 0\r\n')
        if button_b.is_pressed():
            uart.write('K6 1\r\n')
            
### 圓形辨認

指令：K10 threshold

作用：辨認圓形，threshold代表臨界值，一般推薦2000(臨界值越高越難辨認，誤差會更少)

返回：X座標，Y座標，半徑

    from microbit import *

    ret_list=[]
    uart.init(baudrate=115200, tx=pin1, rx=pin2)
    uart.write('\n\n')
    sleep(1000)

    while True:
        if button_a.is_pressed():
            uart.write('K10 3000\r\n')
            sleep(1000)
        if uart.any():
            ret = str(uart.readline(), 'UTF-8')
            ret = ret.strip()
            ret_list = ret.split(' ')
            if len(ret_list)>1:
                display.scroll('X:')
                display.scroll(ret_list[1])
                display.scroll('Y:')
                display.scroll(ret_list[2])
                display.scroll('R:')
                display.scroll(ret_list[3])