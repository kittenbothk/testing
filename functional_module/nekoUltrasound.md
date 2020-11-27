# Kittenbot 原廠貓耳造型超聲波模組

Kittenbot 原廠貓耳造型超聲波模組 (HKBM8014A)

![](./images/ultrasound2.png)

這是一隻超聲波測距模組。



## 產品參數

- 工作電壓：5V
- 工作溫度：-25 ~ +80°C
- 測量角度：30°範圍內
- 測量範圍：5~300cm（誤差<1cm）
- 接口：杜邦線



## 接線教學

超聲波模組需要接5v電源。

![](./images/ultraSound1.jpg)

### 超聲波模組v2

超聲波模組v2需要接A(RGB燈)和D(超聲波)接口。

![](./images/ultraSoundv2_wire.png)

### 超聲波模組v1

超聲波模組v1只需要接Ultr接口。

![](./images/ultraSoundv1_wire.png)

## MakeCode編程教學

![](./PWmodules/images/mcbanner.png)

![](../meowbit/images/acbanner.png)

### 此模組可供Microbit和Meowbit使用。

### Microbit:

### 加載robotbit插件：https://github.com/KittenBot/pxt-robotbit

### [詳細方法](../Makecode/powerBrickMC)

### 超聲波模組積木塊：

![](./images/ultraSound_blocks.png)

#### 距離檢測編程：

![](./images/ultraSound_code1.png)

[參考程式網址](https://makecode.microbit.org/_Lt021WgXuWfz)

### RGB燈編程(只限v2)：

![](./images/ultraSound_code2.png)

[參考程式網址](https://makecode.microbit.org/_J9R5xhCwgJqH)

### 示範案例：

![](./images/ultraSound_code3.png)

[參考程式網址](https://makecode.microbit.org/_5vf48tf6xdVc)

### Meowbit:

### 加載robotbit插件：https://github.com/KittenBot/meow-robotbit

### [詳細方法](../Makecode/powerBrickMC)

### 加載neopixel插件：

![](./images/neopixel.png)

### 超聲波模組積木塊：

![](./images/ultraSound_blocks.png)

#### 距離檢測編程：

![](./images/ultrasound_codeMeow1.png)

[參考程式網址](https://makecode.com/_fC6XoUHHR79p)

### RGB燈編程(只限v2)：

![](./images/ultrasound_codeMeow2.png)

[參考程式網址](https://makecode.com/_hs3LykMzV78o)

## 插件版本與更新

Robotbit插件可能會不定時推出更新，改進功能。亦有時候我們可能需要轉用舊版插件才可使用某些功能。

詳情請參考: [Makecode插件版本更換](../../Makecode/makecode_extensionUpdate)


## KittenBlock編程教學

![](./PWmodules/images/kbbanner.png)

### 加載Robotbit插件

![](./images/addRB.png)

#### 距離檢測編程：

![](./images/ultraSound_code4.png)

### RGB燈編程(只限v2)：

![](./images/ultraSound_code5.png)

## Mu Editor編程教學

#### 距離檢測編程：

![](./images/ultraSound_code6.png)

    超聲波模組的原理是使用數位寫入發射訊號，然後量度訊號反彈回到模組的時間，然後將時間乘以音波速度得知距離。
