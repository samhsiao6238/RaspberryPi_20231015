_提供參考_
# virtualenv 介紹

_一個在 venv 尚未出現之前常用的虛擬環境建立工具_

<br>

## 與 `venv` 的差異

_`venv` 和 `virtualenv` 都是 Python 的虛擬環境管理工具，讓開發者可以為不同的專案建立獨立的 Python 環境。_

<br>

1. 沿革：

    - `virtualenv` 是一個早於 `venv` 出現的第三方套件，需要使用 `pip` 進行安裝。

    - 從 Python 3.3 開始內建 `venv` 模組。

<br>

1. 功能和特性：

    - `venv` 已提供了虛擬環境的基本需求。

    - `virtualenv` 具有更多高階功能，例如跨平台支持、支持 Python 2 以及更多的自訂選項。

<br>

3. 依賴：

    - `venv` 使用系統的 Python 來建立虛擬環境，並且需要系統的 `pip` 。

    - `virtualenv` 因為有一個參數 `--download`，可所以以在系統沒有安裝 Python 或 `pip` 的情況下建立虛擬環境。

<br>

4. 安全性：

    - `venv` 不提供 `--no-site-packages` 選項，這個參數是用來可確保虛擬環境將 `不使用系統的任何包` 。

    - `virtualenv` 預設是有這個選項。

<br>

## 基本指令

1. 安裝 `virtualenv`。

    ```bash
    pip install virtualenv
    ```

<br>

2. 建立虛擬環境。

    ```bash
    virtualenv [環境名稱]
    ```

    _如想建立一個名為 `myenv` 的環境_

    ```bash
    virtualenv myenv
    ```

<br>

## 啟動虛擬環境

_根據不同操作系統，啟動虛擬環境的方法有所不同_

<br>

1. Linux/macOS。

    ```bash
    source [環境名稱]/bin/activate
    ```

<br>

2. Windows。

    ```bash
    .\[環境名稱]\Scripts\activate
    ```

    _如啟動名為 `myenv` 的環境_

    _Linux/macOS_

    ```bash
    source myenv/bin/activate
    ```

    _Windows_

    ```bash
    .\myenv\Scripts\activate
    ```

<br>

## 其他指令

1. 退出當前的虛擬環境。

    ```bash
    deactivate
    ```

<br>

2. 刪除虛擬環境。

    _刪除目錄即可_

    ```bash
    rm -r [環境名稱]
    ```

    _如刪除名為 `myenv` 的環境_

    ```bash
    rm -r myenv
    ```

<br>

3. 使用特定版本的 Python。

    _如使用 Python3.8_

    ```bash
    virtualenv -p <實際路徑>/python3.8 [環境名稱]
    ```

<br>

___

_END：`virtualenv` 的基本使用方法_