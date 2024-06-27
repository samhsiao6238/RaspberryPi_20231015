# 更新 EEPROM

_補充說明在隨身碟中製作系統碟的 `刷新韌體` 作業_

<br>

## 說明

1. EEPROM 是 `電可擦寫可編程唯讀記憶體`，這是一種小型儲存芯片，用於儲存引導加載程式和系統設置等重要信息。通過更新 EEPROM，可以修復引導相關的問題，增加新的功能或改善硬體相容性。

<br>

2. `引導程式（bootloader）` 是一段代碼，主要作用是在系統啟動過程中初始化硬體並加載操作系統。

<br>

3. 樹莓派的 `引導程式` 儲存在 `EEPROM` 中，所以更新 `EEPROM` 實際上就是更新這段引導程式碼，等效於修復舊版引導程式問題或添加新的功能。

<br>

## 刷新

_刷新之前，先對當前 EEPROM 設置進行查詢_

<br>

1. 查詢當前樹莓派的引導程式版本。

    ```bash
    vcgencmd bootloader_version
    ```

    _輸出_

    ```bash
    Apr 29 2021 17:11:25
    version c2f8c388c4ee37ad709ace403467d163e8dd91ce (release)
    timestamp 1619712685
    update-time 1619712685
    capabilities 0x0000001f
    ```

<br>

2. 查詢當前樹莓派的引導程式配置設定。

    ```bash
    vcgencmd bootloader_config
    ```
    _輸出_
    ```bash
    [all]
    BOOT_UART=0
    WAKE_ON_GPIO=1
    POWER_OFF_ON_HALT=0
    ```

<br>

3. 更新指令，由輸出可知有一個新的 EEPROM 引導程式更新可用，當前版本是 2021/0429，最新版本是 2024/04/15，VL805 固件已經是是最新的不需要更新，而更新文件 (`pieeprom.upd`) 已經複製到資料夾 `/boot/firmware` 中，並且也做了備份 `recovery.bin`，如果想取消此更新，可以執行 `sudo rpi-eeprom-update -r`。

    ```bash
    sudo rpi-eeprom-update -a
    ```

    _輸出_
    ```bash
    *** PREPARING EEPROM UPDATES ***
    BOOTLOADER: update available
        CURRENT: Thu 29 Apr 16:11:25 UTC 2021 (1619712685)
            LATEST: Mon 15 Apr 13:12:14 UTC 2024 (1713186734)
        RELEASE:
            default (/lib/firmware/raspberrypi/bootloader-2711/default)
            Use raspi-config to change the release.

        VL805_FW: Using bootloader EEPROM
            VL805: up to date
        CURRENT: 000138a1
            LATEST: 000138a1
        CURRENT: Thu 29 Apr 16:11:25 UTC 2021 (1619712685)
            UPDATE: Mon 15 Apr 13:12:14 UTC 2024 (1713186734)
            BOOTFS: /boot/firmware
    '/tmp/tmp.O4oXzboYdz' -> '/boot/firmware/pieeprom.upd'
    Copying recovery.bin to /boot/firmware for EEPROM update

    EEPROM updates pending. Please reboot to apply the update.
    To cancel a pending update run "sudo rpi-eeprom-update -r".
    ```

<br>

4. 完成更新後要重啟系統。

    ```bash
    sudo reboot now
    ```

<br>

__END___