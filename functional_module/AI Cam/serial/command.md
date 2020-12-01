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
                
### 矩形辨認

指令：K11 threshold

作用：辨認矩形，threshold代表臨界值，一般推薦6000(臨界值越高越難辨認，誤差會更少)

返回：X座標，Y座標，長，闊

    from microbit import *

    ret_list=[]
    uart.init(baudrate=115200, tx=pin1, rx=pin2)
    uart.write('\n\n')
    sleep(1000)

    while True:
        if button_a.is_pressed():
            uart.write('K11 6000\r\n')
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
                display.scroll('W:')
                display.scroll(ret_list[3])
                display.scroll('H:')
                display.scroll(ret_list[4])
                
### 線條追蹤

指令：K16 color

作用：追蹤線條前必須要校正顏色，color代表校正的顏色，可以隨意更改

指令：K12 color

作用：追蹤線條

返回：X1座標，Y1座標，X2座標，Y2座標，color代表追蹤的顏色，可以隨意更改

    from microbit import *

    ret_list=[]
    uart.init(baudrate=115200, tx=pin1, rx=pin2)
    uart.write('\n\n')
    sleep(1000)
    flag=False

    while True:
        if button_a.is_pressed():
            uart.write('K16 test\r\n')
            sleep(2000)
            flag=True
        if flag:
            uart.write('K12 test\r\n')
            sleep(500)
            if uart.any():
                ret = str(uart.readline(), 'UTF-8')
                ret = ret.strip()
                ret_list = ret.split(' ')
                if len(ret_list)>1:
                    display.scroll('X1:')
                    display.scroll(ret_list[1])
                    display.scroll('Y1:')
                    display.scroll(ret_list[2])
                    display.scroll('X2:')
                    display.scroll(ret_list[3])
                    display.scroll('Y2:')
                    display.scroll(ret_list[4])
                sleep(2000)

### 顏色追蹤

指令：K16

作用：追蹤顏色前必須要校正顏色

指令：K15

作用：追蹤顏色

返回：X座標，Y座標，長，闊

    from microbit import *

    ret_list=[]
    uart.init(baudrate=115200, tx=pin1, rx=pin2)
    uart.write('\n\n')
    sleep(1000)
    flag=False

    while True:
        if button_a.is_pressed():
            uart.write('K16 test\r\n')
            sleep(2000)
            flag=True
        if flag:
            uart.write('K15 test\r\n')
            sleep(500)
            if uart.any():
                ret = str(uart.readline(), 'UTF-8')
                ret = ret.strip()
                ret_list = ret.split(' ')
                if len(ret_list)>1:
                    display.scroll('X:')
                    display.scroll(ret_list[1])
                    display.scroll('Y:')
                    display.scroll(ret_list[2])
                    display.scroll('W:')
                    display.scroll(ret_list[3])
                    display.scroll('H:')
                    display.scroll(ret_list[4])
                sleep(2000)
                
### 辨識二維碼，條碼

指令：K20

作用：辨識二維碼

返回：內容

指令：K22

作用：辨識條碼

返回：內容

    from microbit import *
    
    ret_list=[]
    uart.init(baudrate=115200, tx=pin1, rx=pin2)
    uart.write('\n\n')
    sleep(1000)
    
    while True:
        if button_a.is_pressed():
            uart.write('K20\r\n')
            sleep(500)
        if button_b.is_pressed():
            uart.write('K22\r\n')
            sleep(500)
        if uart.any():
            ret = str(uart.readline(), 'UTF-8')
            ret = ret.strip()
            ret_list = ret.split(' ')
            if len(ret_list)>1:
                display.scroll(ret_list[1])
                ret_list=[]

### 人臉追蹤

指令：K30

作用：加載人臉模型，必須加載才可以追蹤人臉

指令：K31

作用：人臉追蹤

返回：人臉X，Y

    from microbit import *
    
    ret_list=[]
    uart.init(baudrate=115200, tx=pin1, rx=pin2)
    uart.write('\n\n')
    uart.write('K6 0\r\n')
    uart.write('K30\r\n')
    sleep(1000)
    
    while True:
        if button_a.is_pressed():
            uart.write('K31\r\n')
            sleep(500)
        if uart.any():
            ret = str(uart.readline(), 'UTF-8')
            ret = ret.strip()
            ret_list = ret.split(' ')
            if len(ret_list)>1:
                display.scroll('X')
                display.scroll(ret_list[1])
                display.scroll('Y')
                display.scroll(ret_list[2])
                ret_list=[]
                     
### 分類器

指令：K40

作用：初始化模型分類器

指令：K41 className

作用：特徵提取，className代表這物件的名字

指令：K42

作用：特徵辨認

返回：className
    
    from microbit import *
    
    ret_list=[]
    uart.init(baudrate=115200, tx=pin1, rx=pin2)
    uart.write('\n\n')
    uart.write('K40\r\n')
    sleep(1000)
    
    while True:
        if button_a.is_pressed() and button_b.is_pressed():
            uart.write('K42\r\n')
            sleep(500)
        if button_b.is_pressed():
            uart.write('K41 rock\r\n')
            sleep(500)
        if button_b.is_pressed():
            uart.write('K41 paper\r\n')
            sleep(500)
        if uart.any():
            ret = str(uart.readline(), 'UTF-8')
            ret = ret.strip()
            ret_list = ret.split(' ')
            if len(ret_list)>1:
                display.scroll(ret_list[1])
                ret_list=[]

指令：K43 name.json

作用：儲存模型分類器，可以儲存為json或bin

指令：K44 name

作用：載入分類器                