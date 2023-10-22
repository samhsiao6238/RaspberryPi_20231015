# 申請 Ngrok

[官網](https://ngrok.com/) 註冊以及驗證

_步驟很簡單，這裡僅單介紹_

<br>

1. 點擊登入

    ![](images/img_32.png)

2. 可使用 Google 帳號

    ![](images/img_33.png)

3. 複製 `Authtoken` 然後保存好即可

    ![](images/img_31.png)

4. 授權，在終端機中執行

    ```bash
    ./ngrok authtoken <複製下來的 Authtoken>
    ```

5. 會顯示儲存授權並顯示路徑

    ![](images/img_34.png)

6. 在終端機起動 Ngrok
   
    ```bash
    ngrok http <指定端口>
    ```

<br>

---

_END_