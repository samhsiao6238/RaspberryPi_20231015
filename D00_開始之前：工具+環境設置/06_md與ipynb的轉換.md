# Markdown 與 Jupyter 的轉換

<br>

## 1. .ipynb 轉換為 .md

1. 自訂一個腳本 `convert_to_md.sh`

    ```sh
    #!/bin/bash
    jupyter nbconvert --to markdown "$1"
    ```

2. 其餘後補。


<br>

## 2. .md 轉換為 .ipynb

### 在終端機中執行

1. 安裝插件

    ```bash
    pip install jupytext
    ```

<br>

2. 執行指令

    ```bash
    jupytext --to notebook <要轉換的 markdown.md>
    ```

<br>

### 在 VSCode 中建立快速鍵

_在 VSCode 中設定快捷鍵執行特定指令，病使用 `tasks.json` 和 `keybindings.json` 檔案來配置。_

<br>

#### 創建任務

1. 打開命令面板， `Ctrl+Shift+P` 或 `Cmd+Shift+P` 在Mac上。
2. 輸入 `Tasks: Configure Task` 並選擇 `Create tasks.json file from template` 。
   
   ![](images/img_12.png)

3. 假如沒有的話，選擇 `Open User Tasks` ，並任選其中一個就會開啟 `tasks.json` 檔案。

    ![](images/img_13.png)

4. 在 `tasks.json` 檔案中，添加以下任務配置

    ```json
    {
        "version": "2.0.0",
        "tasks": [
            {
                "label": "Convert Markdown to Notebook",
                "type": "shell",
                "command": "jupytext",
                "args": [
                    "--to",
                    "notebook",
                    "${file}"
                ],
                "group": {
                    "kind": "build",
                    "isDefault": true
                }
            }
        ]
    }
    ```

    ![](images/img_14.png)

    - 這將創建一個任務，當運行時會將當前打開的檔案（認為是Markdown檔案）轉換為Jupyter Notebook。

<br>

#### 設定快捷鍵

1. 打開命令面板。
2. 輸入 `Preferences: Open Keyboard Shortcuts (JSON)` 並選擇它。
   
   ![](images/img_15.png)

3. 在 `keybindings.json` 檔案中，添加以下配置。

    ```json
    {
        "key": "ctrl+alt+n", // 或其他任何快捷鍵
        "command": "workbench.action.tasks.runTask",
        "args": "Convert Markdown to Notebook"
    }
    ```

    ![](images/img_16.png)

    - 這將為剛剛創建的任務設定一個快捷鍵。


4. 在 VSCode 中打開一個 Markdown 檔案並使用設定的快捷鍵時，它會自動轉換為 Jupyter Notebook。

<br>

---

_END_
