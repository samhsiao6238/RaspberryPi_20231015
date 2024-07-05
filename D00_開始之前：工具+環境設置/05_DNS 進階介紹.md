# DNS

_樹莓派使用 avahi-daemon 的 mDNS 解析主機名稱_

<br>

# 說明

1. `avahi` 是一個實現 `mDNS` 和 `DNS-SD`（Multicast DNS 和 DNS Service Discovery）` 的服務，在許多 Linux 系統上已預設安裝，包含了樹莓派系統。

<br>

2. `mDNS` 就是 `多播 DNS`，用於在沒有傳統 DNS 服務器的本地網路中進行主機名解析；`DNS-SD` 就是 DNS Service Discovery，顧名思義就是在本地網路中 `發現服務`，如印表機、文件共享服務等。

<br>

3. 樹莓派預設安裝了 `avahi-daemon` 服務，可透過指令查看。

   ```bash
   systemctl status avahi-daemon
   ```

   ![](images/img_21.png)

<br>

4. 樹莓派支援 mDNS 解析，可以在主機名稱後面加上 `.local`，這樣在本地網路中訪問樹莓派時可自動解析並連接。

<br>

## 主要功能

1. 本地網路名稱解析：`avahi` 允許在本地網路中使用主機名稱如 `raspberrypi.local` 來訪問設備，而不需要手動配置 DNS 伺服器。

<br>

2. 服務發現：`avahi` 支持 DNS-SD，可自動發現本地網路中的服務如印表機，客戶端設備可自動找到並連接到這些服務而無需手動配置。

<br>

## 主要命令

1. 啟動。

   ```bash
   sudo systemctl start avahi-daemon
   ```

<br>

2. 檢查狀態。

   ```bash
   sudo systemctl status avahi-daemon
   ```

<br>

3. 停止。

   ```bash
   sudo systemctl stop avahi-daemon
   ```

<br>

4. 開機自動啟動。

   ```bash
   sudo systemctl enable avahi-daemon
   ```

<br>

5. 查看日誌。

   ```bash
   journalctl -u avahi-daemon
   ```

<br>

___

_END_
