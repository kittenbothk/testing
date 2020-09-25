# 雨滴水位感應器

雨滴水位感應器 (HKBM8012G)

![](./images/03drop.png)

這是一塊雨滴水位感應器它可以測量水位高低和是否有雨滴，水位越高數值越大。

![](./images/IMG_2581.GIF)

![](./images/IMG_2578.GIF)

## 使用注意事項：

- 若長期不使用感應器，請妥善放置乾燥地方保管，防止潮濕被氧化。
- 感應器上有最大限位線，請勿過度插入土壤或者水中，避免損壞電路。

## 接線方法

將溫度濕度感應器用4pin排線連接至Armourbit，然後用3pin排線將感應器連接至溫度濕度感應器。

![](./kbimages/06_03.png)

## MakeCode編程教學

![](./images/mcbanner.png)

### 加載PowerBrick插件：https://github.com/KittenBot/pxt-powerbrick

### 雨滴水位感應器積木塊:

![](./images/environmentblocks.png)

### 水位探測編程

![](./images/water.png)

[參考程式網址](https://makecode.microbit.org/_h4Ebo11zUhTr)

### MakeCode教學短片

[![](./images/envtut.png)](https://www.youtube.com/watch?v=ilXSpFd86DQ)

## 插件版本與更新

插件可能會不定時推出更新，改進功能。亦有時候我們可能需要轉用舊版插件才可使用某些功能。

詳情請參考: [Makecode插件版本更換](../../../Makecode/makecode_extensionUpdate)

## KittenBlock編程教學

![](./images/kbbanner.png)

### 加載PowerBrick插件

在左上角小貓logo旁邊的硬件欄選擇PowerBrick，加載Microbit與Powerbrick插件。

![](./kbimages/addextension.png)

### 環境積木塊

![](./kbimages/kbenvblocks.png)

### 水位探測編程

![](./kbimages/kbwaterlevel.png)

[參考程式下載](https://bit.ly/PowerbrickM2_01sb3)

## FAQ

1：為什麼我點擊積木塊沒有反應呢？

首先確保已經連接好Microbit，然後上載韌體再試一試。