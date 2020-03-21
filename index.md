# Robotbit

## 購買鏈接

__轉到網上購買__----------→[Robotbit v2.2](https://kidslab.boutir.com/i/SXu22lAAA)

## 產品名稱：

RobotbitV2.2    
適用人群：小學生/培訓機構/家長/愛好者 配套Microbit進行使用   

## 配送清單

- RobotbitV2.2 X1   
- 其他配套Microbit或者矽膠保護套、電池根據實際購買套餐配送     
- KittenBot團隊專為Microbit量身定做的優秀機器人擴展板。現還有配套3D打印保護殼     

## 產品特色  

- 具有強大的直流電機、步進電機、舵機的驅動能力，板載RGB燈與蜂鳴器，並把Microbit空閑引腳全部引出，支持arduino以及市面上的常見電子模塊。     
- 自帶18650電池座，集成鋰電池升壓、充電、保護芯片。支持外部電源輸入。      
- 支持擴展至KittenBot機器人底盤以及樂高標準孔。強大的驅動能力與自帶電池可使DIY更加方便自由。      
- 受到學校老師培訓機構和個人愛好者的一致好評，microbit教學/diy選擇Robotbit不會有錯！  

![](D:/kittenbothk/source/_static/image/01.jpg)

## 產品參數 

- 產品尺寸：78mm x 57mm x 23mm   
- PCB板厚 ： 1.5mm   
- 小孔直徑 ： 3.0mm   
- 大孔直徑 ： 4.8mm   
- 凈重（不含包裝）:37.5g   

![](D:/kittenbothk/source/_static/image/robotbitSize.png)   

## 功能性參數  

- 18650電池電壓：3.7V   
- USB輸入電壓：5V   
- VM引腳最大：1A（在板載電池的支持下）   
- 綠色端子電壓(外部電源輸入)：5V（最大支持6V輸入，切勿接超6V的電壓，最大電流支持3A）   

## 軟件支持 

配套硬件：Microbit   

編程方式：Kittenblock(基於Scratch3.0) / Makecode /python（Mu editor）   

### MakeCode微軟官方 

![](D:/kittenbothk/source/_static/image/04.png)  

在makecode添加包中直接搜索Robotbit（小喵科技的擴展板插件已經通過微軟官方認證，是實力的象征）   
在小喵makecode離線版本中，添加包列表可以顯示Robotbit以及其他集成擴展包（Robotbit可以離線加載不依靠網絡，其他的擴展包不可以）  

![](D:/kittenbothk/source/_static/image/06.png)   


### KittenBlock（小喵家圖形化編程軟件 基於Scratch 3.0） 

選擇microbit硬件後，可見左側自動加載包含Robotbit的插件分欄可供使用。  

![](D:/kittenbothk/source/_static/image/05-0.png) 

![](D:/kittenbothk/source/_static/image/05.png)  

### python支持   

如果你已經習慣代碼編程，想通過microbit上手python，你有兩個選擇 

- 直接使用Mu Editor，需要下載喵家定制的版本 [前往下載](https://www.kittenbot.cn/Mu)

先給microbit刷入一個空程序。 
![](D:/kittenbothk/source/_static/image/08-0.png)  

接著打開REPL窗口，輸入import robotbit後按回車鍵【加載robotbit模塊】，下一行輸入robotbit. 並按下左側Tab鍵【查看robotbit的所有可用方法】  

![](D:/kittenbothk/source/_static/image/08-1.png)  

你也可以直接點擊上方的Example調出簡單的例子  

![](D:/kittenbothk/source/_static/image/08.png)  

- kittenblock的python代碼編程模式  

通過積木塊搭建好程序段後，點擊舞台代碼切換按鈕，調出micropython代碼框

![](D:/kittenbothk/source/_static/image/07.png)      




## 硬件接口 

![](D:/kittenbothk/source/_static/image/02.png)   

1. 5V外部電源端子（防反接）   
2. 電源開關   
3. 電源指示燈   
4. 電量指示燈   
5. Micro充電口   
6. 4路直流電機/2路28BYJ步進電機   
7. 蜂鳴器跳線帽   
8. 8路IO（對應Micro：bit P0-P2、P8、P12-P15）   
9. 5V與GND排針   
10. 無源蜂鳴器   
11. 8路舵機3PIN接口   
12. I2C接口（可拓展I2C模塊）   
13. 18650鋰電池座   
14. 電池保護激活按鈕   
15. Microbit插槽   
16. 4路全彩RGB   

![](D:/kittenbothk/source/_static/image/03.png)  

17. 舵機驅動芯片   
18. 電機驅動芯片   
19. 標準KittenBot機器人底盤固定孔   
20. 標準樂高孔   


<!-- ## 版本叠代更新說明  

Robotbit作為一款有活力的Microbit擴展板，已經經歷過兩次的大叠代更新，每次的更新都是比前面一代更加智能更加好用。   
Robotbit版本起於2017年11月初的V1.2，中間經歷了V1.3，2018年6月中發布V2.0（由於改動提升比較大，版本直接跳到V2.0）    -->

<!-- ## V2.0版本比前面版本更新的內容：   

### 1. 增加IO接口  

V1.3只引出3個可編程IO   
V2.0在原P0-P2基礎上增加P8、P12-P15，一共8個可編程IO足以應對平常的DIY項目（巡線+避障so easy！） 

### 2. 改進電池放電方案 

充電不易發燙，但依然保持快速大電流充電的特性

### 3. 改進電源開關電路設計 

船型開關完全控制電路中所有電源的通斷，解決關閉電源待機情況下會有耗電的問題。 

### 4. 增加外接電源接口   

5V防反接，再外部電源的供電下，支持接大直流電機（如金屬減速電機）和大舵機（如MG995）時使用。   
支持的電流決定於外部電源5V的電流，小喵在5V3A的外部電源支持下嘗試過驅動4個MG995沒問題  

### 5. 外接電源 VM接口的電流上限3A   

### 6. 增加獨立的電池保護芯片   

摒棄前面版本的一體方案，采取高成本的獨立芯片方案，更好的應對過放過充的情況。

### 7. 增加電池保護激活按鈕   

在過流，或者短路，或者打開開關插拔電池這些瞬間異常大電流情況下，電池保護芯片會啟動工作，保護電路的安全性。在確保更正錯誤後，點擊電池激活按鈕，即可恢覆正常工作模式 

### 8. 蜂鳴器改進   

上移至板頂部,增加蜂鳴器音量，讓做音樂實驗效果更加好   

### 9. 采用全新40P立式microbit插槽，拔插更方便，不傷Microbit金手指。   

### 10. 增加5V和GND各一列排針   

為了更好兼容市面上的模塊，特意增5V和GND各一列。註意Microbit的電壓是3.3V，所以當你使用5V模塊時，Microbit只能作為輸出，不能作為輸入，否則IO口會承受5V的電壓，導致IO口損壞。新手應該在小喵官方的指導下謹慎使用。   

### 11. 電源指示燈與充電指示燈改善   

### 12. 板子上的絲印優化 -->

## Robotbit各個部分詳解 

### 18650電池座

![](D:/kittenbothk/source/_static/image/09.png)  

收到擴展板首先安裝18650鋰電池，註意電池正負極，切勿裝反（雖然防反接功能）   
當第一次安裝電池時，拓展板處於待激活狀態（電源燈不亮），此時需要短按一下電池保護激活按鈕或連接usb供電.
使拓展板進入正常工作模式（如果你重新安裝電池，就需要操作這個步驟）   

### 18650電源開關   

![](D:/kittenbothk/source/_static/image/11.png)   
開關打開後（撥向綠色端子那邊為打開開關），為Micro:bit和擴展板的接口供電（擴展板需要裝上18650電池）  

### Micro usb充電口   

![](D:/kittenbothk/source/_static/image/10.png)    

```attention:: 只能用於充電，不是用於程序下載

```

電腦供電或任意5V 1A或者1A以上的手機充電器均可為KittenBot原廠18650鋰電池充電   
5V1A的充電器約2.5小時充滿，建議充電時關閉電源。充滿會自動截止，指示燈變綠 **不會過沖**  

### 電源與電量指示燈   

![](D:/kittenbothk/source/_static/image/12.png)  

Led（3）為電源指示燈，打開開關後常亮   
Led（1）為充電指示燈，充電過程中常亮，電量充滿後Led（2）常亮   

### Micro:bit立式插槽

![](D:/kittenbothk/source/_static/image/13.png)  

用於安裝Microbit主板，安裝方向：Micro:bit帶按鍵那面（正面）朝4顆LED方向  

即使插反也不會燒，只會控制無反應   

### 4路全彩RGB燈   

![](D:/kittenbothk/source/_static/image/14.png)  

4路RGB燈實際與Micro:bit的P16相連控制   

### 8路舵機標準3Pin接口  

![](D:/kittenbothk/source/_static/image/15.png)  

- 8路舵機實際通過專門的舵機擴展驅動芯片與Micro:bit的I2C口控制,而非IO口控制   

- 擴展板在KittenBot原裝電池狀態下，最多能支持8個9g舵機（總電流＜2A），禁止使用MG995等大電流舵機，以免燒毀擴展板   

- 擴展板在外部電源接口（綠色端子）供電狀態下（5V 3A或者3A以上），最多能支持總電流不超過3A的舵機。  

```attention:: 舵機接口不能作為普通IO口使用，只能驅動舵機 

```

### 支持4路直流電機/2路28BYJ步進電機    

![](D:/kittenbothk/source/_static/image/17.png)   

在KittenBot原裝電池狀態下工作，一共可以同時控制4路（左右兩側合計）TT馬達，或者2路步進電機（與舵機合計總電流＜2A），禁止接大電流電機和大電流步進電機，以免燒毀擴展板   
支持直流電機與步進電機混搭使用（2個直流電機與1個步進電機）（與舵機合計總電流＜2A）   

### 蜂鳴器與跳帽

![](D:/kittenbothk/source/_static/image/21.png)   

- 蜂鳴器跳帽出廠默認已插上，對應蜂鳴器與Micro:bit的P0口連接   
- 如果想正常使用P0口的IO口讀寫功能，需要把蜂鳴器跳帽拔下來   
- 蜂鳴器硬件上的電氣連接與Microbit的Music積木塊是對應的，可直接使用Music控制蜂鳴器 

### Micro:bit的IO口引出

![](D:/kittenbothk/source/_static/image/18.png)  

已經將Micro:bit上P0-P2、P8、P12-P15轉出到擴展板上（P0使用時需要拔掉跳帽）
標準的arduino 3PIN接口，支持市面上的Arduino模塊與常用模塊
P0-P2支持數字讀寫和模擬讀寫，P8、P12-P15只支持數字讀寫
如果需要使用5V輸出模塊，可以接3PIN接口左側的5V電源（3PIN接口的電源默認是3.3V）   

### I2C接口

![](D:/kittenbothk/source/_static/image/19.png)    

可拓展I2C模塊，只能用於插接I2C模塊，不能用於普通IO口讀寫

### 2PIN外接電源端子

![](D:/kittenbothk/source/_static/image/20.png)   

- 雖然有防反接功能，但是還是接線需要註意正負     
- 接線端子支持DC 5V的外部電源供電，推薦5V 2A以上適配器電源供電以滿足拓展板驅動高扭矩舵機的電流需求         
- 內部電源供電時，舵機VM接口電源為18650電池電壓3.7V；當使用外部電源供電時，舵機VM接口的電壓為5V 負載電流最大3A   

## Robotbit新手必看快速入門教程  

### 把18650電池裝到Robotbit上，註意正負

![](D:/kittenbothk/source/_static/image/z1.GIF)   

### 把Microbit插到Robotbit上，註意插接方向

![](D:/kittenbothk/source/_static/image/z4.GIF)

### 點擊電池激活按鈕

![](D:/kittenbothk/source/_static/image/z2.GIF)   

### 打開18650電池開關

![](D:/kittenbothk/source/_static/image/z3.GIF)   

### 打開makecode的網址

![](D:/kittenbothk/source/_static/image/22.png)   

### 搜索robotbit

![](D:/kittenbothk/source/_static/image/23.png)   
![](D:/kittenbothk/source/_static/image/24.png)   

### 把robotbit的一些積木塊拖拽出來進行編程，編程記得對應連接相應的電機舵機等等..

![](D:/kittenbothk/source/_static/image/25.png)   
![](D:/kittenbothk/source/_static/image/26.png)   
![](D:/kittenbothk/source/_static/image/27.png)   
![](D:/kittenbothk/source/_static/image/28.png)   
![](D:/kittenbothk/source/_static/image/29.png)   
![](D:/kittenbothk/source/_static/image/30.png)   
![](D:/kittenbothk/source/_static/image/31.png)    

### 下載前記得用usb先連接Microbit的USB口，點擊下載按鈕

下載後，會彈框提示，請自行選擇保存在Microbit的U盤上 

![](D:/kittenbothk/source/_static/image/32.png)   
![](D:/kittenbothk/source/_static/image/33.png)   

### 控制點陣屏的實驗現象   

![](D:/kittenbothk/source/_static/image/34.png)   

## 有沒有視頻教程？

請直接跳轉網易雲課堂，視頻是之前錄制robotbit的V1.3，編程使用方法上沒有區別，使用上也是大同小異，註意引腳接線即可(另外說明1.3版本的A0-A2對應2.0版本的P0-P2) 
http://study.163.com/course/courseMain.htm?courseId=1005485001&share=2&shareId=400000000501010   

## FAQ常見問題與解答

### 電池插上去沒有，打開開關沒有反應？

檢查是否已經按了電池激活按鈕？   
檢查電池正負是否接反？   
檢查電池是否有電？   

----------

### 電池激活按鈕用什麽用？

在過流，或者短路，或者打開開關插拔電池這些瞬間異常大電流情況下，電池保護芯片會啟動工作，保護電路的安全性。點擊電池激活按鈕，即可恢覆正常工作模式   

----------

### 插上usb電腦找不到Microbit

robotbit上的usb只能用於充電，不能用於下載程序，插到robotbit的usb口上，電腦是不會有反應的   

----------

### 電池插反會不會燒？

不會，robotbit的設計考慮到一般性失誤操作而做了防反接處理。插反不會供電

----------

### Microbit插反會不會燒？

不會，另外Microbit插反只會不工作

----------

### P0引腳控制沒有反應？是不是壞了？

PO是通過跳帽默認連接到板子的蜂鳴器上，可以直接用makecode中的music模塊進行控制蜂鳴器。如果要使用P0口，需要拔掉跳帽

----------

### Microbit上可編程IO口不止8個剩下的都去哪裏了？

Microbit上可編程IO口接近20個，但是很多已經與板子上的點陣按鍵覆用了。考慮到覆用帶來的不方便性對，新手容易帶來誤解，小喵引出了8個（跟板子資源沒有覆用的IO口）已經完全足夠應對日常的DIY。如果你對IO數量有狂熱的追求，可以選擇喵家另外一款擴展板IObit

----------

### 舵機排針可以當編程IO口使用嗎？

不能，舵機s1-s8使用專門的舵機驅動芯片拓展出來，只能用於舵機驅動

----------

### 電機接口那邊的VM有什麽用？

平時使用直流電機是用不到VM，直流電機只需要插A+A-或者B+B-。使用4相5線步進電機的時候，剛好VM就用上了，詳細請看Robotbit控制步進電機的視頻教程

----------

### 板子可以放在金屬表面或者潮濕環境下使用嗎？

不行，會短路的，要註意絕緣

----------

### 綠色端子外部電源應該接幾V電源？插高壓電會燒壞嗎？

只能接5V，高於5V都會燒毀板子，電流建議2~3A，也就是說板子最大支持的電流是3A

----------

### 我按照教程做得，得不到實驗結果

如果實驗得不到對應的結果，請首先檢查自己的接線和程序，一般就是有些小地方遺漏了，請再三檢查下   

### 電路板好像燒壞了，怎麽辦小喵有保修麽？

robotbit在工廠出廠都進行過硬件程序測試，保證了功能的完好性。   
首先先排除下是不是程序使用問題。如果你確定燒壞了，可以寄回來給小喵，小喵只收取元件的成本費，沒有多少錢。具體價格咨詢淘寶客服，根據實際損壞的嚴重性進行評判   
請用購買賬號聯系小喵淘寶店的客服，咨詢相關維修的問題。   

需要寫清楚   

姓名，電話，地址，方便小喵寄回去板子給你   
還有板子問題描述，方便工程師快速定位問題給你維修。謝謝你們的配合這樣會縮短維修的時間   