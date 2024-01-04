# [專題]智慧照護穿戴裝置之Discord Bot

![](https://img.shields.io/badge/Python_3.11.5-Version-FFFF00?logo=python) ![](https://img.shields.io/badge/Discord_2.3.2-Version-5865F2?logo=discord)


## 簡介
基於智慧照護穿戴裝置功能需求的DISCORD BOT 及硬體裝置、APP

## Discord Bot
### 套件使用
- discord.py ```撰寫discord bot的核心套件```
- dotenv ```用於控制env檔案的操作```
- loguru ```自訂終端機Log訊息```
- datetime ```產生時間戳```
- json ```處理json檔案```
- geopy ```能將經緯度轉換為實際地址```
- ast ```用於安全地解析 Python 字符串，提供 literal_eval 函數，避免執行潛在的不安全代碼。```
- sys ```用於將項目的路徑添加到 Python 解釋器的模組搜索路徑中，以便能够導入項目中的模組```
- googletrans ```使用google翻譯 api製作的套件(和google無直接關聯)```
- pyairtable ```用於與airtable連線進行讀寫檔案及查詢的功能```

## 自訂module
- Address_Locator >可以透過座標查詢地址並回傳
- TextInputEdit >改寫discord.ui的TextInput方法
- Datetime >產生當前時間戳

## 功能介紹
### 指令相關功能
>文字指令
- sync ```更新指令如果有新增其他功能```
- status ```查詢機器人當前已載入的擴充```
- ping ```查詢機器人的延遲時間```  

---
>斜線指令
- thread_create ```選擇特定貼文頻道新增貼文並上傳預設訊息```
- forum_create ```創建一個預設名稱的貼文頻道```
- modal_call ```呼叫表單填寫並在送出後返回資料```
- 新增穿戴裝置 ```根據使用者輸入的穿戴裝置id及自訂名稱新增至dc bot的紀錄中```
---
>非指令類型
- 透過Arduino傳遞webhook訊息給dc bot做接收並上傳至airtable同時產生log

```該功能使用到ON_MESSAGE事件監聽函式檢測```

- 如果指令發生錯誤可根據發生問題找到源頭伺服器並且傳送至名為```錯誤通知區```的頻道
  
---
>Discord Bot檔案結構
```
SmartCare_Wearable_Device_Discord_Bot
├─ .gitignore
├─ cogs
│  ├─ ButtonUI.py
│  ├─ ButtonUIS.py
│  ├─ CreateForum.py
│  ├─ CreateThread.py
│  ├─ DeviceAdd.py
│  ├─ GetData.py
│  ├─ ModalChek.py
│  ├─ System.py
│  └─ TestCommand.py
├─ core
│  └─ classes.py
├─ Device_Data
├─ ImportFunction
│  ├─ Address_Locator.py
│  ├─ Datetime.py
│  ├─ Modaltemplate.py
│  ├─ Register.py
│  └─ TextInputEdit.py
├─ main.py
├─ README.md
└─ User_Data
   └─ User_Data.json
```

## Arduino

### 使用的硬體及模組感測器
- Esp系列開發版
- neo gps GPS定位感測器
- MAX30102 血氧濃度檢測模組

### 功能列表
- 可將感測之資料以webhook形式傳遞至discord伺服器中的頻道
- 查詢當前位置之經緯度(暫無)
- 感測穿戴者當前心跳及血氧濃度(暫無)

  ## APP
  ### 待開發
  - 透過裝置ID搜尋當前裝置資料(可切換)
  - 設定完後預設顯示當前首筆最新資料(重啟APP自動刷新及待於頁面可手動刷新)
