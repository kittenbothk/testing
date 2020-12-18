# GeekServo 2KG電機

2KG電機 (HKBD8009A)

![](./images/image--010.png)

這是一款兼容樂高插孔的高扭力的電機，相對於9g電機，在同等供電下具有更高轉速。輸出軸為兩組樂高十字孔，主要用在驅動動力機械。

## 產品參數

- 工作電壓：3.3V~6V
- 額定電壓：4.8V
- 額定電流：70mA
- 堵轉電流：900mA   
- 打滑電流：700mA
- 最大扭力：1.6kg±0.2kg/cm(4.8V)
- 最高轉速：120rpm(3V供電情况下)
- 重量：20g
- 接口：紅黑線

## 產品特色：

![](./images/2kg_1.jpg)

繼承了GeekServo 9G舵機電機的優點，增強了扭力與速度，改善了結構

- 採用十字沉孔作輸出軸
    - 可以因使用情況自由插入不同長度的十字軸

- 扭力更大
    - 扭力為GeekMotor 9G的三倍左右

## 規格尺寸

### 樂高孔單位:

- 長度：5孔
- 闊度：3孔
- 高度：3孔
- 輸出軸：樂高十字軸

### mm單位:

- 長度：40mm
- 闊度：24mm
- 高度：24mm
- 輸出軸：樂高十字軸

![](./images/0111.png)

## 接線方法

### Armourbit

---

將電機的紅黑線連接至Armourbit底部的電機接口。

![](./images/2kmotorCon.jpg)

    沒有嚴格正負極之分，插的方向只會影響電機轉動方向。
    
### Robotbit

---

將電機的紅黑線連接至RobotBit的電機接口。

![](./images/2kmotorConRB.jpg)

![](./images/2kmotorConRB1.jpg)

    沒有嚴格正負極之分，插的方向只會影響電機轉動方向。

## MakeCode編程教學

### 此模組可供Microbit和Meowbit使用。

![](./images/mcbanner.png)

![](../meowbit/images/acbanner.png)

### Armourbit

---


### 加載PowerBrick插件：https://github.com/KittenBot/pxt-powerbrick

### [詳細方法](../Makecode/powerBrickMC)

### 電機積木塊:

![](./images/2kmotorblocks.png)

### 電機編程

![](./images/2kmotorcode.png)

[參考程式下載](https://bit.ly/PowerbrickM11_01Hex)

### RobotBit

---

### 加載RobotBit插件：

![](./images/robotbitExtension.png)

### [詳細方法](../Makecode/powerBrickMC)

### 電機積木塊:

![](./images/2kmotorblocks_rb.png)

### 電機編程

![](./images/2kmotorcode_rb.png)

[參考程式網址](https://makecode.microbit.org/_33HMywgx9H97q)

### Meowbit:

---

### 加載robotbit插件：https://github.com/KittenBot/meow-robotbit

### [詳細方法](../Makecode/powerBrickMC)

### 電機積木塊:

![](../motors/images/motorblocks.png)

## 電機編程

![](../motors/images/2kmotorcode_meow.png)

[參考程式網址](https://makecode.com/_2z0C8v6XAC5y)

## 插件版本與更新

插件可能會不定時推出更新，改進功能。亦有時候我們可能需要轉用舊版插件才可使用某些功能。

詳情請參考: [Makecode插件版本更換](../Makecode/makecode_extensionUpdate)

## KittenBlock編程教學

![](./images/kbbanner.png)

### Armourbit

--- 

### 加載PowerBrick插件

在左上角小貓logo旁邊的硬件欄選擇PowerBrick，加載Microbit與Powerbrick插件。

![](./images/addextension.png)

### 電機積木塊

![](./images/2kkbmotorblocks.png)

### 電機編程

![](./images/2kkbmotor.png)

[參考程式下載](https://bit.ly/PowerbrickM11_01sb3)

[參考程式網址](https://makecode.microbit.org/_RYHivyayYL4q)

### Robotbit

---

### 加載Robotbit插件

在左上角小貓logo旁邊的硬件欄選擇Microbit，加載Microbit與Robotbit插件。

![](./images/addRB.png)

### 電機積木塊

![](./images/rbmotorblocks.png)

### 電機編程

![](./images/rbmotorcode.png)



## FAQ

1：為什麼我點擊積木塊沒有反應呢？

首先確保已經連接好Microbit，然後上載韌體再試一試。