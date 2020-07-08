# **圓形追踪**

<<<<<<< HEAD
矩形與圓形追踪在生活中用得比較少，一般用在工業流水線上的視覺分揀與碼垛場景。



## 編寫圓形追踪程式
=======
·    條碼 (Bar Code) 廣泛用於我們生活中，例如產品的識別標籤。

·    二維碼(QR Code)用於支付場景或者社交場景。



## 編寫Bar Code及QR Code讀取程式
>>>>>>> 48c291569cb03a3385baa461af65d77e513a5ff8

**加載KOI插件：https://github.com/KittenBot/pxt-koi**



按鍵積木塊：

<<<<<<< HEAD


​             ![](KOI07/01-1.png)
=======
 ![](KOI06/01.png)
>>>>>>> 48c291569cb03a3385baa461af65d77e513a5ff8



完整參考程式：

<<<<<<< HEAD
  ![](KOI07/02-1.png)



### 臨界值

 ![](KOI07/04-1.png)

臨界值是影響識別率的一個參數, 需要自主嘗試並調整臨界值。

臨界值越大，干擾越少，但識別難度也會提高。因此需要自己根據場景多做測試。
=======
  ![](KOI06/02-1.png)
>>>>>>> 48c291569cb03a3385baa461af65d77e513a5ff8



## **程式運行流程**

<<<<<<< HEAD
把程式下載到Microbit 上, 按下Microbit 上的A鍵. Microbit 點陣會顯示出檢測所得之半徑值 (佔KOI 的螢幕長度計算, 最大r 值在105 - 110 右左); 同時在KOI 的螢幕上顯示出圓中心的X, Y 位置值。
=======
把程式下載到Microbit 上, 

1. 把Bar Code 放到KOI 鏡頭前, 按下Microbit的按鍵A，進行識別;  Bar Code 數字便會顯示在KOI 的螢幕上。
2. 把QR Code 放到KOI 鏡頭前, 按下Microbit的按鍵B，進行識別;  QR Code 所含的資訊便會顯示在KOI 的螢幕上。
>>>>>>> 48c291569cb03a3385baa461af65d77e513a5ff8



## 進階程式

<<<<<<< HEAD
為方便讀取圓形資訊, 我們便可考慮多加一塊OLED顯示屏, 以提高資訊的可讀性。
=======
讀取Bar Code 及 QR Code 後可能出現大量資訊, 在KOI 的螢幕上未必有足夠時間閱讀; 此時我們便可考慮多加一塊OLED顯示屏, 以提高資訊的可讀性。
>>>>>>> 48c291569cb03a3385baa461af65d77e513a5ff8

### OLED接線

本例子以Robotbit 示範, 把OLED 屏接到I2C 接口上

<<<<<<< HEAD
​      ![](KOI06/03-1.png)
=======
 ![](KOI06/03-1.png)
>>>>>>> 48c291569cb03a3385baa461af65d77e513a5ff8



### 編寫程式

**加入OLED的插件： https://github.com/KittenBot/pxt-oled**

<<<<<<< HEAD
 ![](KOI07/03-1.png)
=======
 ![](KOI06/04-1.png)


>>>>>>> 48c291569cb03a3385baa461af65d77e513a5ff8



## 參考程式下載

<<<<<<< HEAD
[1. 圓形追踪 Hex](https://bit.ly/KOICircleRegHex)

[2. 圓形追踪, OLED顯示](https://bit.ly/KOICircleRegOLEDHex)
=======
[1. 讀取Bar Code及QR Code Hex](https://bit.ly/KOIQRBarCodeScannerHex)

[2. 讀取Bar Code 及QR Code, OLED顯示](https://bit.ly/KOIBarAndQRCodeReadOLEDHex)

[Bar Code 及 QR Code Sample](https://bit.ly/KOIBarAndQRCodeSample)
>>>>>>> 48c291569cb03a3385baa461af65d77e513a5ff8



## FAQ

1. **為什麼我打開電源，按Microbit的A按鍵，怎麼沒反應？**

​       ·    答：打開電源後, KOI 及microbit 同時起動; 相對上, Microbit 所需的起動時間比KOI魔塊短, 引致 Microbit 的初始化程式已經跑完了，KOI還沒完全起動。

​       ·    解決辦法：打開電源後，重新按下Microbit背後的Reset按鍵，讓Microbit重新開始運行（秘訣就是讓KOI魔塊先完全運行起來，再讓Microbit 跑初始化程式）



<<<<<<< HEAD
2. **如何提高識別率**

   ·    調整識別閾值，調整識別環境與調整識別物體;

   ·    識別背景盡量單調，不能太雜亂;

   ·    圓形有銳利的輪廓。
   
=======
2. **為什麼不能成功讀取Bar Code 或QR Code？**

   ·    答：條碼及二維碼的寬度要求不小於3.5cm; 若條碼太小，會因解析度太小的原因無法識別。另掃描時保證完全條碼或二維碼入鏡且清晰。

   

>>>>>>> 48c291569cb03a3385baa461af65d77e513a5ff8
   


