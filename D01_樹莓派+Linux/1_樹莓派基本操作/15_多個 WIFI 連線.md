# 多個 WIFI 連線

_適用舊版 Bullseye 以前系統，新版的網絡管理已改用 `NetworkManager`，特別說明，雖然依舊可以在 `wpa_supplicant.conf` 文件中進行設定，但為了避免不必要的衝突，建議不要這樣做。_

<br>

1. 終端機指令。

    ```bash
    sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
    ```

<br>

2. 一開始會看到燒錄記憶卡的時候設定的 WIFI；特別注意，新版依舊會看到前兩行關於 `控制接口目錄和允許訪問的用戶組` 及 `運行時更新配置文件` 的設定，只是連線資訊已不在這顯示。

    <img src="images/img_16.png" width="400px" />

<br>

3. 在舊版系統中，可使用相同比格式加入新的 WIFI 設定即可。

    ```bash
    network={
        ssid="<SSID 名稱>"
        psk=<密碼>
    }
    ```

    <img src="images/img_18.png" width="400px" />

<br>

## 查看並建立連線

1. 查看當前運行中的 `連線種類`，結果顯示包含有線與無線網路。

    ```bash
    nmcli device status
    ```

    ![](images/img_133.png)

<br>

2. 查看樹莓派可連線的 WIFI 及當前連線的 WIFI。

    ```bash
    nmcli device wifi list
    ```

    ![](images/img_128.png)

<br>

2. 添加 Wi-Fi 連接，要使用 `sudo`。

    ```bash
    # 指令說明
    sudo nmcli dev wifi connect <SSID 名稱>  password <連線密碼>
    # 實際指令
    sudo nmcli dev wifi connect SamHome2.4g  password xxxxxx
    ```

    ![](images/img_129.png)

<br>

3. 可添加多個 WIFI 設定，這個指令的顯示的排序不同代表優先級別；特別說明，其中 `preconfigured` 就是燒錄光碟時設定的 WIFI 的別名。

    ```bash
    nmcli connection show
    ```

    ![](images/img_131.png)

<br>

4. 但最後設定的會優先連線。

    ```bash
    nmcli device wifi list
    ```

    ![](images/img_132.png)

<br>

5. 設定優先權，值越大，優先級越高。

    ```bash
    sudo nmcli connection modify <SSID 名稱> connection.autoconnect-priority <優先級別>
    ```

<br>

6. 若要查看優先級別，必須透過 `show` 指令指定 `SSID` 來查看指定參數的設定值。

    ```bash
    nmcli connection show <SSID 名稱>
    ```

    ![](images/img_134.png)

<br>

___

_END_