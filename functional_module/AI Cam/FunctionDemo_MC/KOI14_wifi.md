# **IoT物聯網 (固件版本: v1.8.2或之後)**

KOI上面也有Wifi的功能，我們可以透過Wifi存取物聯網平台的數據。

## 編寫物聯網程式

![](../../PWmodules/images/mcbanner.png)

### 加載KOI插件：https://github.com/KittenBot/pxt-koi


### [詳細方法](../makecodeQs.md)

物聯網積木塊：

![](KOI14/1.png)

編寫程式：

我們本節教程將會使用MakerCloud作示範。

有關創客雲的資料可以參考： [創客雲介紹](https://learn.makercloud.io/zh_TW/latest/)
    
![](KOI14/5.png)

## 程式流程

1: 首先將程式下載到Microbit上。

2: 等待KOI連接網絡，完成後Microbit上會顯示剔號。

    像手提電話一樣，連接Wifi網絡的名稱密碼，和MQTT伺服器的資料已經會儲存在KOI上面。
    所以不需要每次使用時都是用連接wifi網絡和MQTT的積木，只需要訂閱話題就可以了。

3: 按下A按鍵，由0至10隨機取數然後將數值傳上MQTT伺服器。

4: 按下B按鍵，讀取MQTT的上的數據。

5: 讀取到的數據(剛才我們傳上去的數字)就會顯示在KOI的屏幕上。

## 參考程式

[1. 物聯網HEX網址(v1.8.2)](https://makecode.microbit.org/_X7iWq8XtJega)

## FAQ

### 1： 為什麼我重新開機，按下按鍵A，但按鍵沒有反應？

·    答：打開電源後, KOI 及microbit 同時起動; 相對上, Microbit 所需的起動時間比KOI魔塊短, 引致 Microbit的初始化程式已經跑完了，KOI還沒完全起動, 因此按下A鍵沒有反應。

·    解決辦法：打開電源後，重新按下Microbit背後的Reset按鍵，讓Microbit重新開始運行（秘訣就是讓KOI魔塊先完全運行起來，再讓Microbit 跑初始化程式）

### 2： KOI鯉魚魔塊我直接3V電源可以嗎？

·    答：不行，必須要接5V！

### 3: KOI開啟的時候出現選項菜單，我應該按下A還是B呢？

·    答：KOI在新的固件上新增了開機選項，選擇主控板或被動運行模式。

·    解決辦法：連接Microbit時我們選擇被動模式，按下KOI的B按鍵（右面的按鍵），進入被動模式。