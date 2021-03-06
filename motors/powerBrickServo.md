# Geekservo 9g舵機

Geekservo舵機 (HKBD8005A)

![](./images/13_04.png)

這是一款兼容樂高件的舵機。輸出軸為樂高十字軸。主要用在需求精細控制的結構上，例如關節，機械臂。

## 產品參數

- 工作電壓：3.3V~6V
- 額定電壓：4.8V
- 額定電流：200ma
- 堵轉電流：700ma
- 打滑電流：450ma
- 最大扭力：500g/cm(4.8V)
- 角度轉速：60°/0.12s
- 角度範圍：-45°~225°
- 重量：12.4g
- 接口：橙紅啡線
    
## 使用注意事項

- 這只是一種小型電機，使用情境的扭力和電壓需求請不要過大。
- Geekservo舵機有嚴格的線序要求，請根據線序連接。
- 禁止長時間超出堵轉電流，否則會燒壞電機。

## 規格尺寸

### 樂高孔單位:

- 長度：5孔
- 闊度：2孔
- 高度：3孔
- 輸出軸：樂高十字軸

### mm單位:

- 長度：40mm
- 闊度：16mm
- 高度：34.4mm
- 輸出軸：樂高十字軸

![](./images/13_03.png)

## Geekservo特色

- 極力子過載保護:
    - 遇到輸出軸被暴力扭擰會啟動極力子進行跳齒保護，發出「噠噠噠」的聲音。不會損毀齒輪。

- 安裝方式靈活:
    - 支援樂高標準磚和Technic插孔，輸出軸亦是樂高標準十字軸。

- 輕盈小巧:
    - 方便製作各種小型機械。

## 接線方法

### ArmourBit

將舵機的橙紅啡線連接至Armourbit背部的舵機接口。

![](./kbimages/servo_wire.png)

    啡色接負極，紅色接正極，橙色接數據。
    
### RobotBit

將舵機的橙紅啡線連接至RobotBit的舵機接口。

![](./images/servoConRB.jpg)

![](./images/2kservoConRB1.jpg)

    啡色接負極，紅色接正極，橙色接數據

## MakeCode編程教學

![](./images/mcbanner.png)

![](../meowbit/images/acbanner.png)

### 此模組可供Microbit和Meowbit使用。

### ArmourBit與RobotBit的編程是一樣的。

### ArmourBit

### 加載PowerBrick插件：https://github.com/KittenBot/pxt-powerbrick

### [詳細方法](../Makecode/powerBrickMC)

### RobotBit

### 加載RobotBit插件：

![](./images/robotbitExtension.png)

### [詳細方法](../Makecode/powerBrickMC)

### 舵機積木塊:

![](./images/servoblocks.png)

## 舵機編程

![](./images/servo.png)

[參考程式下載](https://bit.ly/PowerbrickM12_01Hex)

[參考程式網址](https://makecode.microbit.org/_APuPfVUHtMpe)

### Makecode教學短片

[![](./images/geekservotut.png)](https://www.youtube.com/watch?v=gUR2DbgVTCQ)

### Meowbit:

---

### 加載robotbit插件：https://github.com/KittenBot/meow-robotbit

### [詳細方法](../Makecode/powerBrickMC)

### 電機積木塊:

![](../motors/images/motorblocks.png)

## 電機編程

![](../motors/images/servocode_meow.png)

[參考程式網址](https://makecode.com/_WrrEcRhMm0o4)

## 插件版本與更新

插件可能會不定時推出更新，改進功能。亦有時候我們可能需要轉用舊版插件才可使用某些功能。

詳情請參考: [Makecode插件版本更換](../Makecode/makecode_extensionUpdate)

## KittenBlock編程教學

![](./images/kbbanner.png)

### Armourbit，Robotbit與Meowbit編程方法一樣，請加載相應插件

### 加載PowerBrick插件

在左上角小貓logo旁邊的硬件欄選擇PowerBrick，加載Microbit與Powerbrick插件。

![](./kbimages/addextension.png)

### 舵機積木塊

![](./kbimages/kbservoblocks.png)

### 舵機編程

![](./kbimages/kbservo.png)

[參考程式下載](https://bit.ly/PowerbrickM12_01sb3)

## FAQ

1：為什麼我點擊積木塊沒有反應呢？

首先確保已經連接好Microbit，然後上載韌體再試一試。