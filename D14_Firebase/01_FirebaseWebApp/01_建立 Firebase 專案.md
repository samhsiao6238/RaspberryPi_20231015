# 建立 Firebase 專案

_這是在 Firebase 主控台建立的 Google Cloud 專案，可在 [GC](https://cloud.google.com/free?utm_source=google&utm_medium=cpc&utm_campaign=japac-TW-all-zh-dr-BKWS-all-core-trial-EXA-dr-1605216&utm_content=text-ad-none-none-DEV_c-CRE_644095273672-ADGP_Hybrid%20%7C%20BKWS%20-%20EXA%20%7C%20Txt%20~%20GCP_General_core%20brand_main-KWID_43700074766895895-aud-970366092687%3Akwd-6458750523&userloc_9040379-network_g&utm_term=KW_google%20cloud&gad_source=1&gclid=CjwKCAjw7oeqBhBwEiwALyHLM6yxfxy1e1fy44bdmMAbPSBu1sJLtWigFGMS-Ye12HF5FwfpLtxOgBoCfAUQAvD_BwE&gclsrc=aw.ds&hl=zh-tw) 直接查詢_

<br>

## 完成展示

![](images/img_34.png)

<br>

## 步驟

1. 登入 Firebase，點擊進入 [主控台 Console](https://console.firebase.google.com/) 。

    ![](images/img_37.png)   

<br>

2. 建立專案。

    ![](images/img_01.png)

<br>

3. 自訂專案名稱、然後點擊 `繼續`。

    ![](images/img_02.png)

<br>

4. 暫時先關閉分析功能，這樣可減少所需的額外設定，然後 `建立專案`。

    ![](images/img_03.png)

<br>

5. 完成後，點擊 `繼續`。

    ![](images/img_04.png)

<br>

## 專案主控台

_此時會自動進入專案主控台_

<br>

1. 專案的主控台中很多應用，這裡先從 `網頁應用` 開始。

    ![](images/img_05.png)

<br>

2. 給專案一個任意的暱稱，可以先不用選擇 `Hosting`，接著點擊 `註冊應用程式`。

    ![](images/img_06.png)

<br>

## 安裝開發工具

_畫面會開啟安裝指引_

<br>

1. 依據預設指引，選取 `Use upm` 安裝開發工具 `Firebase JavaScript SDK`，安裝的目的是在前端應用（如 Web、React）或後端應用（如 Node.js）中整合使用 Firebase 服務；特別注意兩件事，第一是必須在指令前面加上 `sudo`，否則安裝時會報錯；其次，這與安裝 Firebase 的命令列工具 `firebase-tools` 是不同的，安裝 `firebase-tools` 的主要目的是在終端機執行與 Firebase 相關的操作。

    ![](images/img_07.png)

    ```bash
    npm install firebase
    ```

<br>

2. 畫面中顯示的這段是要貼在應用腳本中的 API 資訊，可稍後再來複製，接著點擊 `前往控制台`。

    ![](images/img_08.png)

<br>

3. 這時便會看到有了 `一個應用`。

    ![](images/img_09.png)

<br>

## 設定專案

1. 點擊齒輪圖標開啟選單，接著點擊 `專案設定`。

    ![](images/img_10.png)

<br>

2. 往下滑動就可以看到剛剛的資料，以後可以來這裡重新複製。

    ![](images/img_11.png)

<br>

3. 切換到 `服務帳戶` 頁籤，使用預設選取的 `Node.js`，接著點擊 `產生新的私密金鑰`，點擊便可下載。

    ![](images/img_12.png)

<br>

4. 彈出視窗中會有一些提醒，點擊 `產生金鑰` 後會自動下載到本地電腦中。

    ![](images/img_13.png)

<br>

## Realtime Database

1. 在左側 `建構 Build` 中選取 `Realtime Database`。

    ![](images/img_14.png)

<br>

2. 選取過的服務會自動添加到 `專案捷徑 Project shortcuts` 中。

    ![](images/img_15.png)

<br>

3. 點擊 `建立資料庫 Create Database`。

    ![](images/img_16.png)

<br>

4. 選擇區域，這裡選擇比較近的 `新加坡`，然後 `下一步`。

    ![](images/img_17.png)

<br>

5. 使用預設的 `以鎖定模式啟動 Start in locked mode`，之後還會再設定修正，點擊右下角的 `啟用 Emable`。

    ![](images/img_18.png)

<br>

6. 切換到 `規則 Rukes` 頁籤，修改兩個權限設定值為 `true`，然後點擊 `發布 Publish`。

    ![](images/img_19.png)

<br>

7. 無需在意完成時的警告，這個階段先這樣設定即可。

    ![](images/img_20.png)

<br>

_至此完成初步的設定_

___

_END_