# 與 Minikube 連線

_以下是本機嘗試連線樹莓派 A_

<br>

## 樹莓派 A

_運行 Minikube_

<br>

1. 樹莓派 A 啟動 Minikube；使用參數 `--driver=none` 會直接在本地機器樹莓派 A 上運行，而不使用虛擬機；若要使用虛擬網卡可用參數 `--driver=docker`，預設也會在容器中啟動。

    ```bash
    minikube start
    ```

    ![](images/img_08.png)

<br>

2. 確認 Minikube 狀態。

    ```bash
    minikube status
    ```

    ![](images/img_09.png)

<br>

3. 確認 IP。

    ```bash
    minikube ip
    ```

<br>

## 證書文件

_樹莓派 A 上的證書文件_

<br>

1. 檢查並確認證書文件是否存在於樹莓派 A，以下指令分開兩次執行，用以明確觀察證書所在路徑。

    ```bash
    ls ~/.minikube/profiles/minikube/
    ls ~/.minikube/
    ```

    _要確認這三個文件的位置_

    ![](images/img_15.png)

<br>

2. 確認文件存在後準備進行複製，先在 MacOS 上建立目標目錄；建立之前可先檢查 `~/.minikube/profiles/minikube` 文件是否存在，若有殘餘資料可先將其刪除。

    ```bash
    mkdir -p ~/.minikube/profiles/minikube
    ```

<br>

3. 使用 scp 將三個證書文件從樹莓派 A 複製到 MacOS。

    ```bash
    scp ssd:~/.minikube/profiles/minikube/client.crt ~/.minikube/profiles/minikube/client.crt
    scp ssd:~/.minikube/profiles/minikube/client.key ~/.minikube/profiles/minikube/client.key
    scp ssd:~/.minikube/ca.crt ~/.minikube/ca.crt
    ```

    _務必確保文件正常複製_

    ![](images/img_22.png)

<br>

4. 使用以下指令確定複製完成。

    ```bash
    ls ~/.minikube/profiles/minikube/client.crt
    ls ~/.minikube/profiles/minikube/client.key
    ls ~/.minikube/ca.crt
    ```

<br>

## 查看 Minikube 狀態與 IP

1. 確認在樹莓派 A 上已經啟動並運行了 Minikube。

    ```bash
    minikube status
    ```

    _輸出_

    ```bash
    minikube
    type: Control Plane
    host: Running
    kubelet: Running
    apiserver: Running
    kubeconfig: Configured
    ```

<br>

2. 在樹莓派 A 上確認 Minikube 的 IP 地址。

    ```bash
    minikube ip
    ```

    _輸出_

    ```bash
    192.168.49.2
    ```

<br>

3. 這是 Kubernetes 集群內的 Pod 和服務之間通信的網段，若試圖從 MacOS 連線這個 IP 地址是無法連線的。

    ```bash
    ping 192.168.49.2
    ```

<br>

## 複製 Minikube 配置文件到 MacOS

_從樹莓派將配置文件複製到本機電腦上_

<br>

1. 在樹莓派 A 檢查所需的設定文件已經存在。

    ```bash
    ls ~/.kube/config
    ```

<br>

2. 在本地電腦 MacOS 上建立目標目錄。

    ```bash
    mkdir -p ~/.kube
    ```

3. 在 MacOS 上運行以下指令從樹莓派 A 複製 Minikube 的 kubeconfig 文件到 MacOS。

    ```bash
    scp ssd:~/.kube/config ~/.kube/config
    ```

    ![](images/img_12.png)

<br>

4. 在 MacOS 設置 Minikube 環境變數。

    ```bash
    export KUBECONFIG=~/.kube/config
    ```

<br>

## 編輯設定文件

1. 查看本機使用者的家目錄絕對路徑 `/Users/samhsiao`；可在任何路徑中透過 `pwd` 查看路徑前綴即可。

    ![](images/img_14.png)

<br>

2. 編輯 Kubeconfig 文件 `~/.kube/config` 中的路徑，使其指向 MacOS 上的正確位置；可先確認資料 `~/.kube/config` 存在。

    ```bash
    code ~/.kube/config
    ```

<br>

3. 將其中的使用者家目錄從樹莓派的 `/home/sam6238` 改為本機用戶的家目錄 `/Users/samhsiao`；再次強調，務必詳細檢查。

    ![](images/img_13.png)

<br>

4. 將其中的 `server` 改為 `localhost`，端口 `8443`。

    ```bash
    server: https://localhost:8443
    ```

    ![](images/img_17.png)

<br>

5. 開啟通道，這個通道不可關閉。

    ```bash
    ssh -L 8443:192.168.49.2:8443 ssd
    ```

<br>

6. 在 MacOS 運行指令切換連線。

    ```bash
    kubectl config use-context minikube
    ```

    _輸出_

    ```bash
    Switched to context "minikube".
    ```

<br>

7. 連線測試；確認連接是否成功，以下訊息表示 Minikube 集群已經成功運行，節點 `minikube` 處於 Ready 狀態，並且運行了 3 小時 45 分鐘，Kubernetes 的版本是 `v1.30.0`；確認了 Minikube 安裝和配置是正確的，並且節點已經準備好接收和運行工作負載。

    ```bash
    kubectl get nodes
    ```

    _輸出_

    ```bash
    NAME       STATUS   ROLES           AGE     VERSION
    minikube   Ready    control-plane   3h45m   v1.30.0
    ```

<br>

___

_END_
