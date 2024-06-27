# 分區工具 GParted

_安裝分配分區圖形化界面工具 GParted_

<br>

1. 按標準程序，在安裝工具之前先更新運作中的樹莓派系統。

    ```bash
    sudo apt update && sudo apt full-upgrade -y
    ```

<br>

2. 在樹莓派中安裝工具 `GParted` 來管理分區。

    ```bash
    sudo apt install gparted -y
    ```

<br>

3. 同時安裝分處理區格式等附屬工具。

    ```bash
    sudo apt install dosfstools mtools -y
    ```

<br>

## 啟動工具

<br>

1. 這是一個圖形化界面工具，所以要進入樹莓派並從終端啟動 `GParted`。

    ```bash
    sudo gparted
    ```

<br>

## 使用

_後補_

<br>

___

_END_