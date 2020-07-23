# 顏色手勢感應模組 

顏色手勢感應模組 (HKBM8012F)

![](./images/09_06.png)

這是一塊多功能的模組，它的主要功能是識別顏色和識別手勢。

![](./images/IMG_2572.GIF)

![](./images/IMG_2573.GIF)

![](./images/IMG_2574.GIF)

它有4種模式：

1. 在顏色辨識模式下，4顆LED會常亮，檢測顏色的色環角度。它還可以檢測環境光度。
1. 在手勢辨識模式下，手的移動方向會觸發對應方向的LED閃動。
1. 在距離檢測模式下，最遠範圍為大約3cm。距離越近，LED越亮。
1. 在LED模式下，可以控制4顆LED的亮度。

## 詳細介紹

![](./images/09_05.png)

## 產品參數

- 支援電壓：3V-5V
- 尺寸：56mm X 24mm X 16mm
- 接口：4pin防反插接口
- 顏色識別檢測返回值：0－360
- 手勢識別模式下，可識別上下左右四個方向，分別返回1、2、3、4。偵測不到手勢則返回0。
- 距離檢測模式下，最大檢測距離為3cm左右，返回值為0-255，越靠近數值越大。
- 亮度檢測返回值：0-255

## 使用注意事項

- 這模組只能連接到I2C接口，其他接口無效。
- 使用前要先設置模式，否則默認為距離模式。
- 手勢模式下，你可能需要熟習一下手移動的方向、距離和速度才掌握到觸發技巧。
- 顏色辨認會返回HSV角度數值，並非RGB數值。
- 顏色辨認的距離為大約1cm時的效果最為理想。
- 在LED模式之下才可以控制LED的亮度。

## 接線方法

將顏色手勢模組用4pin排線連接至Armourbit的I2C接口。

![](./kbimages/gesturecon.jpg)

## MakeCode編程教學

加載PowerBrick插件：https://github.com/KittenBot/pxt-powerbrick

### 顏色手勢模組積木塊:

![](./images/colorgestureblocks1.png)

![](./images/colorgestureblocks2.png)

### 顏色檢測

![](./images/color.png)

[參考程式下載](https://bit.ly/PowerbrickM7_01Hex)

HSV色環可以參考下圖：

![](./images/hsv.jpg)

### 距離檢測

![](./images/colordist.png)

[參考程式下載](https://bit.ly/PowerbrickM7_03Hex)

### 亮度檢測

![](./images/colorbrightness.png)

[參考程式下載](https://bit.ly/PowerbrickM7_02Hex)

### 手勢檢測

![](./images/gesture.png)

[參考程式下載](https://bit.ly/PowerbrickM7_04Hex)

### LED控制

![](./images/led.png)

[參考程式下載](https://bit.ly/PowerbrickM7_05Hex)

### Makecode教學短片

[![](./images/gesturetut.png)](https://www.youtube.com/watch?v=7WrkDYMc2f0)

## KittenBlock編程教學

### 加載PowerBrick插件

離線版與在線版同樣操作。

在左上角小貓logo旁邊的硬件欄選擇PowerBrick，加載Microbit與Powerbrick插件。

![](./kbimages/addextension.png)

### 顏色手勢模組積木塊

![](./kbimages/kbcolorgestureblocks.png)

### 顏色檢測

![](./kbimages/kbcolor.png)

[參考程式下載](www.google.com)

### 亮度檢測

![](./kbimages/kbbrightness.png)

[參考程式下載](www.google.com)

### 距離檢測

![](./kbimages/kbcolordist.png)

[參考程式下載](www.google.com)

### 手勢檢測

![](./kbimages/kbgesture.png)

[參考程式下載](www.google.com)

### LED控制

![](./kbimages/kbled.png)

[參考程式下載](www.google.com)

## FAQ

1：為什麼我點擊積木塊沒有反應呢？

首先確保已經連接好Microbit，然後上載韌體再試一試。