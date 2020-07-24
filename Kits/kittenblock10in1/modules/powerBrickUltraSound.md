# 超聲波聲音魔塊

超聲波聲音魔塊 (HKBM8012K)

![](./images/06_04.png)

這魔塊包含了超聲波感應器和咪高峰。它可以用超聲波來測量與物件的距離，咪高峰可以探測環境聲音的強弱。


![](./images/IMG_2577.GIF)

![](./images/IMG_2576.GIF)

## 詳細介紹

![](./images/06_01.png)

## 產品參數

- 支援電壓：3V-5V
- 尺寸：56mm X 24mm X 24mm
- 接口：4PIN防反接排線
- 超聲波探測距離：4cm-200cm（推薦範圍）
- 聲音模擬數值範圍：0-1023

## 使用注意事項

- 超聲波距離測量要求物件表面比較平整，平面盡量與超聲波魔塊垂直。超聲波的發射是一個扇形，所以要注意測量距離之間是否有其他障礙物遮擋。
- 咪高峰只能檢測環境聲音的強度，並非分貝值，測量分貝值需要比較專業的儀器。咪高峰只是檢測瞬時聲音的強弱數值。

## 接線方法

將超聲波聲音魔塊用4pin排線連接至Armourbit。

![](./kbimages/ultrasoundcon.jpg)

## MakeCode編程教學

加載PowerBrick插件：https://github.com/KittenBot/pxt-powerbrick

### 超聲波聲音魔塊積木塊:

![](./images/ultrasoundblocks.png)

### 距離檢測編程

![](./images/distance.png)

[參考程式下載](https://bit.ly/PowerbrickM4_01)

### 環境聲音檢測編程

![](./images/soundlevel.png)

[參考程式下載](https://bit.ly/PowerbrickM4_02Hex)

### Makecode教學短片

[![](./kbimages/ultrasoundtut.png)](https://www.youtube.com/watch?v=Jwj449zjnYE)

## KittenBlock編程教學

### 加載PowerBrick插件

離線版與在線版同樣操作。

在左上角小貓logo旁邊的硬件欄選擇PowerBrick，加載Microbit與Powerbrick插件。

![](./kbimages/addextension.png)

### 巡線積木塊

![](./kbimages/kbultrasoundblocks.png)

### 距離檢測編程

![](./kbimages/kbultrasounddist.png)

[參考程式下載](https://bit.ly/PowerbrickM4_01sb3)

### 環境聲音檢測編程

![](./kbimages/kbultrasoundlevel.png)

[參考程式下載](https://bit.ly/PowerbrickM4_02sb3)

## FAQ

1：為什麼我點擊積木塊沒有反應呢？

首先確保已經連接好Microbit，然後上載韌體再試一試。