# 五路巡線模組

五路巡線模組



這是一隻巡線模組，它有五顆巡線感應器，它返回的數值是類比形式。

感應器收到的光度越少（遇上黑線），返回的數值就會越低。

## 產品參數

- 工作電壓：3V-5V
- 感應器間距：11mm
- 固定孔直徑：5mm
- 感應距離：1cm-5cm
- 接口：杜邦線

## 接線教學

五路巡線模組可以接3v或5v電源。

    由於這是類比模組，所以只能使用robotbit的PIN0-2。（使用PIN0的話需要拔除蜂鳴器跳線帽）

![](./images/line_wire.png)

## MakeCode編程教學

![](./PWmodules/images/mcbanner.png)

### 加載robotbit插件：https://github.com/KittenBot/pxt-robotbit

#### 巡線感應器編程

    巡線感應器返回的數值可能會因環境而改變，例如感應器高度、巡線膠紙的顏色和物料等。建議在使用次測試和調較一下觸發巡線的數值。

![](./images/line_code.png)

[參考程式網址](https://makecode.microbit.org/_c7rXpLY791Cw)

## 插件版本與更新

插件可能會不定時推出更新，改進功能。亦有時候我們可能需要轉用舊版插件才可使用某些功能。

詳情請參考: [Makecode插件版本更換](../../Makecode/makecode_extensionUpdate)

## KittenBlock編程教學

![](./PWmodules/images/kbbanner.png)

### 加載Robotbit插件

![](./images/addRB.png)

#### 巡線感應器編程

    巡線感應器返回的數值可能會因環境而改變，例如感應器高度、巡線膠紙的顏色和物料等。建議在使用次測試和調較一下觸發巡線的數值。

![](./images/line_code2.png)