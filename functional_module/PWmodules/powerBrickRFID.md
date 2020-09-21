# RFID魔塊

RFID魔塊 (HKBM8012L) + RFID卡片 (HKBM8012M)

![](./images/10_04.png)

![](./images/10_05.png)

這是一個RFID魔塊，可以對套件附有的RFID卡或者空白RFID卡進行讀寫。

附有的RFID卡有1K內存，有16個分區，每個分區有3個區塊可以寫入資料。

![](./images/IMG_2583.GIF)

## 詳細介紹

![](./images/10_03.png)

## 產品參數

- 支援電壓：3V-5V
- 尺寸：56mm X 56mm X 16mm
- 接口：4pin防反插接口
- 感應距離：大約3cm

## 使用注意事項

- RFID請勿在有強力磁場的環境下使用
- RFID卡與魔塊之間不能有金屬阻擋，否則無法進行讀寫。
- RFID卡寫入大量數據的速度比較慢，請靜待一下，等數據成功寫入再拿去RFID卡。
- 八達通卡身份證之類的卡因為資料被加密所以不能進行寫入數據，只可以讀取UID號碼（每張卡也有獨有的ID）。

## 接線方法

### Armourbit

---

將RFID魔塊用4pin排線連接至Armourbit的I2C接口。

![](./kbimages/rfidcon.jpg)

### Robotbit

--- 
將RFID魔塊連接至Robotbit的I2C接口。

    藍色線（A）請接到SCL，綠色線（B）請接到SDA。

![](./images/rfid_wire1.png)


## MakeCode編程教學

![](./images/mcbanner.png)

### 加載PowerBrick插件：https://github.com/KittenBot/pxt-powerbrick

### RFID魔塊積木塊

![](./images/rfidblocks.png)

### RFID卡片寫入

![](./images/rfidwrite.png)

[參考程式下載](https://bit.ly/PowerbrickM8_01Hex)

[參考程式網址](https://makecode.microbit.org/_XdP0Pye1rFA0)

### RFID卡片讀取

![](./images/rfidread.png)

[參考程式下載](https://bit.ly/PowerbrickM8_02Hex)

[參考程式網址](https://makecode.microbit.org/_TEz6D45qgDaa)

### RFID讀取UUID

每張卡的UUID也不同，請自行抄下你自己卡片的UUID。

![](./images/uidread.png)

[參考程式下載](https://bit.ly/PowerbrickM8_03Hex)

[參考程式網址](https://makecode.microbit.org/_a6wiKdUqWaXL)

### UUID身份辨別

我們可以用UUID作身份辨別。

![](./images/uididentify.png)

    這裡請使用您卡片的UUID。

[參考程式下載](https://bit.ly/PowerbrickM8_04Hex)

[參考程式網址](https://makecode.microbit.org/_c4rcrE76Tc6Y)

### Makecode教學短片

[![](./images/rfidtut.png)](https://www.youtube.com/watch?v=r1B6l7xK7So)

## 插件版本與更新

插件可能會不定時推出更新，改進功能。亦有時候我們可能需要轉用舊版插件才可使用某些功能。

詳情請參考: [Makecode插件版本更換](../../../Makecode/makecode_extensionUpdate)

## KittenBlock編程教學

![](./images/kbbanner.png)

### 加載PowerBrick插件

在左上角小貓logo旁邊的硬件欄選擇PowerBrick，加載Microbit與Powerbrick插件。

![](./kbimages/addextension.png)

### RFID積木塊

![](./kbimages/kbrfidblocks.png)

### RFID卡片寫入

![](./kbimages/rfidwrite.png)

[參考程式下載](https://bit.ly/PowerbrickM8_01sb3)

### RFID卡片讀取

![](./kbimages/rfidread.png)

[參考程式下載](https://bit.ly/PowerbrickM8_02sb3)

### RFID讀取UUID

![](./kbimages/uidread.png)

[參考程式下載](https://bit.ly/PowerbrickM8_03sb3)

### UUID身份辨別

![](./kbimages/uididentify.png)

    這裡請使用您卡片的UUID。
    
[參考程式下載](https://bit.ly/PowerbrickM8_04sb3)

## FAQ

1：為什麼我點擊積木塊沒有反應呢？

首先確保已經連接好Microbit，然後上載韌體再試一試。