# 監聽 Firebase 即時資料庫

_Firebase Realtime Database_

<br>

## 說明

1. 使用 `firebase-admin` 的 Python 套件來實現。
2. 在樹莓派 `背景` 執行一個腳本，並 `監聽` Firebase Realtime Database 的某個指定節點。
3. 可透過手動更新即時資料庫來觀察樹莓派是否確實監聽了資料庫的變動。
4. 透過監聽機制，可將任何邏輯撰寫在監聽到變動時觸發的程式碼區塊，實現類似發佈與訂閱的機制，而且更輕量也更即時。

<br>

## 開始

1. 在樹莓派安裝必要的套件

    ```sh
    pip install firebase-admin
    ```

2. 建立一個 Python 腳本，如 `firebase_listener.py` 。

    ```python
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import db

    def listener(event):
        # 監聽到變動的時候在這裡執行邏輯
        # 暫且打印更新的資料
        print('Listener: {}, {}'.format(event.path, event.data))

    if __name__ == '__main__':
        # 初始化 Firebase 應用
        cred = credentials.Certificate('<自己的 credentials.json 檔案')
        firebase_admin.initialize_app(cred, {
            'databaseURL': '<資料庫網址>'
        })

        # 設置監聽器
        ref = db.reference('<要監聽的節點>')
        # 傳入自訂監聽函數
        ref.listen(listener)

        # 保持腳本運行
        print('Listening for changes...')
        while True:
            pass
    ```

3. 若要在背景執行腳本，可使用 `nohup` 和 `&` 來實現。

    ```sh
    nohup python3 firebase_listener.py &
    ```
   - 這會啟動腳本並將其放到背景執行，即使關閉終端機，腳本也會繼續運行。


<br>

---

_END_