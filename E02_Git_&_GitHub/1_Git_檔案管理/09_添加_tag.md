# 添加 Tag

Tag 在 Git 中是一種重要的功能，它通常用於標記特定的項目版本。Tag 可以幫助我們更容易地管理和識別不同版本的代碼。

## 使用 Tag 的步驟：

1. **創建一個新的 tag**:

    ```bash
    git tag <tag_name>
    git tag v1.0
    ```

2. **為 tag 添加註解**:

    透過參數 `-a` 可以給 tag 添加註解。

    ```bash
    git tag -a <tag_name> -m "<annotation>"
    git tag -a v1.0 -m "My version 1.0"
    ```

3. **查看倉庫中的全部 tag**:

    ```bash
    git tag
    ```

4. **推送 tag**:

    預設情況下，`git push` 不會將 tags 推送到遠端倉庫。使用以下指令可以推送所有 tags 或指定的 tag。

    ```bash
    git push --tags
    git push origin <tag_name>
    git push origin v1.0
    ```

5. **刪除 tag**:

    ```bash
    git tag -d <tag_name>
    git tag -d v1.0
    ```

6. **查看 tag**:

    從界面點擊進入查看。

7. **使用 tag**:

    - **回到特定版本**:

        ```bash
        git checkout v1.0
        ```

    - **用 tag 標記你的發布版本**
    - **使用 `git diff` 比較兩個版本**:

        ```bash
        git diff v1.0..v2.0
        ```

    - **追蹤修改歷史**:

        ```bash
        git log
        ```

---

END