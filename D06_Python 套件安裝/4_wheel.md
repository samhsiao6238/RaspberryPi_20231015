# 使用 wheel 安裝套件

<br>

## 步驟說明

1. 安裝 `wheel` 模組：首先需要安裝 `wheel` 模組，以便將套件打包成 wheel 格式。

    ```bash
    pip install wheel
    ```

<br>

2. 創建一個 `setup.py` 文件，並包含基本的打包資訊。

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

3. 打包成 wheel 檔案：在包含 `setup.py` 文件的目錄中運行以下命令來生成 wheel 檔案；以下命令將在 `dist` 目錄中生成一個 `.whl` 文件。

    ```bash
    python setup.py bdist_wheel
    ```

<br>

4. 安裝 wheel 檔案：使用 pip 安裝生成的 wheel 檔案。

    ```bash
    pip install dist/<套件名稱>-0.1-py3-none-any.whl
    ```

<br>

5. 列出已安裝套件，確認已安裝的套件是否在列表中。

    ```bash
    pip list
    ```

<br>

6. 更新 wheel 檔案：如果需要更新 wheel 檔案，可以重新運行打包命令。。

    ```bash
    python setup.py bdist_wheel
    ```

<br>

7. 卸載套件：使用 pip 卸載已安裝的 wheel 套件。

    ```bash
    pip uninstall <套件名稱>
    ```

<br>

___

_END_
