# 補充說明 Section

<br>

## 簡介

1. 如之前的簡介提到， `systemd` 是主流的系統服務管理器，其設定文件的副檔名為 `.service`，內容有多個 `段 （Section）` 形成的區塊所組成，如 `[Unit]`、`[Service]` 和 `[Install]` 等。

<br>

2. 這些 `段` 各自包含不同類型的設置選項，定義了服務的不同構面。

<br>

## 常用的段

<br>

### 單元 `[Unit]`

_用於描述服務單元的一般資訊，除了描述性訊息外，還包含單元間的關聯和順序。_

<br>

1. `Description`：服務的描述。

2. `Documentation`：指向相關文件的 URL。

3. `After`：定義服務啟動的順序，在哪些其他服務之後啟動。

4. `Before`：定義服務啟動的順序，在哪些其他服務之前啟動。

5. `Requires`：定義服務的嚴格依賴關係。

6. `Wants`：定義服務的非嚴格依賴關係。

<br>

### 服務 `[Service]`

_用於定義具體的服務運行方式，包括如何啟動、停止和重啟服務。_

<br>

1. `ExecStart`：定義啟動服務的命令。

2. `ExecStop`：定義停止服務的命令。

3. `ExecReload`：定義重載服務的命令。

4. `Restart`：定義服務失敗後的重啟策略。

5. `Type`：定義服務的啟動類型，如 `simple`、`forking`、`oneshot` 等。

6. `User`：指定運行服務的用戶。

7. `Group`：指定運行服務的用戶組。

<br>

### 安裝 `[Install]`

_定義服務如何安裝到系統中，特別是與 `systemctl enable` 和 `systemctl disable` 命令相關的設置。_

<br>

1. `WantedBy`：定義服務應該被哪些目標（target）所要求。

2. `RequiredBy`：定義服務必須被哪些目標所依賴。

3. `Alias`：定義服務的別名。

<br>

### 計時器 `[Timer]`

_用於定義計時器單元的設置，計時器單元用於安排定期執行的任務。_

<br>

1. `OnCalendar`：定義基於日曆的定時安排。

2. `OnBootSec`：定義在系統啟動後多少時間觸發。

3. `OnUnitActiveSec`：定義單元上次活躍後多少時間觸發。

### 套接字 `[Socket]`

_用於定義套接字單元，管理與服務通訊的套接字。_

<br>

1. `ListenStream`：定義要監聽的 TCP 流。

2. `ListenDatagram`：定義要監聽的 UDP 數據報。

3. `Accept`：定義是否為每個連接建立新的服務單元。

<br>

### 路徑 `[Path]`

_用於監控文件或目錄的改變，當發生改變時觸發對應的服務。_

<br>

1. `PathExists`：當指定的文件存在時觸發。

2. `PathChanged`：當指定的文件改變時觸發。

3. `DirectoryNotEmpty`：當指定的目錄不為空時觸發。

<br>

### 掛載 `[Mount]`

_用於定義文件系統掛載單元_

<br>

1. `What`：要掛載的設備或文件系統。

2. `Where`：掛載點。

3. `Type`：文件系統類型。

<br>

### 切片 `[Slice]`

_用於定義資源管理單元，如 CPU 和內存資源的限制_

<br>

1. `CPUQuota`：限制 CPU 使用率。

2. `MemoryMax`：限制最大內存使用量。

<br>

___

_END_