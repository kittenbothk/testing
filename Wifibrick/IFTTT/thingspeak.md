# ThingSpeak x IFTTT應用教學

ThingSpeak亦都內建了工具讓大家可以透過平台觸發IFTTT程式。

## ThingSpeak官方教學

ThingSpeak有提供官方教學，一切以官方教學為準。

### [ThingSpeak官方教學](https://uk.mathworks.com/help/thingspeak/use-ifttt-to-send-text-message-notification.html?requestedDomain=)

## ThingSpeak x IFTTT應用教學

### 以下內容由KittenBot HK撰寫，一切以官方教學作準。

前往IFTTT並註冊或登入帳號。

![](./images/mc5.png)

建立新程式。

![](./images/mc6.png)

![](./images/mc7.png)

在If This的選項裡選擇Webhooks。

![](./images/mc8.png)

選擇Receive A Web Request。

![](./images/mc9.png)

假如之前沒有使用過Webhook的話，請點Connect。如曾使用此服務的話可以跳過這步驟。

![](./images/mc10.png)

在EventName裏填入一個事件名稱。

![](./images/mc11.png)

然後選擇Then That。

![](./images/mc12.png)

在這個示範會使用電郵，請選擇email。

![](./images/mc13.png)

選擇Send Me an Email。

![](./images/mc14.png)

使用此服務之前需要先啟動，假如曾使用過就不用理會。

![](./images/mc15.png)

按照指示啟動電郵服務。

![](./images/MC16.png)

可以更改電郵的主旨和內容，現在先全部使用預設。

![](./images/mc17.png)

完成之後就可以按Continue。

![](./images/mc18.png)

去到這一步，我們需要返回ThingSpeak設置平台。

在ThingSpeak，前往Apps這個頁面。

![](./images/ts1.png)

在Actions選擇ThingHTTP。

![](./images/ts2.png)

建立新的ThingHTTP。

![](./images/ts3.png)

首先輸入名稱。

![](./images/ts4.png)

然後轉換到IFTTT的頁面。

然之後需要獲取個人的Webhook資料。前往帳戶的My Services。

![](./images/mc19.png)

選擇Webhooks。

![](./images/mc20.png)

選擇Documentation。

![](./images/mc21.png)

在Event的欄位填入您的IFTTT程式事件名稱。

![](./images/ts5.png)

![](./images/ts6.png)

將此連結複製，然後貼上到ThingHTTP的URL一欄上。

![](./images/ts7.png)

最後按Save確認並儲存ThingHTTP。

![](./images/TS8.png)

在Apps頁面選擇React。

![](./images/ts9.png)

建立新React。

![](./images/ts10.png)

假如你的ThingSpeak頻道數據是數字格式，請選擇Numeric。在Action選擇ThingHTTP和你的React。然後剔選每次條件吻合都觸發的選項。

![](./images/ts11.png)

試一下對ThingSpeak頻道發送數據，假如條件吻合的話你應該會收到電郵。

![](./images/mc26.png)

