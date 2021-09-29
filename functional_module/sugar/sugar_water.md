# Sugar 雨滴水位模組

![](./images/water1.png)

這是一隻雨滴水位模組，可以檢測雨滴和水位。背後亦設有塑膠積木孔，可以完美配搭塑膠積木使用。

## 產品參數

- 尺寸：24 x 24 x 23 mm
- 重量：6.7g
- 訊號：模擬信號0~1023/0~4095

## 產品接線

用3Pin 連接線將模組與Robotbit Edu連接起來。

![](./images/water_wire.png)

## MakeCode編程教學

![](../PWmodules/images/mcbanner.png)

### 加載Sugar插件：

### 在擴展頁直接搜尋sugar (sugar已經過微軟認證，可以直接搜尋)

![](./images/sugar_search.png)

### 你亦可以用插件地址搜尋

Sugar插件：https://github.com/KittenBot/pxt-sugar

### [詳細方法](../../Makecode/powerBrickMC)

![](./images/water_mc_code.png)

[參考程式](https://makecode.microbit.org/_Mygbym8KK5vs)

### Kittenblock 編程教學

![](../PWmodules/images/kbbanner.png)

![](./images/water3.png)

### MicroPython 編程教學

    WaterLevel(pin)
    value()

- value(): 模擬信號0~1023/0~4095

參考程式

    from future import *
    
    from sugar import *
    
    waterlevel_P0 = WaterLevel('P0')
    
    x = 0
    
    screen.sync = 0
    while True:
      screen.fill((0, 0, 0))
      screen.text(waterlevel_P0.value(),5,10,2,(0, 119, 255))
      screen.refresh()


