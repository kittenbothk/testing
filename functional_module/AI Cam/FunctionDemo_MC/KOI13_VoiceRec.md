# 語音識別 (固件版本: v1.8.2或之後)

我們可以訓練KOI聆聽語音指令。

## 編寫語音識別程式

![](../../PWmodules/images/mcbanner.png)

### 加載KOI插件：https://github.com/KittenBot/pxt-koi


### [詳細方法](../makecodeQs.md)

按鍵積木塊：

![](KOI13/1.png)

編寫程式：

![](KOI13/2.png)

## 程式流程

1: 首先將程式下載到Microbit上。

2: 按下A，錄製第一段指令。錄製成功的話，KOI的畫面會顯示綠色，否則會顯示紅色。Microbit上會顯示語音指令編號。

3: 重複錄製指令，直至成功錄製2-3次為止。

4: 完成第一段錄音之後按下B，Microbit上的語音指令編號會增加。返回步驟2開始訓練下一段指令。

5: 重複步驟2-4，直至完成錄入所有指令。

6: 完成訓練後，同時按下A和B，KOI會開始辨識指令。成功辨認的話會顯示綠色，否則顯示紅色。Microbit上亦會顯示辨識到指令的編號。

## 參考程式

[1. 語音識別HEX下載]()

[1. 語音識別HEX網址](https://makecode.microbit.org/_9Kui7vMu39Ah)

[1. 語音識別HEX下載(v1.8.2)]()

[1. 語音識別HEX網址(v1.8.2)](https://makecode.microbit.org/_V6MeYw0YU4WY)

## FAQ

1：為什麼我重新開機，按下按鍵A，但不能進行顏色校正？

·    答：打開電源後, KOI 及microbit 同時起動; 相對上, Microbit 所需的起動時間比KOI魔塊短, 引致 Microbit的初始化程式已經跑完了，KOI還沒完全起動, 因此按下A鍵沒有反應。

·    解決辦法：打開電源後，重新按下Microbit背後的Reset按鍵，讓Microbit重新開始運行（秘訣就是讓KOI魔塊先完全運行起來，再讓Microbit 跑初始化程式）

2：KOI鯉魚魔塊我直接3V電源可以嗎？

·    答：不行，必須要接5V！

3：如何提高巡線的準確性？

·    答：盡量保持簡潔的背景，並使用與背景顏色有明顯分別的物件。