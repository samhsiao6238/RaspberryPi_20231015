# AnyDesk

_依據 [官方說明](https://support.anydesk.com/zh-tw/knowledge/anydesk-for-linux-raspberry-pi-freebsd)，截至今日（2024/07/10） 可支援版本如下，但這已不在推薦使用的系統清單中，所以不再贅述安裝步驟，僅對於已經安裝卻無法運行的狀況提供移除安裝說明。_

<br>

## 徹底移除 AnyDesk

1. 找到安裝的 AnyDesk 套件。

    ```bash
    dpkg -l | grep anydesk
    ```

<br>

2. 移除 AnyDesk 套件。

    ```bash
    sudo apt remove --purge anydesk -y
    ```

<br>

3. 清除相關依賴套件和配置文件。

    ```bash
    sudo apt autoremove -y && sudo apt clean -y
    ```

<br>

4. 檢查並刪除可能殘留的 AnyDesk 文件。

    ```bash
    sudo rm -rf /etc/anydesk /var/lib/anydesk
    ```

<br>

5. 如果有安裝桌面版，可能會有殘留的桌面啟動文件，可以檢查並刪除。

    ```bash
    sudo rm -rf /usr/share/applications/anydesk.desktop
    ```

<br>
