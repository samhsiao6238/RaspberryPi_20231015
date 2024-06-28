# VNC 連線時可能發生的錯誤

<br>

## Cannot currently show the desktop

_[參考](https://blog.csdn.net/Dorian15/article/details/128321804)_

<br>

1. 出現如下的畫面，無法進入桌面。

   ![](images/img_02.png)

<br>

## 排除步驟

_特別說明，新版作業系統的設定文件已經變更，這適用於 `Bullseye` 之前的版本。_

<br>

1. 編輯設定檔案。

   ```bash
   sudo nano /boot/config.txt
   ```

<br>

2. 取消註解：強制開啟 HDMI。

   ```bash
   hdmi_force_hotplug=1
   ```

<br>

3. 使用 nano 編輯時，需使用鍵盤組合鍵進行儲存 `CTRL + O` 與 `退出 CTRL + X`。

<br>

4. 如下內容設定。

   ![](images/img_03.png)

<br>

5. 編輯設定文件之後需重新啟動樹莓派。

   ```bash
   sudo reboot now
   ```

<br>

___

_END_