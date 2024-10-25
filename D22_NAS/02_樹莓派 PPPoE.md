# PPPoE

_以下以中華電信為例_

<br>

## 說明

1. 如果樹莓派沒有透過路由器，而是直接連接中華電信的數據機，需要在樹莓派上設定 `PPPoE` 來使用固定 IP，樹莓派在這樣的設置下會直接通過數據機進行撥接上網。

<br>

## 步驟

1. 在樹莓派安裝 PPPoE 客戶端工具 `pppoeconf`。

    ```bash
    sudo apt update
    sudo apt install pppoeconf
    ```

<br>

2. 啟動並配置 PPPoE；這個工具會自動掃描網路介面，並嘗試檢測是否有 PPPoE 伺服器可用。

    ```bash
    sudo pppoeconf
    ```

<br>

3. 在設定過程中，當 `pppoeconf` 檢測到 PPPoE 伺服器後，會要求輸入 PPPoE 帳號和密碼。

    ```bash
    帳號：xxxxxxxx@ip.hinet.net
    密碼：
    ```

<br>

4. 設定過程都接受 `pppoeconf` 工具的預設值。

<br>

## 啟動 PPPoE 連線

1. 配置完成後，`pppoeconf` 會自動啟動 PPPoE 連線；如果它沒有自動啟動，可手動啟動 PPPoE。

    ```bash
    sudo pon dsl-provider
    ```

<br>

2. 檢查 PPPoE 連線狀態；這會顯示 `ppp0` 接口，並且顯示公共 IP 地址，這就是固定 IP 地址。

    ```bash
    ifconfig ppp0
    ```

<br>

## 設置開機自動連線

1. 為了確保樹莓派在每次開機時自動連線到網際網路，可將 PPPoE 設定添加到啟動腳本中，當樹莓派啟動時，會自動撥號連線；編輯 `/etc/rc.local` 文件。


    ```bash
    sudo nano /etc/rc.local
    ```

<br>

2. 在 `exit 0` 之前添加以下代碼，保存並退出。

    ```bash
    sudo pon dsl-provider
    ```

<br>

##  測試外網連接

1. 配置完成後，可嘗試從外網使用固定 IP 連接樹莓派，如果有開啟設置 SSH 服務，可使用以下指令連接。

    ```bash
    ssh <樹莓派使用者帳號>@<固定 IP>
    ```

<br>

## 安全配置

_由於將 SSH 暴露在外網上_

<br>

1. 使用 SSH 公鑰驗證 來替代密碼。

<br>

2. 可修改 SSH 默認端口 避免常見的暴力攻擊。

<br>

3. 設定防火牆 來限制只有特定 IP 能訪問樹莓派。

<br>

___

_END_