_進階應用，先看看即可_

# Flask 上使用 Gunicorn

<br>

## WSGI 

1. 是 `Web Server Gateway Interface` 簡稱。
2. 是一個為 `Python 應用程式` 和 `web 服務器` 之間提供 `通用接口` 的規範。
3. 是一個標準化的界面，無論使用的是什麼技術或部署在什麼環境。

<br>

## 使用的動機

1. 當開發 Flask 應用程序時，通常會使用 Flask 自帶的開發服務器運行應用。
2. 當準備將應用部署到生產環境時，使用一個更強大穩定的 WSGI 服務器來運行應用是很重要的。

<br>

## 可以使用的服務器

1. Heroku
2. AWS (Amazon Web Services)
3. GCP (Google Cloud Platform)
4. Azure
5. 其他：DigitalOcean、Linode、Vultr。

<br>

## 使用的好處

1. 效能：Gunicorn 是一個預先設定好的、高效能的 WSGI 服務器，可以處理更多的客戶端請求，比 Flask 自帶的開發服務器更適合用於生產環境。

2. 穩定性：Gunicorn 提供了更加穩定的運行環境，能夠更好地處理錯誤和異常情況，確保應用即使在面對大量請求時也能保持運行。

3. 靈活性：可輕易配置 Gunicorn 滿足具體需求，包括設置工作進程的數量、調整超時設置等。

4. 易於部署：Gunicorn 可配合 Nginx 或 Apache 等 Web 服務器使用，讓應用能夠更容易地被部署和擴展。

<br>

## 安裝和使用

1. 安裝 Gunicorn

    ```bash
    pip install gunicorn
    ```

2. 使用 gunicorn 運行 Flask 應用

    ```bash
    gunicorn -w 4 -b 127.0.0.1:8000 myapp:app
    ```

3. 參數中使用 `-w 4` 表示正在運行 4 個工作進程，`-b 127.0.0.1:8000` 表示 Gunicorn 將綁定到本地 IP 地址和 8000 端口，`myapp` 是 Flask 應用的名字，`app` 是 Flask 應用實例的名字。


<br>


---

_END_

