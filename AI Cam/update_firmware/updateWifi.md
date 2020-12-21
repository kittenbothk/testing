# KOI Wifi固件更新

Kittenbot會不定時推出KOI Wifi固件，提升穩定性和改善功能。

以下會講解一下檢查和更新固件版本的方法。

![](../../functional_module/PWmodules/images/mcbanner.png)

#### 我們先加載KOI Wifi插件：

#### https://github.com/KittenBot/pxt-koi

### [詳細方法](../makecodeQs.md)

## 檢查固件版本

首先編寫以下程式將KOI連上路由器。

插件版本：0.6.4或之後

![](./images/updateCode1.png)

[參考程式下載](https://makecode.microbit.org/_07dVj25FFJCy)

插件版本：0.5.7或之前

![](./images/updateCode2.png)

[參考程式下載](https://makecode.microbit.org/_YAiLoH9XoPta)

將程序上載至Microbit之後等待KOI連上網絡。

按下A按鍵，Microbit的屏幕上會顯示KOI的IP地址。請將IP地址抄寫下來。

    假如你有網絡路由器的管理員權限，您可以直接到網絡路由器的頁面中查找閣下KOI的IP地址，不用慢慢抄寫。


然後請打開瀏覽器，在搜尋欄輸入剛抄寫下來的IP地址然後按Enter。

    例如，我的IP地址是192.168.2.117，我就將它輸入到瀏覽器然後按Enter前往。
    
![](./images/update4.gif)

    固件版本就會顯示在KOI Wifi介面。
    
![](./images/update2.png)


## 更新KOI Wifi固件

下載最新版本的固件：[v2.95](https://bit.ly/KOIWifiFW295)

根據以上方法進入到KOI Wifi的介面。

在左邊的菜單中選擇Upgrade Firmware。

![](./images/update5.png)

根據提示，選擇正確的user.bin。

![](./images/update6.png)

頁面提示我們要上載user2.bin，所以我們選擇相應的檔案。

![](./images/update8.png)

完成下載更新。

![](./images/update7.png)