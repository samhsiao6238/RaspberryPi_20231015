# .gitignore

_當需要排除 Git 追蹤的特定檔案或目錄時，可以使用 `.gitignore` 檔案。_

<br>

## 使用情境

_以下情況可能需要建立 `.gitignore` 排除清單_

<br>

1. 當同步的檔案太大（超過 100 MB）時會報錯。

<br>

2. 某些私密檔案或目錄不應被追蹤。

<br>

3. 某些會持續不斷增加的日誌檔案不宜被追蹤。

<br>

## 步驟

1. 在 repo 的根目錄建立 `.gitignore` 檔案。

    ```bash
    touch .gitignore
    ```

<br>

2. 若要排除特定的檔案類型，例如 `.zip` 和 `.jar`，在 `.gitignore` 內添加以下內容。

    ```bash
    *.zip
    *.jar
    ```

    _若要排除 `指定路徑` 下的 `指定檔案類型`，可加入路徑， `**` 代表所有路徑_

    ```bash
    00_projects/**/*.zip
    00_projects/**/*.jar
    ```

<br>

3. 若已追蹤了這些檔案，需先移除追蹤。

    ```bash
    git rm --cached 00_projects/**/*.zip
    git rm --cached 00_projects/**/*.jar
    ```

<br>

4. 留意套件生成的 log 檔案，例如 `HiveMQ`。這些檔案若不排除，會不斷增加。

<br>

5. 若想排除特定路徑下的所有檔案，使用 `/**` 表示。

    ```bash
    my_projects/hivemq/data/**
    ```

<br>

6. 提交 `.gitignore`。

    ```bash
    git add .gitignore
    git commit -m "GOOD"
    git push origin main
    ```

<br>

7. 若遇到已有 commit 排在前面的情況，可以選擇強制推送。

    ```bash
    git push -f
    ```

    或是撤銷指定的 commit

    ```bash
    git revert <commit_id>
    ```

<br>

8. 查看最後一次的 commit。

    ```bash
    git show HEAD
    ```

<br>

9. 查詢本地未同步到遠端的 commit。

    ```bash
    git log origin/<branch_name>..<branch_name>
    ```

    舉例：

    ```bash
    git log origin/main..main
    ```

<br>

10. 若需要，可以強制添加某個目錄進行追蹤。

    ```bash
    git add -f <specific_directory>
    ```

<br>

___

_END_