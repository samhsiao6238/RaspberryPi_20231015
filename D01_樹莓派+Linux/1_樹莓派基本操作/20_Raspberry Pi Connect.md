# Raspberry Pi Connect 

## 準備條件

# 硬體需求

1. Raspberry Pi 5
2. Raspberry Pi 4
3. Raspberry Pi 400

## 軟體需求

1. 64位元版本的 Raspberry Pi OS Bookworm

2. 使用 Wayland 窗口服務器

## 安裝步驟

1. 更新系統

    ```bash
    sudo apt update -y && sudo apt upgrade -y
    ```

2. 安裝 Raspberry Pi Connect

    ```bash
    sudo apt install rpi-connect
    ```

3. 重啟 Raspberry Pi

    ```bash
    sudo reboot
    ```

4. 登錄 Raspberry Pi Connect：重啟後，你會在屏幕右上角的系統托盤中看到一個新的圖標。點擊此圖標並選擇“Sign in”開始使用。

## 設置完成後的操作

1. 查看連接狀態：
   當你使用網頁瀏覽器連接到 Raspberry Pi 時，系統會使用 WebRTC 技術來建立安全的點對點連接。你可以懸停在瀏覽器中的鎖定圖標上，以查看連接是否被中繼。

2. 網絡連接的處理：
   - 點對點連接：一般情況下，建立連接後，無需通過伺服器進行流量傳輸。
   - 中繼連接：如果無法建立直接連接，流量會通過位於英國的 TURN 伺服器進行中繼。

## 注意事項

- Beta 限制：目前，Raspberry Pi Connect 處於 Beta 階段，可能會遇到一些限制或不完美的地方。
- 反饋：你可以在 Raspberry Pi Connect 部分的論壇中提供反饋和意見。

通過以上步驟，你可以輕鬆設置並使用 Raspberry Pi Connect，實現遠程桌面訪問你的 Raspberry Pi。