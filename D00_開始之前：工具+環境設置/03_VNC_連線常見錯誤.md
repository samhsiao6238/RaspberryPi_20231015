# VNC 連線時可能發生的錯誤

## Cannot currently show the desktop
- 無險顯示遠端桌面
- 出現黑屏＋文字
- [參考](https://blog.csdn.net/Dorian15/article/details/128321804)
- 使用終端機進行編輯，可避免權限問題

![](images/img_02.png)

1. 編輯設定檔案

   ```bash
   sudo nano /boot/config.txt
   ```

2. 取消註解：強制開啟 HDMI

   ```bash
   hdmi_force_hotplug=1
   ```

3. nano 操作
   - 儲存：CTRL + O
   - 退出：CTRL + X

4. 如下設定

   ![](images/img_03.png)

5. 重新啟動
    ```bash
    sudo reboot now
    ```
