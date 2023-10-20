# 發佈至 GitHub

</br>

## 在樹莓派建立 Git 並且發佈到 GitHub 上

_注意_

- 預設會將 `當前所在目錄` 作為儲存倉庫 `Repository` ，並以當前所在資料夾的名稱作為儲存庫名稱來建立 Git。
- 以目前所在位置 `Documents` 來說，在這建立倉庫對於日後專案管理可能會帶來困擾。
- 所以建議將資料放入其他指定的資料夾，以下進行操作。

</br>

### 📌 A. 建立專案資料夾

1. 連線後先進入 `Documents` 目錄

   ![img](images/img_11.png)
   
2. 使用終端機或直接使用圖標建立資料夾

   ```bash
   mkdir <資料夾名稱> && cd <資料夾名稱>
   ```

3. 透過指令在該資料夾內開啟新的工作視窗，這樣可以確保在正確的路徑下建立倉庫。

   ```bash
   code .
   ```

4. 先建立一個 `README.md` 檔案，內容隨意輸入。
   
   ![](images/img_12.png)

   _以上完成本地資料準備_

</br>



### 📌 B. 先登入 GitHub 帳號密碼

5. 進入 VSCode 之後先啟動一個終端機
   
   ![](images/img_21.png)

6. 以 Git 指令設定用戶名稱和郵箱，這不是驗證程序，只是指定作者資訊。

   ```bash
   git config --global user.name <輸入 github 名稱>
   git config --global user.email <輸入電子郵件>
   ```

   **注意**
   
   _如果用戶名是由多個單詞組成的，例如 `John Doe`，則必須使用引號包裹。_


</br>

### 📌 C. 建立遠端連線


7. 點擊 VScode 的 `原始檔控制` 。
   
   ![](images/img_13.png)
   
8. 點擊 `發布至 GitHub` ，選擇公開或私有皆可。
   
   ![](images/img_14.png)


9. 可以使用預設名稱或自訂名稱。

   ![](images/img_16.png)
   
   ![](images/img_15.png)

10. 選擇 `README.md` 檔案後，點擊 OK。
   
      ![](images/img_17.png)
  

11. 給該提交一個版本命名後 `提交` 。

      ![](images/img_18.png)

12. 假如前面沒設定帳號密碼，這裡會跳出提示。
   
      ![](images/img_19.png)

</br>

13. 再次提交，點擊 `發佈到分支`（若需要，可不輸入訊息）。
    
      ![](images/img_20.png)

14. 同前述，自定義一個倉庫名稱，或使用預設。
    
    ![](images/img_16.png)

15. 完成後，可在 GitHub 上開啟並查看新建立的 Repo 以及 README.md。

      ![](images/img_22.png)


16. 在終端機中可以透過指令到 .git 檔案

      ![](images/img_23.png)


17. 可手動建立 .gitignore 檔案
    
    ![](images/img_24.png)

</br>

---

_END：以上成功在 GitHub 上建立新的 Repo_
