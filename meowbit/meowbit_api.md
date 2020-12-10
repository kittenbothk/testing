# Meowbit MicroPython API

這裡集合了Meowbit的MicroPython API的講解。

## 導入Meowbit庫

需要先導入Meowbit庫才可以使用Meowbit的硬件。

    from meowbit import *
    
## Meowbit文字列印

Meowbit可以列出英文和中文。

### 列出英文

    screen.text(text, x=0, y=0, ext=1, color=255)

在屏幕上顯示英文。
    
- 座標為文字的左上角，不設置的話默認為(0，0)。
- ext為文字的大小，默認為1=8x8像素。ext為2的話文字大小為16x16像素，如此類推。
- color代表顏色，採用RGB格式。

### 列出中文

    screen.textCh(text, x=0, y=0, ext=1, color=255)

在屏幕上顯示中文。

- 座標為文字的左上角，不設置的話默認為(0，0)。
- ext為文字的大小，默認為1=12x12像素。ext為2的話文字大小為24x24像素，如此類推。
- color代表顏色，採用RGB格式。

### 使用範例

    from meowbit import *
    
    screen.text('hello world')
    
    screen.textCh('你好世界', x=30, y=20, ext=2, color=(0,0,255))
    
    
## Meowbit屏幕繪圖

Meowbit的屏幕還可以用來繪圖。

### 屏幕填色
    
    screen.fill(color)

將屏幕填色。
    
- color代表顏色，採用RGB格式。

### 屏幕像素

    screen.pixel(x,y,color)
    
在屏幕上繪畫像素。

- color代表顏色，採用RGB格式。

### 屏幕畫線

    screen.line(x1, y1, x2, y2, color)
  
在屏幕上以(x1，y1)和(x2，y2)為頂點繪畫線條。
  
- color代表顏色，採用RGB格式。

### 使用範例

    from meowbit import *
    
    screen.fill((100,0,100))
    screen.pixel(10,10,(0,255,0))
    screen.line(50,50,100,100,(0,0,255))

---

### 繪畫矩形

    screen.rect(x, y, width, height, color=255, fill=0)
    
在座標繪畫矩形。

- 座標為矩形的左上角。

- width和height代表長和闊。

- color代表顏色，採用RGB格式。

- fill代表填充，1代表填充0代表不填充，默認為0。

### 繪畫圓形

    screen.circle(x, y, r, color=(R, G, B), fill=0)
    
在座標繪畫圓形。   

- 座標為圓形的圓心。

- r代表半徑。

- color代表顏色，採用RGB格式。

- fill代表填充，1代表填充0代表不填充，默認為0。 

### 繪畫三角形

    screen.triangle(x1, y1, x2, y2, x3, y3, color=255, fill=0)
    
以(x1，y1)(x2，y2)(x3，y3)三點作頂點繪畫三角形。   

- color代表顏色，採用RGB格式。

- fill代表填充，1代表填充0代表不填充，默認為0。

### 繪畫多邊形

    screen.polygon(x, y, sides=3, r=10, th=3, rot=0, color=255, fill=0)
    
在屏幕繪畫多邊形。

- 座標為多邊形的中心。

- r代表中心點到邊緣的距離。

- sides代表邊的數目。

- th代表邊緣的粗度，rot代表旋轉角度。

- color代表顏色，採用RGB格式。

- fill代表填充，1代表填充0代表不填充，默認為0。

### 使用範例

    from meowbit import *
    
    screen.fill((100,0,100))
    screen.pixel(10,10,(0,255,0))
    screen.line(50,50,100,100,(0,0,255))
---

### 屏幕刷新

    screen.refresh()
    
刷新1次屏幕。

### 屏幕同步刷新

    screen.sync=val
    
設定屏幕同步刷新。

- val代表狀態，1代表開啟，0代表關閉，默認為1。

### 使用範例

    from meowbit import *
    screen.sync=0
    x=0
    while 1:
        screen.fill(0)
        screen.circle(x,40,20,(255,0,0),1)
        x+=1
        screen.refresh()

## Meowbit顯示圖片

### 顯示bmp

    screen.loadBmp(path, x=0, y=0)
    
- path代表圖片名稱
- 座標為矩形的左上角。
 
### 顯示gif
 
    screen.loadgif(path, x = 0, y = 0)

- path代表圖片名稱
- 座標為矩形的左上角。

### 使用範例

[測試圖片](https://www.yuque.com/attachments/yuque/0/2020/zip/1432972/1600221900298-00115433-2988-472c-938c-09802ee59c35.zip?from=https%3A%2F%2Fwww.yuque.com%2Fkittenbot%2Fhardwares%2Fmeowbit-micropython)

    # 顯示bmp
    from meowbit import *
    screen.loadBmp('haimian.bmp')

--------------

    # 顯示gif
    from meowbit import *
    screen.loadBmp('haimian.gif')
    
## Meowbit按鍵

Meowbit上有6個按鍵可以編程。

### 取得按鍵數值

    sensor.btnValue(btn)
    
取得按鍵數值。

- btn代表按鍵，分別為'a'，'b'，'up'，'down'，'left'，'right'。

### 按鍵引發事件

    sensor.btnTrig[btn] = fn
    sensor.startSchedule()
    
- btn代表按鍵，分別為'a'，'b'，'up'，'down'，'left'，'right'。
- fn代表要執行的函數。
- startSchedule()能使程式不需要在無限運行時都會不斷檢測按鍵狀態。(例子請參考範例)

### 使用範例

    from meowbit import *
    screen.sync=0
    while 1:
        screen.fill(0)
        screen.text(sensor.btnValue('a'))
        screen.refresh()
        
 ---
    from meowbit import *
    import random as r
    screen.fill(0)
    def drawCircle():
        screen.circle(r.randint(0,160),r.randint(0,128),10,(255,0,0),1)
    
    while 1:
        sensor.btnTrig['b']=drawCircle
        
---
    from meowbit import *
    import random as r
    screen.fill(0)
    def drawCircle():
        screen.circle(r.randint(0,160),r.randint(0,128),10,(255,0,0),1)
    
    sensor.btnTrig['b']=drawCircle
    sensor.startSchedule()
    
## Meowbit LED

Meowbit上有2顆LED燈可供使用，分別為led1和led2。

### 控制開關

    led1.on()
    led2.off()
    
控制LED的開和關。

### 狀態切換

    led1.toggle()

切換LED的狀態。

### 控制亮度
    
    led1.intensity(brightness)
    
控制LED的亮度。

- 亮度範圍由0-255。

### 使用範例

    from meowbit import *
    from time import sleep
    
    for i in range(5):
        led1.on()
        sleep(1)
        led1.off()
        sleep(1)
    
---

    from meowbit import *
    from time import sleep
    
    for i in range(5):
        led2.toggle()
        sleep(1)
        
---

    from meowbit import *
    import time
    
    for i in range(256):
        led1.intensity(i)
        time.sleep_ms(10)
    for i in range(255, 0, -1):
        led1.intensity(i)
        time.sleep_ms(10)
        
## Meowbit蜂鳴器

Meowbit上也搭載了蜂鳴器。

### 頻率發聲

    buzzer.tone(freq, delay = 0.5)
    
用特定頻率控制蜂鳴器發聲。

- freq代表頻率，頻率與音調對照表請參考：[頻率對照表](http://cdn.kittenbot.cn/freqToTone.txt)
- delay代表延時，即持續時間，單位為秒，為-1時會持續發聲，默認為0.5秒。

### 音調發聲

    buzzer.note(note, delay = 0.5)
    
- note代表音調，0～130共12個8度，12的倍數為C音。
- delay代表延時，即持續時間，單位為秒，為-1時會持續發聲，默認為0.5秒。

### 蜂鳴器靜音

    buzzer.rest(rest)

靜音一定時間。

- rest代表持續時間，單位為秒。

### 播放旋律

    buzzer.melody(m, bpm = 120)
    
播放一段旋律。

- m代表旋律，m+octave:duration，即是音符+八度音階(默認為4)：長度(默認為4拍子)，你亦可以加入r用作休止符。
    - 例如： "d5:1 b4:1" ， "a3:2 r a3:2"
- bpm代表拍速，默認為120拍/分鐘。
- 固件內預載了數款音效，可以直接使用。
    - CORRECT，NOTICE，ERROR
 
### 停止播放

    buzzer.stop()
    
停止蜂鳴器播放。

### 使用範例

    from meowbit import *
    
    def stopBuzzer():
        buzzer.stop()
        
    sensor.btnTrig['a'] = stopBuzzer
    sensor.startSchedule()
    
    buzzer.tone(262, 1)
    buzzer.rest(1)
    buzzer.note(60, 1)
    buzzer.rest(1)
    buzzer.melody("d r d4:4")
    buzzer.rest(1)
    buzzer.melody(CORRECT)
    
---
    
    from meowbit import *
    
    while 1:
        if sensor.btnValue('a'):
            buzzer.tone(240, -1)
        else:
            buzzer.stop()
            
## Meowbit感應器

### 溫度感應器

    sensor.getTemp()
    
獲取溫度數值，單位為攝氏。

### 光度感應器

    sensor.getLight()
    
獲取亮度檢測數值，範圍由0～4096。

### 使用範例

    from meowbit import *
    
    screen.sync = 0
    
    while 1:
        screen.fill(0)
        lightValue = sensor.getLight()
        tempValue = sensor.getTemp()
        screen.text('Temperature:' + str(tempValue), 20, 50)
        screen.text('Brightness: ' + str(lightValue), 20, 70)
        screen.refresh()
        