(MakeCode 中編程)

# Makecode 編程與Kittenbot自家IoT平台

![](../../functional_module/PWmodules/images/mcbanner.png)

## 前言：

在這節教程，我們將會學習使用WifiBrick和KOI與Kittenbot自家IoT平台溝通。

## 第一步：平台準備

請先登入Kittenbot IoT，然後建立一個新話題。

假如你需要建立一個私人話題，請填入用戶名與密碼。

![](./iotimage/kittenbot_1.png)

## 第二步：編寫程式

平台準備好之後就可以開始編程。

### 使用Wifibrick

打開MakeCode。

### 加載Kittenbot插件：

### 在擴展頁直接搜尋Kittenbot (Kittenbot已經過微軟認證，可以直接搜尋)

### 選擇KittenWiFi和Powerbrick或Robotbit

![](./iotimage/wifi_search.png)

      請按自己的硬件選擇Powerbrick或Robotbit插件。


KittenWifi的插件裏預設的伺服器就是KittenBot的平台，所以可以直接使用。

![](./iotimage/kittenbot_2.png)

組合出以下程式，並填入自己的Wifi資料和話題名稱。

在程式按下A鍵就可以將亮度感測值傳上伺服器。

在平台上手動發布”happy”或”sad”，Microbit會顯示相應圖案。

![](./iotimage/kittenbot_3.png)

[參考程式](https://makecode.microbit.org/_D4J7wX7uRhtV)

### 使用KOI

打開MakeCode。

### 加載Kittenbot插件：

### 在擴展頁直接搜尋Kittenbot (Kittenbot已經過微軟認證，可以直接搜尋)

### 選擇KOI和Powerbrick或Robotbit

![](./iotimage/wifi_search.png)

      請按自己的硬件選擇Powerbrick或Robotbit插件。

KOI的插件裏預設的伺服器就是KittenBot的平台，所以可以直接使用。

![](./iotimage/kittenbot_5.png)

KOI的使用方法和WifiBrick類似，分別在於KOI不會自動讀取數據，需要我們運行MQTT讀取的積木才會讀取到數據。

組合出以下程式，並填入自己的Wifi資料和話題名稱。

在程式按下A鍵就可以將亮度感測值傳上伺服器。

在平台上手動發布”happy”或”sad”，Microbit會顯示相應圖案。

![](./iotimage/kittenbot_4.png)

[參考程式](https://makecode.microbit.org/_9xm455btKcPi)