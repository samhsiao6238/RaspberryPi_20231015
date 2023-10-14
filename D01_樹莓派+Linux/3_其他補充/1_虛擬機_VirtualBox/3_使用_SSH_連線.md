# 使用 SSH 從本機連線虛擬機上的樹莓派

</br>

## 進入樹莓派虛擬機

- 開啟 SSH：虛擬機預設的 SSH 並未開啟
  
  ![](images/img_01.png)

</br>

- 設定主機名稱：虛擬機安裝時並未設定主機名稱

  *自訂名稱，如 `raspi-2023-98`*

  ![](images/img_02.png)

</br>

- 這些設定都是要重新開機的

  ![](images/img_03.png)



</br>

## 進入 Virtual Box

- 開啟應用 VirtualBox

  ![](images/img_04.png)

</br>

- 工具：網路管理員

  ![](images/img_05.png)

</br>

- 右邊會切換到網路功能設定頁面

  ![](images/img_06.png)

</br>

- 預設會有一張網卡

  ![](images/img_07.png)

</br>

- 新建網路卡

  - 原本應該有一個 `192.168.56.1`
  - 要使用這個也是可以
  - 這裡我示範建立新的

    ![](images/img_08.png)

</br>

- 會添加一個，預設狀態停用，要手動開啟並設定 IP `192.168.242.1`

  ![](images/img_09.png)

</br>

- 切換到 `DHCP 伺服器` ，勾選 `啟用伺服器` 後 `套用`

  ![](images/img_10.png)

</br>

- 啟動虛擬機

  - 進入虛擬機終端機查詢 IP

  ```bash
  ifconfig
  ```

</br>

  - 只會看到這個 `10.0.2.15` ，但不是用來連線的

    ![](images/img_11.png)

</br>

- 在本地電腦查詢：

  ```bash
  ipconfig
  ```

  *會看到虛擬機的網路卡以及 IP `192.168.242.1` *

  ![](images/img_12.png)

</br>

- 進入 VB 應用，在虛擬機上點擊 `設定`

  ![](images/img_13.png)

</br>

- 依序點選 `網路` -> `進階` -> `連接埠轉送`

  ![](images/img_14.png)

</br>

- 建立規則

  - 右側 `+` 添加規則
  - `主機 IP` 輸入 `本機上虛擬網卡的 IP`
  - `客體 IP` 輸入 `樹梅派上查詢的 IP`

  ![](images/img_15.png)

</br>

- 放大看清楚

  ![](images/img_16.png)

</br>

- 編輯 Windows 設定檔 `hosts` ，這需要管理員權限。
  *添加 IP 與主機名稱的映射*

    ```shell
    C:\Windows\System32\drivers\etc\hosts
    ```
 
  ![](images/img_17.png)

</br>

- 可使用任意編輯器
  
  ![](images/img_18.png)

</br>

- 在設定檔的最後加入
  *這裡是示意的截圖，注意要使用當前的 IP*

  ![](images/img_19.png)

</br>

- 完成後可從本地電腦用 SSH 連線虛擬機
    ```bash
    ssh sam6238@192.168.242.1
    ```

</br>

- 完成登入

  ![](images/img_20.png)

</br>

- 退出
    ```bash
    exit
    ```
    
    ![](images/img_21.png)

</br>

- 退出後可以嘗試使用 `主機名稱` 進行連線
    
    ```bash
    ssh <樹莓派帳號>@<樹莓派主機名稱>
    ```
    
    ![](images/img_22.png)

</br>

- 在 VSCode 中建立 SSH 設定檔案
  
  ![](images/img_23.png)

</br>

- 雖然通道有打開，連線失敗
  *通道打開時會詢問所要連線機器的作業系統類型*
  
  ![](images/img_24.png)
  
</br>

  *接著下個步驟會在虛擬機中安裝 VSCode 排除這個問題，再進行連線*

</br>

---

_END：以上是虛擬機的 SSH 連線設置_