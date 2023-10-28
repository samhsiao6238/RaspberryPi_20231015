_課後補充_

# Flask 教學

<br>

## 建立 Flask 網頁伺服器

首先，我們需要更新系統套件並安裝 Flask。

<br>

1. 更新系統

   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

<br>

2. 安裝 Flask

   ```bash
   pip install flask
   ```

<br>

3. 建立專案資料夾

   ```bash
   mkdir my_flask_app && cd my_flask_app
   ```

<br>

4. 建立專案主程式 `app.py`

   ```bash
   touch app.py
   ```

<br>

5. 使用 VSCode 開啟 `app.py`

   ```bash
   code app.py
   ```

   _在 `app.py` 中輸入以下代碼_

   ```python
   from flask import Flask

   app = Flask(__name__)

   @app.route('/')
   def home():
       return "Hello, World!"

   if __name__ == '__main__':
       app.run(debug=True, host='0.0.0.0')
   ```

<br>

## 運行

1. 啟動 Flask 伺服器

   ```bash
   python app.py
   ```

   此時 Flask 伺服器 `預設`會在本地的 `5000` 端口上運行，可在區網內的其他電腦上通過 `http://<樹莓派IP>:5000/` 來訪問。

   ```bash
   http://192.168.1.135:5000/
   ```
2. 處理防火牆問題

   _如果遇到防火牆擋住訪問，可透過 `ufw` 開放特定的端口_

   ```bash
   sudo ufw allow 5000
   ```
3. 指定端口

   _可以在 `app.py` 中指定一個不同的端口_

   ```python
   from flask import Flask
   app = Flask(__name__)

   @app.route('/')
   def hello():
       return "Hello Raspberry Pi!"

   if __name__ == "__main__":
       app.run(host='0.0.0.0', port=8080)
   ```
4. 在有防火牆的情況下，如果使用不同的端口，也要設定開放該端口的訪問

   ```bash
   sudo ufw allow 8080
   ```

   訪問時指定新的端口

   ```
   http://<樹莓派網址>:8080/
   ```

<br>

---

_END_
