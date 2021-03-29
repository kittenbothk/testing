# 未來板MicroPython編程5：引腳

## 導入未來板庫

需要先導入未來板的庫才可以使未來板的硬件。

    from future import *
    
## 05: 引腳類

### 1. 引腳初始化

    MeowPin(pin,mode)
    
pin為引腳，例如P1，P2。

mode為模式，有4種模式：
1. 數位輸入：'IN'
2. 數位輸出：'OUT' 
3. 模擬輸入：'ANALOG'  
4. 模擬輸出：'PWM'

### 2. 數位讀取
