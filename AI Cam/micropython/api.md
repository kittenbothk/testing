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

    btnA.value()
    btnB.value()
    
獲取A和B按鍵數值。

- 當按下時返回數值為0，否則為1。

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
      if btnA.value() == 0:
        img.save("s1.jpg")
      if btnB.value() == 0:
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


## 人臉追蹤

### 載入人臉模型

    yoloinit()

載入人臉模型。

### 運行人臉追蹤

    trackface()

運行人臉追蹤。