#  安裝 kubectl

_必須在要部署的設備上安裝 [kubctl on MacOS](https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/)，而樹莓派也可以安裝指定版本 [kubctl on Linux](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)_

<br>

## MacOS 安裝 kubectl

_兩種安裝方式，這是第一種，簡單一點可以使用 Homebrew_

<br>

1. 下載最新版本。

    ```bash
    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/arm64/kubectl"
    ```

<br>

2. 下載 kubectl 校驗和檔案。

    ```bash
    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/arm64/kubectl.sha256"
    ```

<br>

3. 根據校驗和檔案驗證 kubectl 二進位檔案。

    ```bash
    echo "$(cat kubectl.sha256)  kubectl" | shasum -a 256 --check
    ```

    _輸出 OK 代表正確_

    ```bash
    kubectl: OK
    ```

<br>

4. 使 kubectl 二進位檔案可執行。

    ```bash
    chmod +x ./kubectl
    ```

<br>

5. 將 kubectl 二進位檔案移到系統上的檔案位置PATH。

    ```bash
    sudo mv ./kubectl /usr/local/bin/kubectl && sudo chown root: /usr/local/bin/kubectl
    ```

<br>

6. 測試以確保安裝的版本是最新的。

    ```bash
    kubectl version --client
    ```

    _輸出_

    ```bash
    Client Version: v1.30.3
    Kustomize Version: v5.0.4-0.20230601165947-6ce0bf390ce3
    ```

<br>

7. 安裝並驗證 kubectl 後，刪除校驗和檔案。

    ```bash
    rm kubectl.sha256
    ```

<br>

## 樹莓派使用 Homebrew 安裝 kubectl

1. 運行安裝命令。

    ```bash
    brew install kubectl
    ```

<br>

2. 測試以確保您安裝的版本是最新的。

    ```bash
    kubectl version --client
    ```

<br>

## 樹莓派安裝 kubectl

1. 下載最新版本。

    ```bash
    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/arm64/kubectl"
    ```

<br>

2. 驗證二進位

    ```bash
    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/arm64/kubectl.sha256"
    ```

<br>

3. 根據校驗和檔案驗證 kubectl 二進位檔案。

    ```bash
    echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check
    ```

<br>

4. 安裝 kubectl。

    ```bash
    sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
    ```

<br>

5. 測試。

    ```bash
    kubectl version --client
    ```

    _輸出_

    ```bash
    Client Version: v1.30.3
    Kustomize Version: v5.0.4-0.20230601165947-6ce0bf390ce3
    ```

<br>

___

_END_