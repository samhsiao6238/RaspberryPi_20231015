# Git 全局配置

1. 查看當前的全局配置。

    ```bash
    git config --global --list
    ```

    _輸出_

    ```bash
    #  Git 用戶名、郵箱地址
    user.name=samhsiao6238
    user.email=samhsiao6238@gmail.com
    # Git LFS 相關設置，在文件進行清理時應該執行的命令
    filter.lfs.clean=git-lfs clean -- %f
    # Git LFS 相關設置，在文件被檢出時應該執行的命令
    filter.lfs.smudge=git-lfs smudge -- %f
    # 設置 Git LFS 的過濾過程
    filter.lfs.process=git-lfs filter-process
    # 設置 Git 必須使用 LFS 過濾器
    filter.lfs.required=true
    ```

<br>

2. 取消全局帳號、郵箱設置。

    ```bash
    git config --global --unset user.name
    git config --global --unset user.email
    # 其他設置也是相同
    git config --global --unset <參數名稱>
    ```

<br>

3. 移除後，如需再次設置，可重新執行設置命令。

    ```bash
    git config --global user.name "Your Name"
    git config --global user.email "your_email@example.com"
    ```

<br>

___

_END_