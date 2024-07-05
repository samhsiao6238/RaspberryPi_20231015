# Magic Commands

<br>

## 說明

1. 在 Python 開發環境中，所謂的 `Magic Commands` _通常是指_ `Jupyter Notebook` 中的一種特殊命令；除此，在其他環境中有類似的用法，只是並不稱為 `Magic Commands`，例如在 `Bash Shell`、`SQL Databases`、`REPL（Read-Eval-Print Loop）` 也都有類似的做法。

<br>

2. 在 `Jupyter Notebook` 中 的 `Magic Commands` 是一些特定的命令，能夠簡化各種常見的任務，例如文件操作、計時、執行系統命令等；這些命令分為兩種，分別是 `行魔術命令（Line magics）` 和 `單元魔術命令（Cell magics）`。

<br>

## 行魔術命令（Line magics）

1. 行魔術命令以百分號（%）開頭，只作用於一行代碼。

<br>

2. 以下命令會計時 `sum(range(1000))` 的執行時間。

    ```python
    %timeit x = sum(range(1000))
    ```

<br>

## 單元魔術命令（Cell magics）

1. 單元魔術命令以兩個百分號（%%）開頭，作用於整個代碼單元。

<br>

2. 以下命令會計時整個代碼單元的執行時間。
    ```python
    %%timeit
    x = sum(range(1000))
    y = sum(range(1000))
    ```

<br>

## 其他常用魔法命令

1. %lsmagic：列出所有可用的魔術命令。

    ```python
    %lsmagic
    ```

<br>

2. %pwd：顯示當前工作目錄。

    ```python
    %pwd
    ```

<br>

3. %matplotlib inline：使得 matplotlib 的圖形嵌入在 Jupyter Notebook 中顯示。

    ```python
    %matplotlib inline
    import matplotlib.pyplot as plt
    plt.plot([1, 2, 3], [4, 5, 6])
    plt.show()
    ```

<br>

4. %%writefile：將整個代碼單元的內容寫入一個文件。

    ```python
    %%writefile hello.py
    print("Hello, World!")
    ```

<br>

## 其他情境下的 Magic Commands

_特殊命令或功能在不同的工具和框架中可能有不同的名稱和用法，但它們的共同點是提供便捷和快速的操作方式，讓開發者能更高效地完成任務。_

<br>

1. IPython 是一個強大的交互式 Python Shell，也是 Jupyter Notebook 的核心，在 IPython 中也有 Magic Commands 的概念，它們的用法與 Jupyter Notebook 中一致。

    ```python
    %run script.py
    %load file.py
    ```

<br>

2. Bash Shell 中有很多內建命令和快捷鍵可以加速操作，例如 `alias` 可以用來建立命令的簡寫。

    ```bash
    alias ll='ls -la'
    ```

<br>

3. 在一些 SQL Databases 管理系統中，也有類似於 Magic Commands 的功能，例如 MySQL 中的 `SHOW` 命令。

    ```sql
    SHOW DATABASES;
    ```

<br>

4. 許多編程語言的 `REPL（Read-Eval-Print Loop）` 環境中也有特殊命令，這些命令可以快速執行一些常見的操作，例如在 Node.js 的 REPL 中，可以使用 `.help` 查看幫助信息。

    ```node
    .help
    ```

<br>

___

_END_