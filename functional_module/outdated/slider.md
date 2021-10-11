# 滑動式電位器模組

![](../images/slide1.png)

這是一隻滑動式電位器模組，它可以檢測滑動器位置，它返回的數值是類比形式。

數值範圍由0-1023，數值越大代表位置越高。

## 產品參數

- 工作電壓：3.3V~5V
- 類型：類比模組
- 接口：3Pin托邦線

## 接線教學

    由於這是類比模組，所以只能使用robotbit的PIN0-2。（使用PIN0的話需要拔除蜂鳴器跳線帽）
    
將定位器連接到Robotbit的針線和3V接口。

![](../images/slider_wire.png)

## MakeCode編程教學

![](../PWmodules/images/mcbanner.png)

![](../../meowbit/images/acbanner.png)

### 此模組可供Microbit和Meowbit使用。

#### 讀取電位器位置編程

### Microbit:

![](../images/poten_code.png)

### Meowbit:

![](../images/poten_codeMeow.png)

## KittenBlock編程教學

![](../PWmodules/images/kbbanner.png)

### 加載Robotbit插件

![](../images/addRB.png)

#### 讀取電位器位置編程

![](../images/poten_codekb.png)

## Mu Editor編程教學

#### 讀取電位器位置編程

![](../images/poten_codemu.png)