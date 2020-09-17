# **方形追踪**

方形與圓形追踪在生活中用得比較少，一般用在工業流水線上的視覺分揀。



## 編寫方形追踪程式

![](../../PWmodules/images/mcbanner.png)

### 加載KOI插件：https://github.com/KittenBot/pxt-koi

### [詳細方法](../makecodeQs.md)

方形追踪積木塊：

![](KOI08/01-1.png)

完整參考程式：

![](KOI08/02-1.png)

### 臨界值

![](KOI08/04-1.png)

臨界值是影響識別率的一個參數, 需要自主嘗試並調整臨界值。

臨界值越大，干擾越少，但識別難度也會提高。因此需要自己根據場景多做測試。

## 程式運行流程

程式下載到Microbit 上, 按下Microbit 上的A鍵. KOI 的螢幕上顯示出左下角的x, y 位置值, 還有當時測得的長度與寬度 (KOI 螢幕單位佔比計算)

## 進階程式

為方便讀取方形資訊, 我們便可考慮多加一塊OLED顯示屏, 以提高資訊的可讀性。

### OLED接線

本例子以Robotbit 示範, 把OLED 屏接到I2C 接口上

![](KOI06/03-1.png)

### 編寫程式

### 加入OLED的插件： https://github.com/KittenBot/pxt-oled**

![](KOI08/03-1.png)

## 參考程式

[1. 方形追踪 HEX (插件0.5.7)](https://makecode.microbit.org/_2i4V1rWPUWiu)

[2. 方形追踪, OLED顯示HEX (插件0.5.7)](https://makecode.microbit.org/_JA5eX5EAHcJp)


## 插件版本與更新

插件可能會不定時推出更新，改進功能。亦有時候我們可能需要轉用舊版插件才可使用某些功能。

詳情請參考: [Makecode插件版本更換](../../../Makecode/makecode_extensionUpdate)

## FAQ

### 1: 為什麼我打開電源，按Microbit的A按鍵，怎麼沒反應？

​       ·    答：打開電源後, KOI 及microbit 同時起動; 相對上, Microbit 所需的起動時間比KOI魔塊短, 引致 Microbit 的初始化程式已經跑完了，KOI還沒完全起動。

​       ·    解決辦法：打開電源後，重新按下Microbit背後的Reset按鍵，讓Microbit重新開始運行（秘訣就是讓KOI魔塊先完全運行起來，再讓Microbit 跑初始化程式）

### 2: 如何提高識別率

   ·    調整識別閾值，調整識別環境與調整識別物體;

   ·    識別背景盡量單調，不能太雜亂;

   ·    方形有銳利的輪廓。


   


