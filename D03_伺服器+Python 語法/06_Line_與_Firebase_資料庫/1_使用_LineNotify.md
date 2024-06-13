# 建立 LineNotify

- 樹莓派啟動時發送 LineNotify 通知

</br>

## A. 建立 LINE Notify 的 Token

1. 前往 [LINE Notify](https://notify-bot.line.me/en/) 並點擊右上方的登入 `Log in`。

2. 點擊 "My page"。

     ![](images/img_21.png)

3. 發行一個新的 token

     ![](images/img_22.png)

4. 為 Token 命名選擇一個目標群組。

     ![](images/img_24.png)

5. 複製權杖

     ![](images/img_28.png)

</br>

## B. 撰寫腳本

1. 安裝套件
   ```bash
   pip install requests python-dotenv
   ```

2. 安裝時若出現警告
   
   ![](images/img_29.png)

3. 編輯環境參數
   - 避免使用 sudo 直接編輯 .bashrc 或 .env。
   - 使用 sudo 可能會導致這些文件的所有權或權限更改 

   ```bash
   nano ~/.bashrc
   ```

4. 在最後加入一行

   ```bash
   # 加入環境參數
   export PATH=$PATH:/home/sam6238/.local/bin
   ```

5. 儲存後要記得重新載入

   ```bash
   source ~/.bashrc
   ```

6. 若在虛擬環境下執行安裝的時候務必加上 `python -m` 指定使用解釋器
   ```bash
   python -m pip install requests python-dotenv
   ```

7. 建立 .env 環境參數，字串部分有無引號皆可

   ```bash
   nano .env
   ```
   貼上
   ```bash
   _TOKEN=<替換自己的 LineNotify 權杖>
   ```
   

8. 建立一個新的 Python 腳本，例如 `send_line_notify.py`

   ```bash
   sudo nano send_line_notify.py
   ```
   貼上

     ```python
     import requests
     import os
     from dotenv import load_dotenv

     # 載入 .env 文件
     load_dotenv()

     def send_line_notify(msg):
     # 用自己的 token 替換
     TOKEN = os.getenv("_TOKEN") 
     LINE_ENDPOINT = "https://notify-api.line.me/api/notify"
     message = msg
     headers = {
          "Authorization": f"Bearer {TOKEN}",
          "Content-Type": "application/x-www-form-urlencoded"
     }
     data = {"message": message}
     response = requests.post(LINE_ENDPOINT, headers=headers, data=data)
     return response.status_code

     if __name__ == "__main__":
     send_line_notify("\n 樹莓派已開機")
     ```

9.  在終端機內執行一下測試收到通知

    ```bash
    /usr/bin/python /home/sam6238/Documents/send_line_notify.py
    ```
     
     ![](images/img_27.png)


</br>

## C. 設置系統服務

1. 切換路徑

   ```bash
   cd /etc/systemd/system/
   ```
2. 建立一個新的 systemd 服務檔案，例如 `line_notify.service`，

   ```bash
   sudo touch line_notify.service
   ```

3. 編輯服務檔案

   ```bash
   sudo nano line_notify.service
   ```

4. 先去腳本所在資料夾查詢絕對路徑

   ```bash
   pwd
   ```

5. 內容如下：務必記住替換自己的路徑、帳號
   
   ```ini
   [Unit]
   Description=Send LINE Notify on Startup
   After=network-online.target
   Wants=network-online.target

   [Service]
   Type=oneshot
   ExecStartPre=/bin/sleep 10
   ExecStart=/usr/bin/python /home/sam6238/Documents/send_line_notify.py
   User=sam6238
   TimeoutStartSec=0

   [Install]
   WantedBy=multi-user.target  
   ```


6. 啟動並啟用系統服務

   ```bash
   sudo systemctl start line_notify.service
   sudo systemctl enable line_notify.service
   ```

7. 假如修改設定檔案，要重新加載配置

   ```bash
   sudo systemctl daemon-reload
   sudo systemctl restart line_notify.service
   ```


8. 查看服務狀態

   ```bash
   sudo systemctl status line_notify.service
   ```

9.  完成以上步驟後重新開機

    ```bash
    sudo reboot now
    ```

10. 賦予服務執行腳本的權限

    ```bash
    sudo chmod +x /home/sam6238/Documents/send_line_notify.py
    sudo chmod 600 /home/sam6238/Documents/.env
    ```

   
11. 確保文件擁有者

    ```bash
    sudo chown sam6238:sam6238 /home/sam6238/Documents/send_line_notify.py
    sudo chown sam6238:sam6238 /home/sam6238/Documents/.env
    ```

12. 查看日誌

    ```bash
    sudo journalctl -u line_notify.service
    ```
    或僅查看最新的
    ```bash
    sudo journalctl -u line_notify.service -n 50
    ```
    或動態查看
    ```bash
    sudo journalctl -u line_notify.service -n 50 -f
    ```

</br>

---

_END：完成_