# MJPG-Streamer

<br>

## 介紹

1. MJPG-Streamer 的主要設計目的是為了捕獲和串流視訊。
2. 它可以從各種來源如UVC攝像頭、文件或其他網絡資源捕獲視訊，然後將其轉換成 MJPEG 格式並透過 HTTP 輸出到網頁上。
3. 使用戶可在任何支援 MJPEG 和 HTTP 的設備上觀看視訊串流，如網頁瀏覽器、移動裝置或其他媒體播放器。

<br>

## 安裝與安裝依賴

1. 更新系統

   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

2. 安裝依賴

- CMake：用來控制軟體編譯過程的工具。

  ```bash
  sudo apt install cmake
  ```

- JPEG開發庫：讓 MJPG-Streamer 支持 JPEG 格式。

  ```bash
  sudo apt install libjpeg-dev
  ```

- FFmpeg：多媒體處理工具。

  ```bash
  sudo apt install ffmpeg
  ```

<br>

## 下載與編譯 MJPG-Streamer

1. 切換到 Downloads 目錄。

   ```bash
   cd ~/Downloads
   ```

2. 克隆 MJPG-Streamer 的 Git 倉庫。

   ```bash
   git clone https://github.com/jacksonliam/mjpg-streamer.git
   ```

3. 進入下載的目錄。

   ```bash
   cd mjpg-streamer/mjpg-streamer-experimental
   ```

4. 編譯與安裝：使用 make 指令編譯 MJPG-Streamer。

   ```bash
   make
   ```

5. 將 MJPG-Streamer 安裝到系統。

   ```bash
   sudo make install
   ```

<br>

## 完成安裝

1. 啟動串流：使用 MJPG-Streamer 進行串流，這裡使用 UVC 視訊來源 (例如：webcam) 與 HTTP 輸出。

   ```bash
   mjpg_streamer -i "input_uvc.so -r 640x480 -d /dev/video0" -o "output_http.so -w /usr/local/share/mjpg-streamer/www"
   ```

<br>

### 設定開機啟動

_如果要在系統開機時自動啟動串流，可透過編輯 `/etc/rc.local` 文件達成_

1. 使用 nano 編輯器打開文件。

    ```bash
    sudo nano /etc/rc.local
    ```

2. 將前面啟動串流的指令添加到 `exit 0` 之前，這將在每次系統開機時都會自動執行該指令。

<br>

---

_END_
