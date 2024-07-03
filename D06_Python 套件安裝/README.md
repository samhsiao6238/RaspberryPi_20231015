# Python 的套件安裝

_有多種方式，不同方式適用於不同的情境，具體選擇取決於項目的需求和開發者的習慣。以下是常見的幾種_

1. 使用 `pip`

    - 最常見和推薦的方式。
    - 安裝：`pip install package_name`
    - 升級：`pip install --upgrade package_name`
    - 卸載：`pip uninstall package_name`

<br>

2. 使用 `conda`：

    - 適用於 Anaconda 或 Miniconda 環境。
    - 安裝：`conda install package_name`
    - 升級：`conda update package_name`
    - 卸載：`conda remove package_name`

<br>

3. 使用 `setup.py` 文件：

    - 適用於從源代碼安裝。
    - 下載並解壓源代碼後，在源代碼目錄下執行：`python setup.py install`

<br>

4. 使用 `wheel` 文件：

    - `.whl` 文件是一種二進制包格式。
    - 安裝：`pip install package_name.whl`

<br>

5. 使用 `easy_install`：

    - 比較舊的方法，不推薦使用。
    - 安裝：`easy_install package_name`

<br>

6. 使用 `Poetry`：

    - 管理依賴和包的工具。
    - 安裝：`poetry add package_name`

<br>

7. 使用 `pipenv`：

    - 管理 Python 包和虛擬環境的工具。
    - 安裝：`pipenv install package_name`

<br>

8. 手動下載並安裝：

    - 下載包文件後，解壓並使用 `python setup.py install` 安裝。

<br>

___

_END_
