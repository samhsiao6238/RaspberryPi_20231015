# 安裝新版 Nodejs

<br>

## 新版

_20240624 更新_

<br>

1. 參考 [官網](https://deb.nodesource.com/) 提供的安裝指令。

    ```bash
    # 安裝 nvm（Node Version Manager）
    curl -fsSL https://deb.nodesource.com/setup_20.x | sudo bash -
    # 下載並安裝 Node.js
    sudo apt-get install -y nodejs
    # v20.15.0
    node -v
    # 10.7.0
    npm -v
    ```

<br>

## 舊版

1. 這是 `官網` 之前提供的安裝指令。

    ```bash
    sudo apt-get update && sudo apt-get install -y ca-certificates curl gnupg
    curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg
    NODE_MAJOR=18
    echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | sudo tee /etc/apt/sources.list.d/nodesource.list
    sudo apt-get update && sudo apt-get install nodejs -y
    ```

<br>

___

_END_