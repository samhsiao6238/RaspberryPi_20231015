_對於想投入程式設計職人領域的同學可以參考_

# 說明安裝 Conda 時生成的環境參數

_Linux 系統上最常見的 shell scripting 語言_

<br>

## 腳本內容片段

```bash
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/sam6238/miniforge3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/sam6238/miniforge3/etc/profile.d/conda.sh" ]; then
        . "/home/sam6238/miniforge3/etc/profile.d/conda.sh"
    else
        export PATH="/home/sam6238/miniforge3/bin:$PATH"
    fi
fi
unset __conda_setup
if [ -f "/home/sam6238/miniforge3/etc/profile.d/mamba.sh" ]; then
    . "/home/sam6238/miniforge3/etc/profile.d/mamba.sh"
fi
# <<< conda initialize <<<

```
<br>

## 說明
1. 這段程式碼是由 `conda init` 添加到 `shell` 啟動檔案中的，這個部分確保啟動一個新的 `shell` 視窗時，Conda 的環境和命令行工具如 `conda activate` 能夠正常工作。

2. `# >>> conda initialize >>>` 和 `# <<< conda initialize <<<`: 這些註釋用於標記由 `conda init` 管理的區塊的開始和結束。

3. `__conda_setup="$('/home/sam6238/miniforge3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"`: 這行嘗試運行 Conda 的 `shell.bash hook` 命令，這個命令回傳需要被評估 (evaluated) 的 shell 命令來正確地初始化 Conda。這些命令被儲存在 `__conda_setup` 變數中。

4. `if [ $? -eq 0 ]; then`: 這行檢查前一個命令的退出狀態，通常表示命令是否成功執行。

5. `eval "$__conda_setup"`: 如果 `shell.bash hook` 命令成功，則運行 (execute) `__conda_setup` 變數中的命令。

_可特別注意這段語法_

6. `else ... fi`: 如果 `shell.bash hook` 命令失敗，這段程式碼會查看 `/home/sam6238/miniforge3/etc/profile.d/conda.sh` 是否存在，如果存在，它將會執行 `source` 這個檔案；如果不存在，則會將 Conda 的 `bin` 目錄加入到 `PATH` 變數中。

7. `unset __conda_setup`: 這將移除 `__conda_setup` 變數，以確保它不會無意間在後續的 shell 操作中被使用。

8. `if [ -f "/home/sam6238/miniforge3/etc/profile.d/mamba.sh" ]; then`: 檢查 `mamba.sh` 是否存在，如果存在，它會被 source，確保了 Mamba 的功能也可以在新的 shell 會話中使用，而 Mamba 是一個 Conda 的快速替代品。

<br>

---

_END_