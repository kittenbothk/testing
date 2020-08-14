# All in 1水箱連水泵組合

All in 1水箱連水泵組合 (HKBM8015A)

![](../PWmodules/images/image--010.png)

內置浸入式水泵一體化水箱，簡潔方便；水箱頂蓋和底部兼容樂高顆粒件，適合用作智能灌溉、自動洗手機等。

## 產品參數

- 工作電壓：3.3V~6V
- 尺寸：86.5X86.5X98mm
- 額定電流：120mA(3.3V)
- 流量：80L/h
- 最大揚程：0.35M
- 重量：140g
- 膠管長度：60cm
- 接口：紅黑線

## 接線方法

將電機的紅黑線連接至Armourbit底部的電機接口。

![](../PWmodules/images/pumpCon.jpg)

    沒有嚴格正負極之分，插的方向只會影響電機轉動方向。

## MakeCode編程教學

![](../PWmodules/images/mcbanner.png)

### 加載PowerBrick插件：https://github.com/KittenBot/pxt-powerbrick

### 電機積木塊:

![](../PWmodules/images/motorblocks.png)

### 電機編程

![](../PWmodules/images/pumpcode.png)

[參考程式下載](https://bit.ly/M15WaterTankSampleHex)

## KittenBlock編程教學

![](../PWmodules/images/kbbanner.png)

### 加載PowerBrick插件

離線版與在線版同樣操作。

在左上角小貓logo旁邊的硬件欄選擇PowerBrick，加載Microbit與Powerbrick插件。

![](../PWmodules/images/addextension.png)

### 電機積木塊

![](../PWmodules/kbimages/kbmotorblocks.png)

### 電機編程

![](../PWmodules/kbimages/kbpumpcode.png)

[參考程式下載](https://bit.ly/PowerbrickM11_01sb3)

## FAQ

1：為什麼我點擊積木塊沒有反應呢？

首先確保已經連接好Microbit，然後上載韌體再試一試。