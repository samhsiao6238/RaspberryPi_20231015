
# 在樹莓派上安裝 Docker 的步驟

1. **更新系統**:
   ```bash
   sudo apt update
   sudo apt upgrade
    ```

2. **進入目錄**:

   ```bash
   cd Downloads
   ```
3. **下載 Docker 安裝腳本**:

   ```bash
   curl -fsSL https://get.docker.com -o get-docker.sh
   ```
4. **運行安裝腳本**:

   ```bash
   sudo sh get-docker.sh
   ```
5. **添加用戶到 Docker 群組**（可避免每次使用 Docker 都需要使用 sudo）:

   ```bash
   sudo usermod -aG docker $USER
   ```
6. **重新啟動樹莓派**或登出再登入:

   ```bash
   sudo reboot now
   ```

   > 稍等一下重新登入

    <br>

7. **驗證 Docker 安裝**:

   ```bash
   docker run hello-world
   ```
8. **檢查安裝的 Docker 版本**:

   ```bash
   docker --version
   ```

## Docker 基本指令

| 指令              | 功能                   | 說明                                            |
| ----------------- | ---------------------- | ----------------------------------------------- |
| `docker pull`   | 下載 Docker 映像       | 從Docker Hub或其他Docker registry下載指定的映像 |
| `docker run`    | 運行 Docker 容器       | 根據指定的映像啟動一個新的容器實例              |
| `docker ps`     | 列出運行中的容器       | 顯示運行中的所有Docker容器的列表                |
| `docker stop`   | 停止運行的容器         | 使用容器ID或名稱來停止容器                      |
| `docker start`  | 啟動已停止的容器       | 使用容器ID或名稱來啟動停止的容器                |
| `docker rm`     | 刪除一個容器           | 使用容器ID或名稱來刪除一個停止的容器            |
| `docker images` | 列出本地的 Docker 映像 | 顯示在本地機器上儲存的所有Docker映像的列表      |
| `docker rmi`    | 刪除 Docker 映像       | 使用映像ID或名稱來刪除指定的Docker映像          |

## 注意事項

樹莓派使用的是 **ARM 架構** 的處理器，而大部分的 Docker 映像是為 **x86 架構** 的處理器設計的，所以在選擇 Docker 映像時，必須確保它支援 ARM 架構。

---
END
