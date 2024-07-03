# conda

<br>

## 安裝 Conda

1. 使用 Anaconda 安裝。下載並執行 Anaconda 安裝程式，可從 [Anaconda 官方網站](https://www.anaconda.com/products/distribution) 取得最新版本。

2. 使用 Miniconda 安裝。下載並執行 Miniconda 安裝程式，可從 [Miniconda 官方網站](https://docs.conda.io/en/latest/miniconda.html) 取得最新版本。

<br>

## 相關操作

1. 使用 Conda 創建新環境。

    ```bash
    conda create --name <環境名稱> python=<版本>
    ```

<br>

2. 啟用 Conda 環境。

    ```bash
    conda activate <環境名稱>
    ```

<br>

3. 安裝套件。

    ```bash
    conda install <套件名稱>
    ```

<br>

4. 顯示已安裝套件。

    _簡單顯示_

    ```bash
    conda list
    ```

    _詳細顯示_

    ```bash
    conda list | grep <套件名稱>
    ```

<br>

6. 查詢過時套件。

    ```bash
    conda search --outdated
    ```

<br>

7. 更新套件。

    ```bash
    conda update <套件名稱>
    ```

<br>

8. 依據套件管理文件安裝套件。

    ```bash
    conda install --file requirements.txt
    ```

<br>

9. 依據當前開發環境的套件生成套件管理文件。

    ```bash
    conda list --export > requirements.txt
    ```

<br>

10. 刪除 Conda 環境。

    ```bash
    conda remove --name <環境名稱> --all
    ```

<br>

___

_END_
