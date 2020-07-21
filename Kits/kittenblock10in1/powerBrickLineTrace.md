# 雙路IR巡線感應模組

雙路IR巡線感應模組 (HKBM8012B)

![](./images/07_03.png)

這是一個IR巡線模組，它有組兩路尋線感應器，測量電平值高低，偵察到黑線後模組背面的LED會熄滅，觸發尋線事件。

## 詳細介紹

![](./images/07_01.png)

## 產品參數

- 支援電壓：3V-5V
- 尺寸：56mm X 24mm X 25mm
- 接口：4pin防反插接口

## 注意事項

- 巡線模組需要盡量貼近地面。
- 枱面或地板必須為不反光的表面。

## 接線方法

將巡線模組用4pin排線連接至Armourbit。

![](./kbimages/07_02.png)

## MakeCode編程教學

加載PowerBrick插件：https://github.com/KittenBot/pxt-powerbrick

### 巡線模組積木塊:

![](./images/linefollowblocks.png)

### 黑線檢測

我們在枱面貼上黑色膠紙，用巡線模組檢測，當感應器A或B檢測到膠紙的時候就會分別顯示笑臉或哭臉，假如沒有偵測到線條就會顯示心形。

![](./images/linefollow.png)

[參考程式下載](www.google.com)

## 模組演示

![](./images/IMG_2570.GIF)