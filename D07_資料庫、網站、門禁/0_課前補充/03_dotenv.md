# dotenv

<br>

## 說明

1. `dotenv` 是一個 Python 庫，用於將 `.env` 文件中的變量加載到環境變量中。
   
<br>

2. 透過這個方式管理私密資訊如 API 密鑰、數據庫密碼等非常有用，可避免將這些信息硬編碼在公開的代碼中。

<br>

## 步驟

1. 安裝 `python-dotenv` 。

   ```bash
   pip install python-dotenv
   ```

<br>

2. 在專案根目錄下創建一個 `.env` 文件。

<br>

3. 在 `.env` 文件中添加環境變量：以 `KEY=VALUE` 的格式添加到 `.env` 文件中。

   ```
   DATABASE_PASSWORD=yourpassword
   API_KEY=yourapikey
   ```

<br>

4. 在腳本中導入並加載 `dotenv` 。
   
   ```python
   # 導入
   from dotenv import load_dotenv
   # 載入
   load_dotenv()
   ```

<br>

5. 將 `.env` 文件加入 `.gitignore`：避免私密信息傳到版本控制系統。

   ```
   .env
   ```

<br>

6. 特別說明，使用 `.py` 與 `.ipynb` 檔案讀取環境參數時，當 `.env` 內容發生變動，  `.py` 會讀取到新的內容，而 `.ipynb` 則必須重啟核心，否則會快取原本的數據。

<br>

## 使用範例

_以下以資料庫連線為例_

<br>

1. 在 `.env` 文件中存儲資料庫連接的密碼和 API 密鑰。

    ```txt
    DATABASE_PASSWORD=yourpassword
    API_KEY=yourapikey
    ```

<br>

2. 接著在 Python 脚本中導入庫並載入環境變數，接著就是使用環境變數。

    ```python
    import os
    # 導入庫
    from dotenv import load_dotenv

    # 加載 .env 文件中的環境變數
    load_dotenv()

    # 使用環境變數
    database_password = os.getenv("DATABASE_PASSWORD")
    api_key = os.getenv("API_KEY")

    # 可是是輸出看看
    print(f"Database Password: {database_password}")
    print(f"API Key: {api_key}")
    ```

<br>

---

_END_