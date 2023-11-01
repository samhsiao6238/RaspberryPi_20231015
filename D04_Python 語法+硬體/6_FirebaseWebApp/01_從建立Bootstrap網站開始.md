# 前情回顧

## 速覽

1. 登入 Firebase 並建立專案

    ![](images/img_01.png)

2. 輸入任意名稱、接受條款後繼續
   
   ![](images/img_02.png)

3. 是否使用分析功能皆可，然後建立專案
   
   ![](images/img_03.png)

4. 完成後繼續
   
   ![](images/img_04.png)

5. 主控台中很多功能，這裡先從 `網頁` 開始
   
   ![](images/img_05.png)

6. 註冊應用程式，可以先不用選擇 `Hosting`。
   
   ![](images/img_06.png)

7. 安裝開發工具 `Firebase JavaScript SDK`，這跟命令列工具是不同的。
   
   ![](images/img_07.png)
   
   ```bash
   npm install firebase
   ```

8. 這段是要貼在應用中的 API 資訊，可稍後再來複製，然後往控制台。
   
   ![](images/img_08.png)

9. 這時便會看到有了一個應用
    
    ![](images/img_09.png)

10. 點擊專案設定
    
    ![](images/img_10.png)

11. 往下滑動就可以看到剛剛的資料了，以後可以來這裡重新複製。
    
    ![](images/img_11.png)

12. 切換到服務帳戶頁籤，選取 Node.js，可以產生新的私密金鑰，點擊便可下載。
    
    ![](images/img_12.png)

13. 會有一些提醒，點擊產生金鑰完成下載。
    
    ![](images/img_13.png)
   
14. 在左側建構中選取 Realtime Database
    
    ![](images/img_14.png)

15. 選取過的服務會自動添加到捷徑中
    
    ![](images/img_15.png)

16. 選擇建立資料庫
    
    ![](images/img_16.png)

17. 選擇區域，美國新加坡皆可，然後下一步
    
    ![](images/img_17.png)

18. 以鎖定模式啟動，之後還會再設定修正，選擇啟用
    
    ![](images/img_18.png)

19. 切換到規則頁籤，修改兩個權限設定值為 `true`，然後點擊 `發布`
    
    ![](images/img_19.png)

20. 無需在意完成時的警告，這個階段先這樣設定沒關係。
    
    ![](images/img_20.png)

<br>

_至此完成初步的設定_

---

_END_