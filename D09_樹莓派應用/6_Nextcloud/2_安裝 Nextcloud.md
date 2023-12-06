# 安裝與配置 Nextcloud

<br>

## 步驟說明

1. 切換到要安裝 Nextcloud 的資料夾：這是樹莓派系統預設的 Web 服務器資料夾。

    ```bash
    cd /var/www/html
    ```

<br>

2. 透過 `wget` 指令下載 Nextcloud 安裝檔案。

    ```bash
    sudo wget https://download.nextcloud.com/server/releases/latest.tar.bz2
    ```

    ![](images/img_11.png)

<br>

3. 透過 `tar` 指令進行解壓縮：解壓縮需要一點時間，過程中畫面沒有變化，請耐心等待。
    
    ```bash
    sudo tar -xjf latest.tar.bz2
    ```

    ![](images/img_38.png)

<br>

4. 設定權限：需要一點時間，這將設定 Nextcloud 目錄 `/var/www/html/nextcloud` 的所有權限，包含 `chown` 更改所有權、`chmod` 設置目錄與文件權限。

    ```bash
    sudo chown -R www-data:www-data /var/www/html/nextcloud && sudo find /var/www/html/nextcloud/ -type d -exec chmod 750 {} \; && sudo find /var/www/html/nextcloud/ -type f -exec chmod 640 {} \;
    ```

<br>

5. 建立 Nextcloud 設定檔 `nextcloud.conf`：這是自訂的文件，預設沒有這個檔案。

    ```bash
    sudo nano /etc/apache2/sites-available/nextcloud.conf
    ```

<br>

6. 貼上以下內容：特別注意， Apache 配置文件並無縮排規定，以易讀為主即可，完成後儲存退出。

    ```ini
    Alias /nextcloud "/var/www/html/nextcloud"

    <Directory /var/www/html/nextcloud>
        Require all granted
        AllowOverride All
        Options FollowSymLinks MultiViews

        <IfModule mod_dav.c>
            Dav off
        </IfModule>

    </Directory>
    ```

<br>

7. 啟用站點配置文件：告知 Apache 按照配置文件服務網站。

    ```bash
    sudo a2ensite nextcloud.conf
    ```

<br>

8. 出現提示訊息說要重新載入 `apache2`：不過我們的設置還未完成，所以暫且不用執行 `systemctl reload apache2` 無妨。

    ![](images/img_12.png)

<br>

9. 啟動必要模組：Nextcloud 運行所必要的模組。

    ```bash
    sudo a2enmod rewrite headers env dir mime
    ```
    
    ![](images/img_13.png)

<br>

10. 查詢 `nginx` 服務狀態：因為我們要使用的是 Apache，避免服務在端口上產生衝突，所以會將 nginx 關閉，不過同學在前面的章節中應該知道如何管理讓它們共存，這裡僅是基於讓環境更單純作為考量，並非絕對程序。

    ```bash
    sudo systemctl status nginx
    ```

    ![](images/img_14.png)

<br>

11. 假如 `nginx` 服務的狀態是啟用中：透過以下指令進行停用。

    ```bash
    sudo systemctl stop nginx
    ```

<br>

12. 查詢 `apache2` 服務狀態：需要的狀態是 `active` 。

    ```bash
    sudo systemctl status apache2
    ```

    ![](images/img_15.png)

<br>

13. 如需前一個步驟顯示尚未啟用 `apache2` ：立即啟用 Apache 服務並設定為開機啟動。

    ```bash
    sudo systemctl start apache2 && sudo systemctl enable apache2
    ```

<br>

14. 假如有修改設定文件：必須透過 `restart` 指令重啟 Apache 服務。

    ```bash
    sudo systemctl restart apache2
    ```

<br>

15. 安裝套件 `software-properties-common` ：這是管理軟件來源和 PPA 的工具，以下程序所需。

    ```bash
    sudo apt install -y software-properties-common
    ```

    ![](images/img_18.png)

<br>

16. 安裝兩個套件： `certificates` 包含了一系列被信任的證書， `apt-transport-https` 讓 APT 可通過 HTTPS 協議訪問軟件倉庫。

    ```bash
    sudo apt install ca-certificates apt-transport-https
    ```

    ![](images/img_25.png)

<br>

17. 下載公鑰：從指定的 URL 下載 GPG，並且儲存到系統中。

    ```bash
    wget -q https://packages.sury.org/php/apt.gpg -O- | sudo tee /etc/apt/trusted.gpg.d/php.gpg
    ```

<br>

18. 出現可怕的一堆亂碼：會先嘗試檢驗這亂碼是否影響運行。

    ![](images/img_26.png)

<br>

19. 用 gpg 命令來列出密鑰：可查看密鑰是否正確下載達到驗證目的。

    ```bash
    sudo gpg --show-keys /etc/apt/trusted.gpg.d/php.gpg
    ```

<br>

20. 繼續進行安裝：既然檢查程序都正確，對前面顯示的亂碼不予理會。

    ![](images/img_27.png)

<br>

21. 手動添加資源列表。

    ```bash
    echo "deb https://packages.sury.org/php/ bullseye main" | sudo tee /etc/apt/sources.list.d/php.list
    ```

<br>

22. 進行更新。

    ```bash
    sudo apt update && sudo apt upgrade -y
    ```

<br>

---

_END：以上若可順利完成更新，再進入下一個步驟_
