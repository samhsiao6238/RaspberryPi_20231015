# 設定 sudo 群組免密碼

<br>

# 注意事項

1. 所謂的 `不需要輸入密碼`，是指用戶在使用 `sudo` 指令執行需要超級用戶權限的指令時，不需要再輸入密碼。換句話說，一旦用戶已經成功地以自己的用戶密碼執行了 sudo 指令，系統就會暫時授予該用戶超級用戶權限，允許其不必重新輸入密碼就能執行其他 sudo 指令。

<br>

2. sudo 的主配置文件位於 `/etc/sudoers`，但在 `/etc/sudoers.d` 目錄中也可能存在其他相關的配置文件。

<br>

3. 在對 `sudo` 配置進行修改時，建議不要直接編輯 `/etc/sudoers` 文件，而應該使用 `visudo` 命令或在 `/etc/sudoers.d` 下建立新的文件進行配置，以避免可能的語法錯誤影響系統安全。

<br>

## 說明權限設置的語法

_這是一個相對複雜的操作，以下只列舉幾種狀況_

<br>

1. `sudoers` 文件用於定義用戶和群組的權限，決定用戶可以 `在哪些主機上`、`以何種方式`、`執行哪些命令`、`是否需要密碼`。

<br>

2. 配置語法結構：`主機` 用以指定權限在哪些主機上有效，`標誌` 用來定義是否需要密碼或其他標誌，`NOPASSWD` 表示無需密碼，`命令` 用以指定哪些命令可以被執行，`ALL` 表示所有命令。

    ```bash
    (主機) 標誌: 命令
    ```

<br>

3. 語法範例。

    | 指令                          | 主機 | 用戶 | 群組 | 任何命令 | 無需密碼 |
    | ----------------------------- | ---- | ---- | ---- | -------- | -------- |
    | `(ALL ) : ALL`              | O    | O    |      | O        |          |
    | `(ALL : ALL) : ALL`         | O    | O    | O    | O        |          |
    | `(ALL) NOPASSWD: ALL`       | O    | O    |      | O        | O        |
    | `(ALL : ALL) NOPASSWD: ALL` | O    | O    | O    | O        | O        |

<br>

4. 在 `命令` 部分，可對多個具體命令進行設置，如下設置表示 user 可以使用 sudo 執行 ls、cat 和 tail 命令。

    ```bash
    user ALL=(ALL) /bin/ls, /bin/cat, /usr/bin/tail
    ```

<br>

5. 延續上一點，還可以允許特定命令參數，如下設置表示 user 只能使用 sudo 執行 ls /home/user 和 tail -n 10 /var/log/syslog 這兩個特定的命令和參數組合。

    ```bash
    user ALL=(ALL) /bin/ls /home/user, /usr/bin/tail -n 10 /var/log/syslog
    ```

<br>

6. 允許一個目錄下的所有命令，如下設置表示 user 可以使用 sudo 執行 /usr/bin/ 目錄下的所有命令。。

    ```bash
    user ALL=(ALL) /usr/bin/
    ```

<br>

7. 允許命令及其所有參數，如下設置表示 user 可以使用 sudo 執行 ls 命令及其所有可能的參數。

    ```bash
    user ALL=(ALL) /bin/ls *
    ```

<br>

## 開始實作

<br>

1. 編輯設定檔案。

    ```bash
    sudo visudo
    ```

<br>

2. 可看到預設權限設置如下。

    ![img](images/img_808.png)

<br>

3. 加入免密碼 `NOPASSWD`：`sudo` 群組的所有使用者可以在所有主機上，以所有使用者身份執行所有命令且無需密碼。

    ```bash
    %sudo   ALL=(ALL:ALL) NOPASSWD:ALL
    ```

<br>

4. 檢查語法是否正確。

    ```bash
    sudo visudo -c
    ```

    ![](images/img_809.png)

<br>

5. 這個編輯會自帶檢查，假設將參數 `NOPASSWD` 誤植為 `NOPASSWORD` ，系統會在儲存後提出警告。

    ![](images/img_810.png)

<br>

6. 按下 `e` 重新編輯即可。

    ![](images/img_811.png)

<br>

## 還有另一個設定檔案 `sudoers.d`

1. 在前項說明的設定檔最後一行內容。

    ![](images/img_812.png)

<br>

2. 會發現裡面有三項設定。

    ![](images/img_813.png)

<br>

3. 可透過 `cat` 語法逐一查看內容。

    ```bash
    sudo cat /etc/sudoers.d/010_at-export
    sudo cat /etc/sudoers.d/010_pi-nopasswd
    sudo cat /etc/sudoers.d/010_proxy
    ```

<br>

4. 其中 `010_pi-nopasswd` 有設定了初始的用戶 `sam6238` 免密碼。

    ![](images/img_814.png)

<br>

5. 可知透過編輯這個設定檔案也可以達到相同目的。

    ```bash
    sudo nano /etc/sudoers.d/010_pi-nopasswd
    ```

<br>

6. 將要免密碼的用戶或是 `ALL` 加入。

    ![](images/img_815.png)

<br>

___

_END_