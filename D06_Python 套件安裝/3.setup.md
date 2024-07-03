# 使用 setup.py 安裝套件

<br>

## 步驟說明

1. 準備 `setup.py` 文件，並包含以下基本內容。

    ```python
    from setuptools import setup, find_packages

    setup(
        name='套件名稱',
        version='0.1',
        packages=find_packages(),
        install_requires=[
            '依賴套件1',
            '依賴套件2',
            # 更多依賴套件...
        ],
    )
    ```

<br>

2. 在終端機中導航到 `setup.py` 文件所在的目錄，並執行以下命令。

    ```bash
    python setup.py install
    ```

<br>

3. 使用開發模式允許在修改代碼後無需重新安裝即可使用新代碼。

    ```bash
    python setup.py develop
    ```

<br>

4. 檢查套件是否正確安裝：使用 pip 列出已安裝的套件來檢查新安裝的套件。

    ```bash
    pip list
    ```

<br>

5. 卸載套件：如果需要卸載通過 `setup.py` 安裝的套件，可以使用 pip 進行卸載。

    ```bash
    pip uninstall <套件名稱>
    ```

<br>

6. 指定安裝路徑：如果需要將套件安裝到特定路徑，可以使用 `--prefix` 參數。

    ```bash
    python setup.py install --prefix=/path/to/installation
    ```

<br>

___

_END_