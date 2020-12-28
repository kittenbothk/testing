# KOI MicroPython API

KOI也支援使用MicroPython編程，可以實現純文字的編程。

## 導入KOI庫

需要先導入KOI庫才可以使用KOI。

    from koi import *

## 基本應用

### 改變屏幕方向

    lcd.rotation(0)
    
改變屏幕方向。

- 屏幕方向：0代表前置鏡頭，1代表橫置鏡頭，2代表後置鏡頭。

### 顯示字串

    drawString(x, y, string, delay)
    
在屏幕顯示字串。

- x和y代表文字左上角的座標。
- string代表字串。
- delay代表延時，字串顯示時間。

### 截圖和顯示

    img.save("s1.jpg")
    loadImage("s1.jpg")
    
用KOI拍照和顯示相片。

### 獲取按鍵數值

    btnAValue()
    btnBValue()
    
獲取A和B按鍵數值。

- 當按下時返回數值為1，否則為0。

### 示範程式

    #/bin/python
    from koi import *
    
    from time import sleep
    
    x = 0
    
    lcd.rotation(2)
    sleep(1)
    lcd.rotation(0)
    sleep(1)
    drawString(5,5,"hello world",500)
    while True:
      img=sensor.snapshot()     #屏幕刷新
      lcd.display(img)          #屏幕刷新
      if btnAValue() == 1:
        img.save("s1.jpg")
      if btnBValue() == 1:
        loadImage("s1.jpg")
        
## 特徵分類器

### 初始化分類器

    cla.reset()
    
初始化特徵分類器。

### 特徵提取

    cla.addImage("tag")

提取特徵添加標籤。

- tag代表物件標籤，最多支援40張圖片，40件物件。

### 執行特徵分類

    cla.getImageTag()
    
運行一次分類器。

### 分類器返回觸發事件

    while cla.getImageTag()=='tag':
        pass
    
分類器返回標籤為tag時觸發事件。

### 保存和載入分類器

    cla.save("abc.json")
    cla.load("abc.json")
    
保存分類器模型和載入分類器模型。

### 示範程式

    #模型訓練與保存
    from koi import *
    
    x=0
    
    cla.reset()
    
    while True:
        img=sensor.snapshot()   #屏幕刷新
        lcd.display(img)        #屏幕刷新
        if btnAValue():
            cla.addImage('apple')
        if btnBValue():
            cla.addImage('orange')
        if btnAValue() and btnBValue():
            cla.save('fruit.json')
        time.sleep(0.1)

---
    #模型載入與運行
    from koi import *
    
    x=0
    cla.reset()
    cla.load("fruit.json")
    
    while True:
        img=sensor.snapshot()   #屏幕刷新
        lcd.display(img)        #屏幕刷新
        if btnAValue():
            tag=cla.getImageTag()
            if tag=='orange':
                print('I like oranges.')
            elif tag=='apple':
                print('Apples are healthy.')
        time.sleep(0.1)
    
## 人臉追蹤

### 載入人臉模型

    yoloinit()

載入人臉模型。

### 運行人臉追蹤

    trackface()

運行人臉追蹤。

### 示範程式

    #/bin/python
    from koi import *
    
    x = 0
    face_prop=[0,0]
    
    yoloinit()
    while True:
        img=sensor.snapshot()   #屏幕刷新
        lcd.display(img)        #屏幕刷新
        r = trackface()
        if r:
            is_face=1
            drawString(5,5,r,500)
            face_prop[0]=(r[0][2]+r[0][0])/2
            face_prop[1]=(r[0][3]+r[0][1])/2
        else:
            is_face=0
            
        while is_face:
            print('X: '+str(face_prop[0]))
            print('Y: '+str(face_prop[1]))
            is_face=0
        time.sleep(0.5)
    
## 幾何圖形識別

### 線條追蹤

    findLines()
    
追蹤畫面裡的線條。返回一個列表。

### 圓形追蹤
    
    findCircle(threshold)
    
追蹤畫面裡的圓形。

- threshold代表臨界值，越高越難追蹤，一般建議4000。返回一個列表。

### 矩形追蹤

    findCircle(threshold)
    
追蹤畫面裡的矩形。

- threshold代表臨界值，越高越難追蹤，一般建議4000。返回一個列表。

### 示範程式

    from koi import *

    x=0
    
    while True:
        img=sensor.snapshot()   #屏幕刷新
        lcd.display(img)        #屏幕刷新
        if btnAValue() and btnBValue():
            line_prop = findLines()
            print(line_prop[0])
            time.sleep(0.1)
        elif btnAValue():
            circle_prop = findCircle(4000)
            print(circle_prop[0])
            time.sleep(0.1)
        elif btnBValue():
            rect_prop = findRects(4000)
            print(rect_prop[0])
            time.sleep(0.1)
            
## 顏色追蹤

### 顏色校正

    colorCalibrate()
    
校正要追蹤的顏色。

### 追蹤色塊

    findBlob()
    
追蹤色塊。

### 追蹤巡線

    findLinearRegress()
    
追蹤巡線。

### 示範程式

    from koi import *
    
    x=0
    
    while True:
        img=sensor.snapshot()   #屏幕刷新
        lcd.display(img)        #屏幕刷新
        if btnAValue():
            colorCalibrate()
            time.sleep(0.1)
        elif btnBValue():
            blob_prop=findBlob()
            print(blob_prop[0])
            time.sleep(0.1)
        elif btnAValue() and btnBValue():
            line_prop=findLinearRegress()
            print(line_prop[0])
            time.sleep(0.1)
            
## 條碼識別

### QR Code識別

    findQRCode()

識別畫面裡的QR Code。

### Barcode識別

    findBarcode()

識別畫面裡的Barcode。

### AprilTag識別

    findAprilTag()

識別畫面裡的AprilTag。

### 示範程式

    from koi import *

    x=0
    
    lcd.rotation(2)
    
    while True:
        img=sensor.snapshot()   #屏幕刷新
        lcd.display(img)        #屏幕刷新
        if btnAValue():
            barcode=findBarCode()
            print(barcode[0][4])
            time.sleep(0.1)
        if btnBValue():
            qrcode=findQRCode()
            print(qrcode[0][4])
            time.sleep(0.1)
        if btnAValue() and btnBValue():
            april=findAprilTag()
            print(april[0])
            time.sleep(0.1)
            
## 語音辨識

### 錄音與播放

    speech.recordWav('hi.wav')
    speech.playWav('hi.wav')
    
錄製與播放wav音頻檔。

### 語音辨識-設立噪音基準

    speech.noiseTap()

設立噪音基準，語音辨識前必須運行。

### 語音辨識-增加命令詞

    speech.addCommand('hi')
    
增加語音辨識命令詞。

### 運行語音辨識

    speech.getCommand()
    
運行語音辨識，返回命令詞。

### 參考程式

    # 錄音與播放
    from koi import *

    x=0

    while True:
        img=sensor.snapshot()   #屏幕刷新
        lcd.display(img)        #屏幕刷新
        if btnAValue():
            speech.recordWav('hi.wav')
            time.sleep(0.1)
        if btnBValue():
            speech.playWav('hi.wav')
            time.sleep(0.1)
            
---    
    
    #語音辨識
    from koi import *
    
    x=0
    
    speech.noiseTap()
    
    while True:
        img=sensor.snapshot()   #屏幕刷新
        lcd.display(img)        #屏幕刷新
        if btnAValue():
            speech.addCommand("hello")
            time.sleep(0.1)
        if btnBValue():
            speech.addCommand("bye")
            time.sleep(0.1)
        if btnAValue() and btnBValue():
            print(speech.getCommand())
            time.sleep(0.1)
            
## 物聯網

### 連接網絡

    wifi.joinap(str("apname"),str("password"))
    
連接WiFi網絡。
    
### IP地址

    wifi.ipaddr()
    
獲取IP地址。

### 連接MQTT伺服器

    wifi.mqtthost(host)
    
連接MQTT伺服器。

- host代表伺服器地址。

### 訂閱話題

    wifi.mqttsub(topic)

訂閱MQTT話題。
  
- topic代表話題。

### 發佈信息

    wifi.mqttsub(topic, message)
    
發佈信息到話題。

- topic代表話題。
- message代表信息。

### 讀取訊息

    wifi.mqttread(topic)
    
讀取話題信息。

- topic代表話題。

### 參考程式

    from koi import *
    
    wifi.joinap(str("apname"),str("password"))
    time.sleep(2)
    print(wifi.ipaddr())
    time.sleep(2)
    wifi.mqtthost("127.0.0.1")
    wifi.mqttsub("test01")
    
    while True:
        img=sensor.snapshot()    #屏幕刷新
        lcd.display(img)         #屏幕刷新
        if btnAValue():
            wifi.mqttpub("test01","hello world")
        if btnBValue():
            msg=wifi.mqttread("test01")
            print("Message: "+msg[0])
            print("Topic: "+msg[1])

## 人臉辨識

### 運行一次人臉辨識

    face=baiduFace(op=1)

運行一次人臉辨識。(需要網絡連線)
    
### 人臉參數

    face['parameter']

獲取人臉辨識的參數。

parameter代表參數，可以獲得的參數有：

- facetoken：人臉特徵碼
- location: 人臉的位置信息，包括座標和大小等
- gender：性別
- expression：表情
- angle：人臉傾斜角度
- mask：人臉是否有佩戴口罩
- age：年齡
    
### 添加人臉到組別

    baiduFace(op=2, token=face['face_token'], group="group", name="name")
    
將人臉的名稱添加到組別。
    
### 在組別搜尋人臉

    baiduFace(op=3, token=face['face_token'], group="group")
    
在組別搜尋人臉，返回人臉的名字和準確度。

### 參考程式

    from koi import *
    
    wifi.joinap(str("apname"),str("password"))
    time.sleep(2)
    
    while True:
        img=sensor.snapshot()   #屏幕刷新
        lcd.display(img)        #屏幕刷新
        if btnAValue():
            face=baiduFace(op=1)
            time.sleep(5)
            baiduFace(op=2, token=face['face_token'], group="group", name="name")
        if btnBValue():
            face=baiduFace(op=1)
            time.sleep(5)
            print(baiduFace(op=3, token=face['face_token'], group="group"))
            
## Q&A

