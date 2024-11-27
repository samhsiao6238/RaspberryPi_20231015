# 米家

_使用 [MiService](https://github.com/Yonsm/MiService)，暫時先記錄在這裡，之後再看看如何正確分類_

<br>

## 建立開發環境

_虛擬環境與套件_

<br>

1. 建立新的虛擬環境。

    ```bash
    python -m venv envMiHome
    ```

<br>

2. 安裝 `miservice` 所有可能需要的套件。

    ```bash
    pip install -q aiohttp aiofiles requests pandas
    ```

<br>

3. 使用 `--no-build-isolation` 跳過構建隔離並重新安裝。

    ```bash
    pip install miservice --no-build-isolation
    ```

<br>

4. 在開啟的終端機視窗中設定環境變數。

    ```bash
    export MI_USER=<自己的米家帳號>
    export MI_PASS=<自己米家帳號的密碼>
    ```

<br>

5. 若使用 `.env`。

    ```json
    MI_USER=
    MI_PASS=
    MI_DID=
    OPENAI_API_KEY=
    ```

<br>

## 啟用筆記本

1. 
