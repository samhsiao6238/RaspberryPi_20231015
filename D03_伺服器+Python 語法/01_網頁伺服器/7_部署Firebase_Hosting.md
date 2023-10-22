# Firebase Hosting


<br>

## 安裝


1. 下載 Node.js 的 16.x 版

    ```bash
    curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -
    ```

    ![](images/img_49.png)

2. 安裝
    
    _node.js_
    ```bash
    sudo apt install -y nodejs
    ```
    
    _firebase-tools_
    ```bash
    sudo npm install -g firebase-tools
    ```

<br>

## 開始部署

1. 登入
   
   ```bash
   firebase login
   ```

2. 允許登入
   
   ![](images/img_50.png)

3. 複製網址在樹莓派上開啟瀏覽器貼上（一定要）   

    ![](images/img_52.png)

4. 完成認證
   
   ![](images/img_53.png)

5. 終端機會顯示成功

    ![](images/img_54.png)

6. 初始化

    ```bash
    firebase init
    ```

