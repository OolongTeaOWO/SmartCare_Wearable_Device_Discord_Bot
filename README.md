# [專題]智慧照護穿戴裝置之Discord Bot

![](https://img.shields.io/badge/Python_3.11.5-Version-FFFF00?logo=python) ![](https://img.shields.io/badge/Discord_2.3.2-Version-5865F2?logo=discord)


## 簡介

## 套件使用
- discord.py ```撰寫discord bot的核心套件```
- dotenv ```用於控制env檔案的操作```
- loguru ```自訂終端機Log訊息```
- datetime ```產生時間戳```
- json ```處理json檔案```
- geopy ```能將經緯度轉換為實際地址```
- ast ```用於安全地解析 Python 字符串，提供 literal_eval 函數，避免執行潛在的不安全代碼。```
- sys ```用於將項目的路徑添加到 Python 解釋器的模組搜索路徑中，以便能够導入項目中的模組```
- googletrans ```使用google翻譯 api製作的套件(和google無直接關聯)```

## 功能介紹

>指令相關功能
- sync ```更新指令如果有新增其他功能```
- status ```查詢機器人當前已載入的擴充```
- ping ```查詢機器人的延遲時間```  

>非指令類型
- 透過Arduino傳遞webhook訊息並在bot端接收並產生log訊息

```該功能使用到ON_MESSAGE事件監聽函式檢測```

- 如果指令發生錯誤可根據發生問題找到源頭伺服器並且傳送至名為```錯誤通知區```的頻道  

- 如果伺服器設定不傳送系統消息則首次被加入到伺服器後，會自動發布訊息同時讓使用者知道需要新增
  
```錯誤通知區```頻道

>檔案結構

```
Project_Heathly
├─ .gitignore
├─ cogs
│  ├─ GetData.py
│  ├─ slash_command.py
│  ├─ slash_event.py
│  ├─ System.py
│  └─ TestCommand.py
├─ core
│  └─ classes.py
├─ ImportFunction
│  └─ Address_Locator.py
├─ log
├─ main.py
└─ README.md
└─ .env
```
