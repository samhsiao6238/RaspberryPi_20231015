*上課實作*

## 參考
[HiveMQ 官網](https://www.hivemq.com/)

<br>

## 下載應用
[下載](https://www.hivemq.com/downloads/hivemq/)

下載前必須填寫一些資料
![](images/img_41.png)

將下載的檔案複製到目錄內

解壓縮指令
```bash
unzip <檔案路徑>
```

進入目錄
```bash
cd hivemq-4.18.0
```

<br>

## 啟動 HiveMQ 服務

*啟動之前需要先確認已安裝 Java*

更新
sudo apt update

安裝 OpenJDK 11，OpenJDK 是 Java 的開源實作
sudo apt install openjdk-11-jdk

檢查版本
「java -version」

運行 HiveMQ 伺服器
./bin/run.sh

透過腳本方式啟動的 HiveMQ 服務，在關閉終端或重啟樹莓派後會停止運行。
如果想讓 HiveMQ 作為一個系統服務在後台運行，需要建立一個 systemd 服務檔案來管理 HiveMQ。

<br>

## 建立系統服務
sudo nano /etc/systemd/system/hivemq.service

HiveMQ systemd 服務的範例檔案

```ini
[Unit]
Description=HiveMQ MQTT Broker
After=network.target

[Service]
WorkingDirectory=/home/sam6238/Documents/env02/00_RaspberryPi_2023/00_projects/26_HiveMO/hivemq-4.18.0
ExecStart=/home/sam6238/Documents/env02/00_RaspberryPi_2023/00_projects/26_HiveMO/hivemq-4.18.0/bin/run.sh
User=sam6238
Type=simple
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

讓 systemd 重新讀取其配置
sudo systemctl daemon-reload

設定 HiveMQ 在開機時自動啟動
sudo systemctl enable hivemq

立即開始運行
sudo systemctl start hivemq

檢查 HiveMQ 的運行狀態
sudo systemctl status hivemq


在樹莓派安裝套件
pip install paho-mqtt

如果沒有安裝 pip
sudo apt-get install python3-pip

<br>

## 實作練習
### 範例 1
- 撰寫一個基本的範例

```python
import paho.mqtt.client as mqtt
# Callbacks
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("test/topic")
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
# Create client
client = mqtt.Client()
# Assign callbacks
client.on_connect = on_connect
client.on_message = on_message
# Connect to HiveMQ server
client.connect("192.168.1.135", 1883, 60)
# Blocking loop to handle networking, receiving messages, etc.
client.loop_forever()
```

<br>

### 範例 2
以下時做一個發布以及訂閱的互動式專案

```python
# 匯入所需的模組
import paho.mqtt.client as mqtt  # MQTT 客戶端模組
import random  # 用於產生隨機數
import time  # 用於時間相關操作
# 建立一個名為 "Temperature Sensor" 的 MQTT 客戶端物件
client = mqtt.Client("Temperature Sensor")
# 連線到 MQTT 代理伺服器 (Broker)
client.connect("192.168.1.135", 1883, 60)
# 持續運行的迴圈
while True:
    # 產生一個 20.0 到 30.0 之間的隨機溫度讀數
    temperature = random.uniform(20.0, 30.0)  
    # 將溫度讀數發布到 "sensor/temperature" 主題
    client.publish("sensor/temperature", temperature)
    # 暫停 5 秒鐘
    time.sleep(5)  
```

<br>

### 範例 3
```python
# 匯入 MQTT 客戶端模組
import paho.mqtt.client as mqtt
# 定義連線回調函式
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))  # 顯示連線結果
    client.subscribe("sensor/temperature")  # 訂閱 "sensor/temperature" 主題
# 定義接收訊息回調函式
def on_message(client, userdata, msg):
    temperature = float(msg.payload)  # 將訊息內容轉換為浮點數（溫度）
    print("Temperature: " + str(temperature))  # 顯示溫度
    # 如果溫度低於 21.0 或高於 26.0，則發出警告
    if temperature < 21.0 or temperature > 26.0:
        print("Warning: Temperature is out of range!")
# 建立一個名為 "Temperature Monitor" 的 MQTT 客戶端物件
client = mqtt.Client("Temperature Monitor")
# 設定回調函式
client.on_connect = on_connect  # 設定連線回調函式
client.on_message = on_message  # 設定接收訊息回調函式
# 連線到 MQTT 代理伺服器 (Broker)
client.connect("192.168.1.135", 1883, 60)
# 開始執行事件處理迴圈，以處理網路事件、接收訊息等操作
client.loop_forever()
```

<br>

### 範例測試

1. 使用 ngrok
   - 先在樹莓派終端機中啟動 ngrok
   
   ```bash
   ./ngrok tcp 1883
   ```

2. 修改腳本
   - 接著發布與訂閱的連線設定改為
  
    ```python
    # ngrok
    client.connect("2.tcp.ngrok.io", 18139, 60)
    ```

3. 找出進程 ID
    ```bash
    ps
    ```

4. 結束測試
   - 會在背景執行，使用 ` kill ` 進行關閉

---

END