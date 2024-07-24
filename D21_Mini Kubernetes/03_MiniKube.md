# 安裝 MiniKube

_MiniKube 是一個用於本地 Kubernetes 集群的工具，它適合在開發環境中使用，以下在樹莓派 A 進行安裝_

<br>


## 步驟說明

1. 更新樹莓派系統。

    ```bash
    sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y
    ```

<br>

2. 確認是否安裝了 Docker。

    ```bash
    docker -v
    ```

<br>

3. 假如還沒安裝 Docker 則進行安裝；因為 `MiniKube` 依賴於 `Docker` 作為容器運行，所以一定要先安裝 Docker。

    ```bash
    curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh
    ```

<br>

4. 檢查當前用戶群組。

    ```bash
    groups sam6238
    ```

<br>

5. 假如 `當前用戶` 不在群組 Group 內，則將其加入。

    ```bash
    sudo usermod -aG docker $USER
    ```

<br>

6. 安裝 MiniKube：下載並安裝 MiniKube 的二進制文件。

    ```bash
    curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-arm64
    ```

<br>

7. 添加執行權限。

    ```bash
    chmod +x minikube
    ```

<br>

8. 將執行文件搬移到系統路徑 `/usr/local/bin/` 中。

    ```bash
    sudo mv minikube /usr/local/bin/
    ```

<br>

9. 使用 Docker 作為驅動器啟動 MiniKube。

    ```bash
    minikube start --driver=docker
    ```

    ![](images/img_21.png)

<br>

10. 檢查 MiniKube 狀態，確認 MiniKube 已經成功啟動並運行。

    ```bash
    minikube status
    ```

    ![](images/img_01.png)

<br>

11. 檢查容器 IP。

    ```bash
    minikube ip
    ```

    _輸出_

    ```bash
    192.168.49.2
    ```

<br>

___

_END_