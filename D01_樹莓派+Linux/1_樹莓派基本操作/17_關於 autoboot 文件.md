# 安裝在隨身碟

_進一步編輯 autoboot.txt，為下一步實作 AB 啟動做準備_

<br>

## 繼續設定

1. 在更新 `EEPROM` 之前，先進行設定，使用以下指令編輯 `EEPROM` 配置文件。

    ```bash
    sudo nano /etc/default/rpi-eeprom-update
    ```

<br>

2. 可看到設定值預設為 `default`，這表示樹莓派會接收所有類型的固件更新，包括測試版、穩定版和關鍵更新。為確保固件版本穩定且經過充分測試，可以將設定值改為 `critical`，這樣樹莓派只會接收經過充分測試的關鍵更新，從而避免固件的不穩定性問題。

    ```bash
    FIRMWARE_RELEASE_STATUS="critical"
    ```

<br>

3. 完成設定後進行更新韌體，目的是更新 `啟動加載程序（bootloader）` 和相關的配置，特別注意這僅適用於 `樹莓派 4` 以上的型號。

    ```bash
    sudo rpi-eeprom-update -a
    ```

    ![](images/img_56.png)

<br>

4. 完成後將樹莓派關機，關機後取出 SD 卡片，然後重新啟動並以外接裝置作為啟動碟。

    ```bash
    sudo shutdown now
    ``` 

<br>

## 重啟之後

1. 先觀察一下系統現況，透過以下指令查詢樹莓派上的儲存設備。

    ```bash
    lsblk
    ```

    _輸出_

    ```bash
    （後補）
    ```

<br>

2. 接著查詢這些 `儲存設備` 的 `文件系統類型` 及 `掛載資訊 MOUNTPOINTS`。

    ```bash
    sudo blkid
    ```

    _輸出_

    ```bash
    （後補）
    ```

<br>

3. 依據前一個步驟顯示的掛載路徑，執行指令以編輯 `SSD` 上的分區設定文件 `cmdline.txt`，這個文件就在根目錄上，所以直接套用掛載路徑即可取得。

    ```bash
    sudo nano <查詢的 boot 掛載點>/cmdline.txt
    ```

<br>

4. 這個文件用於設置樹莓派的 `引導設定值`，其中 `root=PARTUUID=617a2abd-02` 指定根文件系統的分區 `PARTUUID` 指向分區 `617a2abd-02`，且系統類型為 `ext4`。

    ```bash
    console=serial0,115200 console=tty1 root=PARTUUID=617a2abd-02 rootfstype=ext4 fsck.repair=yes rootwait quiet init=/usr/lib/raspberrypi-sys-mods/firstboot splash plymouth.ignore-serial-consoles cfg80211.ieee80211_regdom=TW systemd.run=/boot/firstrun.sh systemd.run_success_action=reboot systemd.unit=kernel-command-line.target
    ```

<br>

5. 從查詢結果可知，root 參數已經指向 SSD 上的 `/dev/sda2` 分區，且文件系統類型 `ext4`，若要重置 `引導碟`，則需對此文件進行修改。

<br>

## 設置 fstab 與 autoboot.txt 文件

_依據樹莓派官網說明，系統的啟動機制將紀錄在這兩個文件，且文件需要放在各自合適的位置_

<br>

1. `autoboot.txt` 要放在 `啟動分區`，通常是 `/boot` 或 `/boot/firmware` 的根目錄。

<br>

2. `fstab` 要放在根文件系統 `/` 的 `etc` 目錄下，用於定義系統啟動時自動掛載的文件系統。

<br>

## 設置 fstab 文件

_掛載配置文件_

<br>

1. 先修改 `/etc/fstab` 文件，這 `Linux 文件系統掛載配置文件`，用於設置文件系統在啟動時應該如何掛載。

    ```bash
    sudo nano /media/sam6238/rootfs/etc/fstab
    ```

<br>

2. 將 `/boot` 和 `根分區` 指向 `SSD`，確認 `PARTUUID` 是否與前一個步驟查詢結果一致；至於 `proc` 則是 `虛擬文件系統`，用於表示內核和進程的相關信息。

    ```bash
    proc            /proc           proc    defaults          0       0
    PARTUUID=617a2abd-01  /boot/firmware  vfat    defaults          0       2
    PARTUUID=617a2abd-02  /               ext4    defaults,noatime  0       1
    ```

<br>

## 設置 autoboot.txt 文件

_設置啟動時使用的 `分區號 boot_partition`，這個文件預設並未建立_

<br>

1. 在之前步驟中有說明過，可透過 `lsblk -f` 或 `sudo blkid` 取得分區資訊，其中 `引導分區` 通常是 `vfat (FAT32)` 格式，而 `根文件系統分區` 通常是 `ext4` 格式；其中引導文件資料夾還包含的引導文件有 `boot`、`cmdline.txt`、`config.txt` 等。

    ```bash
    lsblk -f
    ```

    _輸出_

    ```bash
    NAME FSTYPE FSVER LABEL UUID                                 FSAVAIL FSUSE% MOUNTPOINTS
    sda                                                                         
    ├─sda1
    │    vfat   FAT32 bootfs
    │                       50C8-AEAE                             435.5M    15% /media/sam6238/bootfs
    └─sda2
        ext4   1.0   rootfs
                            fc7a1f9e-4967-4f41-a1f5-1b5927e6c5f9  180.2G     2% /media/sam6238/rootfs
    # ... 以下省略
    ```

<br>

2. 建立並編輯 `autoboot.txt` 文件，特別注意這個文件預設是不存在的，路徑也與前一步驟不同，這文件要放在 `boot` 目錄。

    ```bash
    sudo nano /media/sam6238/bootfs/autoboot.txt
    ```

<br>

3. 添加以下內容，表示指定從 `SSD` 的第一分區引導。

    ```bash
    [all]
    boot_partition=1
    ```

<br>

## 設置引導標誌

1. 啟動 `fdisk`。

    ```bash
    sudo fdisk /dev/sda
    ```

<br>

2. 在 `fdisk` 內輸入指令 `a` 以進行 `設置或取消分區` 的 `啟動標誌（bootable flag）`，然後選擇分區 `1` 來設置 `引導標誌`，最後輸入 `w` 保存並退出。

    ![](images/img_57.png)

<br>

## 其他指令

1. 卸載分區指令，可串接。

    ```bash
    sudo umount <掛載點 1> <掛載點 2>
    ```

<br>

2. 查詢當前磁區分配，會顯示當前文件系統的磁區使用情況，包括每個掛載點的容量、已用空間和可用空間。

    ```bash
    df -h
    ```

<br>

3. 只要查詢根分區。

    ```bash
    df -h /
    ```
<br>

4. 顯示所有的塊設備及其分區，包括它們的掛載點。

    ```bash
    lsblk
    ```

<br>

5. 列出所有磁盤及其分區詳細信息。

    ```bash
    sudo fdisk -l
    ```

<br>

___

_END_