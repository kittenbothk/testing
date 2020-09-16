# 磁場感應器模組

![](./images/magnet2.png)

這是一隻可以感應磁場的模組，它返回的數值是數位形式。

數值範圍由0-1，沒有探測到磁石時返回1，探測到磁石時返回0。

## 產品參數

- 工作電壓：3.3V~5V
- 類型：數位模組
- 接口：3Pin防反插

## 接線教學

### Robotbit Shield

將磁場感應器模組連接到Robotbit Shield的3PIN接口。

![](./images/magnet_wire2.png)

### Robotbit

將磁場感應器模組連接到Robotbit的針線和3V接口。

![](./images/magnet_wire1.png)

## MakeCode編程教學

![](./PWmodules/images/mcbanner.png)

### 加載robotbit插件：https://github.com/KittenBot/pxt-robotbit

#### 讀取磁場數值編程

![](./images/digitRead_code.png)


## 插件版本與更新

Robotbit插件可能會不定時推出更新，改進功能。亦有時候我們可能需要轉用舊版插件才可使用某些功能。

詳情請參考: [Makecode插件版本更換](../../Makecode/makecode_extensionUpdate)


## KittenBlock編程教學

![](./PWmodules/images/kbbanner.png)

### 加載Robotbit插件

![](./images/addRB.png)

#### 讀取磁場數值編程

![](./images/magnet_codekb.png)

## Mu Editor編程教學

#### 讀取磁場數值編程

![](./images/magnet_codemu.png)