# Robotbit 在Kittenblock編程

Robotbit亦支援在Kittenblock上編程。

有關Kittenblock的介紹可以參考：[Kittenblock大全](../KittenBlock/index)

## Kittenblock編程

![](../../functional_module/PWmodules/images/kbbanner.png)

首先將Microbit用USB線連接到電腦。

在左上角小貓logo旁邊的硬件欄選擇硬件，加載Robotbit的插件。

![](../RBimage/add.png)

在Microbit的積木欄中按下感嘆號 ( ! ) 按鈕。

![](../../functional_module/PWmodules/kbimages/kbmbcon.png)

然後點選『開始連線』。

![](../../functional_module/PWmodules/kbimages/kbmbcon1.png)

連接完成！

![](../../functional_module/PWmodules/kbimages/kbmbcon2.png)

成功連接後，MicroBit會顯示心形。

假如沒有顯示心形，可以按下升級韌體。

![](../../functional_module/PWmodules/kbimages/upload.png)

#### 加載成功

![](../RBimages/success1.png)

### 1. 電機編程

![](../RBimage/robotbit_motorKB.png)

Kittenbot每款電機的詳細教學可以參考：[電機教學](../../motors/index)

示範接線與編程：

將電機連接在robotbit的M1A和M1B上。

![](../RBimage/motor_wire.png)

    電機速度範圍由-255至255

![](../RBimage/kb_code1.png)

### 2. 舵機編程

Kittenbot每款舵機的詳細教學可以參考：[舵機教學](../../motors/index)

示範接線與編程：

將舵機連接在Robotbit的S1上。

    將舵機的橙色線接到黃色引腳針線，紅色線接到紅色正極針線，黑色線接到黑色負極針線。

![](../RBimage/servo_wire.png)

    由於舵機轉動需要時間，所以我們需要加一個短暫的停頓(pause)，給予舵機足夠時間轉動。
    一般舵機的轉向角度範圍由0至180度
    
![](../RBimage/kb_code2.png)

### 3. 步進電機編程

Kittenbot每款電機的詳細教學可以參考：[電機教學](../../motors/index)

示範接線與編程：

將步進電機連接到Robotbit的M1和M2上（將紅色電線連接到VM）。

![](../RBimage/stepper_wire.png)

    步進電機的角度範圍為-360至360度

![](../RBimage/kb_code3.png)

### 4. 蜂鳴器編程

使用蜂鳴器時，不可以拔除P0的Jumper線帽。

![](../RBimage/kb_code4.png)

### 5. RGB燈編程

    所有積木都需要加一個”顯示”的積木才會顯示效果。

#### 5.1 4顆燈同時點亮

![](../RBimage/kb_code5.png)

#### 5.2 使用RGB數值指定顏色

    RGB的數值範圍由0-255。

![](../RBimage/kb_code6.png)

#### 5.3 點亮指定一顆燈

    燈的編號由0至3。(Robotbit上也印有編號)
    
![](../RBimage/robotbit_neopixel2.png)

![](../RBimage/kb_code7.png)

### 6. 引腳編程

引腳的讀寫需要用到Microbit的積木塊。

![](../RBimage/robobit_pinKB.png)

    Pin 0-2可以用作類比引腳，其他Pin只可以用作數位引腳。
    類比數值範圍由0-1023，數位數值範圍由0至1。
    
![](../RBimage/robobit_pinKB1.png)

#### 6.1 引腳數值讀取

    Pin 0預設與蜂鳴器相接，所以使用Pin 0引腳時需要拔除跳線帽。

![](../RBimage/robobit_pinKB2.png)

#### 6.2 引腳數值寫入

    Pin 0預設與蜂鳴器相接，所以使用Pin 0引腳時需要拔除跳線帽。

![](../RBimage/robobit_pinKB3.png)