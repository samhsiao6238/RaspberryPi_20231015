# 建立模板 

_Templates in Flask_

<br>

## 說明

在 Flask 中，我們可以使用 Jinja2 模板引擎來動態生成 HTML 頁面。以下是一個基於你提供的筆記，進行加強和補充的指南。

<br>

## 開始

1. 建立 `app.py`，或是既有的主檔案。

   _在代碼中導入除了導入 `Flask` ，並導入 `render_template` 來渲染 HTML 模板。_

    ```python
    # render_template 用於渲染 HTML 模板
    from flask import Flask, render_template
    
    # 建立應用
    app = Flask(__name__)

    # 指定路由
    @app.route('/')
    def home():
        return render_template('index.html')

    if __name__ == '__main__':
        app.run(debug=True)
    ```

<br>

2. 建立模板文件

    _建立 `templates` 資料夾，並在資料夾內新增超文本 `index.html`_

    ```bash
    mkdir -p templates && touch templates/index.html
    ```

<br>

3. 編寫 `index.html`
   
   _在這個文本中，使用 `Bootstrap` 快速搭建一個簡單的導航欄和內容區域。_

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Simple Flask App</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="#">Flask App</a>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item active">
                        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
                    </li>
                </ul>
            </div>
        </nav>
        <div class="container mt-3">
            <h1>歡迎來到我的 Flask 網站</h1>
        </div>
    </body>
    </html>
    ```

<br>

4. 運行 Flask 應用

    ```bash
    python app.py
    ```

5. 啟動服務器後在瀏覽器訪問

    ```bash
    http://127.0.0.1:5000
    ```
    或
    ```bash
    http://localhost:5000
    ```

---

<br>

_END_