# shebang

_使用 `#!/bin/bash` 是指定腳本由哪個解釋器來執行，這個特殊語法稱為 `shebang`。_

<br>

## 使用原因

1. 指定解釋器：告訴操作系統這個腳本應該由 Bash 解釋器來執行。如果沒有這行代碼，操作系統可能不知道應該用哪個解釋器來執行這個腳本，特別是在 Unix 或 Linux 系統中。

<br>

2. 可移植性：雖然大多數 Unix/Linux 系統預設的 shell 是 Bash，但並不是所有的系統都如此。指定 `#!/bin/bash` 可以確保腳本在任何 Unix/Linux 系統上都能使用 Bash 來運行，這提高了腳本的可移植性。

<br>

3. 功能完整性：不同的 shell 有不同的語法和功能，其中 Bash 是一個功能強大的 shell，支持許多高級的腳本編寫功能；指定使用 Bash 可以確保腳本能夠利用 Bash 的所有功能。

<br>

## 範例

1. 編寫腳本時，第一行為 `#!/bin/bash`。

    ```bash
    #!/bin/bash

    echo "Hello, World!"
    ```

<br>

___

_END_