# 安裝 MiniKube

_MiniKube 是一個用於本地 Kubernetes 集群的工具，它適合在開發環境中使用_

<br>

## 步驟說明

1. 更新樹莓派系統。

    ```bash
    sudo apt update && sudo apt upgrade -y
    ```

<br>

2. 安裝 Docker：MiniKube 依賴於 Docker 作為容器運行，因此需要先安裝 Docker。

    ```bash
    curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh
    ```

<br>

3. 將 `當前用戶` 加入 Group。

    ```bash
    sudo usermod -aG docker $USER
    ```

<br>

4. 安裝 MiniKube：下載並安裝 MiniKube 的二進制文件。

    ```bash
    curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-arm64
    ```

<br>

5. 添加執行權限。

    ```bash
    chmod +x minikube
    ```

<br>

6. 將執行文件搬移到系統路徑中。

    ```bash
    sudo mv minikube /usr/local/bin/
    ```

<br>

7. 啟動 MiniKube：使用 Docker 作為驅動器啟動 MiniKube。

    ```bash
    minikube start --driver=docker
    ```

<br>

8. 檢查 MiniKube 狀態，確認 MiniKube 已經成功啟動並運行。

    ```bash
    minikube status
    ```

    ![](images/img_01.png)

<br>

___

_END_