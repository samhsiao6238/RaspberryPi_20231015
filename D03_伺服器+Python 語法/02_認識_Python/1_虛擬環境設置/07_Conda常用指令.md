# Conda 語法介紹

<br>


## 安裝

1. 使用 wget 下載 Miniconda 或 Miniforge 的 ARM 版本安裝腳本

    ```bash
    wget [下載鏈接] 
    ```

2. 執行安裝腳本

    ```bash
    bash [安裝腳本名稱]  
    ```


<br>

## 虛擬環境管理

1. 創建虛擬環境

    ```bash
    conda create --name [環境名稱] python=[版本]
    ```

2. 啟動或切換虛擬環境

    ```bash
    conda activate [環境名稱]
    ```

3. 停止或退出當前虛擬環境

    ```bash
    conda deactivate
    ```

4. 列出所有虛擬環境

    ```bash
    conda env list
    ```

5. 刪除虛擬環境

    ```bash
    conda env remove --name [環境名稱]
    ```


<br>

## 套件管理

1. 安裝套件

    ```bash
    conda install [套件名稱]
    ```

2. 列出已安裝的套件

    ```bash
    conda list
    ```

3. 更新套件

    ```bash
    conda update [套件名稱]
    ```

4. 刪除套件

    ```bash
    conda remove [套件名稱]
    ```

<br>

## 其他常見指令

1. 更新 conda 本身

    ```bash
    conda update conda
    ```

2. 查找可用的套件版本

    ```bash
    conda search [套件名稱]
    ```

<br>

---

_END_
