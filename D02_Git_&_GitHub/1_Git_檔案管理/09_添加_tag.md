_參考即可_

# 添加 Tag

_通常用於標記特定項目的版本，更容易地管理和識別不同版本的代碼_

</br>

## 使用 Tag 的步驟

1. 建立一個新的 tag

    ```bash
    git tag <tag_name>
    ```
    如
    ```bash
    git tag v1.0
    ```    

<br>

2. 為 tag 添加註解

   - 透過參數 `-a` 可以給 tag 添加註解。

    ```bash
    git tag -a <tag_name> -m "<annotation>"
    ```
    如
    ```bash
    git tag -a v1.0 -m "My version 1.0"
    ```
<br>

3. 查看倉庫中的全部 tag

    ```bash
    git tag
    ```
<br>

4. 推送 tag

     - 預設情況下，`git push` 不會將 tags 推送到遠端倉庫。
     - 使用以下指令可以推送所有 tags 或指定的 tag。

    ```bash
    git push --tags
    ```
    或
    ```bash
    git push origin <tag_name>
    ```
    如
    ```bash
    git push origin v1.0
    ```
<br>

5. 刪除 tag

    ```bash
    git tag -d <tag_name>
    ```
    如
    ```bash
    git tag -d v1.0
    ```

<br>

6. 查看 tag

    從界面點擊進入查看。

<br>

7. 使用 tag

    - 回到特定版本

        ```bash
        git checkout v1.0
        ```

    - 使用 `git diff` 比較兩個版本

        ```bash
        git diff v1.0..v2.0
        ```

    - 追蹤修改歷史

        ```bash
        git log
        ```

</br>

---

_END_