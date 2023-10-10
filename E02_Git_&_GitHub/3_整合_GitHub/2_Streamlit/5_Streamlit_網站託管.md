# Streamlit 網站託管
- 可將網站架設在官網
  
</br>

# 註冊

1. [官網](https://streamlit.io/)


2. 授權

    ![](images/img_16.png)

3. 已經建立的 Streamlit 應用清單

    ![](images/img_17.png)


4. 可以添加新的 app，這裡先不用，之後再回來添加

    ![](images/img_18.png)

</br>

## 建立網站資料

1. 建立網站資料夾
   
   ```bash
   mkdir __streamlit_web_01__
   ```
   
   ![](images/img_19.png)

2. 建立 README.md
   
   ```bash
   touch README.md
   ```
   ![](images/img_20.png)

</br>

## 將資料夾發佈到 GitHub

1. 原始碼控制
   
   ![](images/img_21.png)

2. 發佈至 GitHub
   
   ![](images/img_22.png)

3. 選取
   
   ![](images/img_23.png)

4. 勾選
   
   ![](images/img_24.png)

</br>

## 建立網站內容

1. 建立必要檔案
   - app.py
   - requirements.txt
   
   ```bash
   touch app.py requirements.txt
   ```

2. 編輯腳本
   
   ```python
   import streamlit as st
    import matplotlib.pyplot as plt
    import numpy as np
    st.title('Streamlit 與 Matplotlib')
    fig, ax = plt.subplots()
    x = np.linspace(0, 20, 100)
    ax.plot(x, np.sin(x))
    st.pyplot(fig)
    st.write('這是一個使用 Matplotlib 在 Streamlit 上繪製的線圖。')
   ```

3. 編輯依賴文件
   
   ```bash
   streamlit
    matplotlib
    numpy
   ```

</br>

## 設定 Streamlit
- 回到官網

1. 添加
   
   ![](images/img_25.png)

2. 選取倉庫
   
   ![](images/img_26.png)

3. 前一個步驟也可以手動貼上超連結
   
   ![](images/img_27.png)

4. 選擇儲存網站內容的倉庫
   
   ![](images/img_28.png)

5. 設定網站主檔案路徑
   
   ![](images/img_29.png)
   
6. 可自訂網址前綴
   
   ![](images/img_31.png)

</br>

## 進階設定與部署

1. 可選取 Advanced settings 進行其他設定
   - 之後再補充
   
   ![](images/img_32.png)

2. 完成後進行部署
   
   ![](images/img_33.png)

3. 瀏覽器會顯示烘烤的示意圖
   
   ![](images/img_34.png)

4. 完成後即可以指派的網址進行訪問
   
   ![](images/img_35.png)

</br>

---
_END：以上完成在官網上佈置站台_