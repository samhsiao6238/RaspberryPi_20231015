# 安裝 PHP

_務必完成前面的程序才能接續這個小節_

<br>

## 步驟說明

1. 安裝 PHP8.1 等套件。

    ```bash
    sudo apt install php8.1 php8.1-common php8.1-cli php8.1-bcmath php8.1-fpm php8.1-mbstring php8.1-xml php8.1-curl php8.1-gd php8.1-mysql php8.1-pgsql php8.1-sqlite3 php8.1-zip php8.1-readline php8.1-opcache
    ```

<br>

2. 安裝好會顯示以下訊息。

    ![](images/img_28.png)

<br>

3. 設定預設版本：在 `2023/12/06` 時更新到了 `8.3` 。

    ```bash
    sudo update-alternatives --config php
    ```

    ![](images/img_39.png)

<br>

4. 特別注意：不要使用 `8.3`，因為當前版本不適配，在後面步驟會出錯。

    ![](images/img_41.png)

<br>

5. 除了在這個步驟進行切換，也可以透過以下指令指定，這個指令是指定為 `8.1`。

    ```bash
    sudo update-alternatives --set php /usr/bin/php8.1
    ```

<br>

6. 透過指令查看當前鏈接的版本：這是指 `php` 指令所鏈接的版本號。

    ```bash
    sudo update-alternatives --display php
    ```

    ![](images/img_40.png)

<br>

7. 確認當前啟用的版本：這是服務器目前正在使用的 PHP 模組版本，可用於確保 Apache 使用的是與 `update-alternatives` 設置相符合的 PHP 版本。

    ```bash
    sudo apache2ctl -M | grep php
    ```

    ![](images/img_32.png)

<br>

8. 關於 `AH00558`：表示 Apache 伺服器在啟動時，無法確定完全合格域名（FQDN），這是因為配置文件中並未明確指定 `ServerName`，當發生這種情況，Apache 會嘗試自動檢測域名，如未能確定則使用本地回路地址 `127.0.1.1`。

    ![](images/img_31.png)

<br>

9. 編輯個別網站配置文件：解決 `AH00558` 警告。

    ```bash
    sudo nano /etc/apache2/sites-available/000-default.conf
    ```

<br>

10. 在網站文件 `000-default.conf` 中添加 `ServerName` 設置。 

    ```ini
    <VirtualHost *:8080>

        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html/nextcloud

        # 加入 ServerName 指令
        ServerName 192.168.1.134

        <Directory /var/www/html/nextcloud>
            AllowOverride All
            Require all granted
        </Directory>

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

    </VirtualHost>

    ```

<br>

11. 安裝 PHP 8.1。

    ```bash
    sudo apt install libapache2-mod-php8.1
    ```

<br>

12. 假如要安裝 8.3 可執行以下指令，不過這裡不適配，指令僅供參考。

    ```bash
    sudo apt install libapache2-mod-php8.3
    ```

<br>

13. 切換版本：停用舊版 7.4、啟用新版 8.1，並且重啟服務。

    ```bash
    sudo a2dismod php7.4 && sudo a2enmod php8.1 && sudo systemctl restart apache2
    ```

<br>

14. 未來依版本適配狀況調整：若要停用 8.1 改為 8.3 可使用以下指令，其他版本的切換亦同。

    ```bash
    sudo a2dismod php8.1 && sudo a2enmod php8.3 && sudo systemctl restart apache2
    ```

<br>

15. 再查看一次啟用的版本：確任已經完成切換。

    ```bash
    sudo apache2ctl -M | grep php
    ```

    ![](images/img_33.png)

<br>

16. 重新啟動。

    ```bash
    sudo reboot
    ```

<br>

---

_END_