# 發送課程

<br>

## 安裝 Selenium 

1. 安裝並更新。

    ```bash
    pip install --upgrade selenium
    ```

<br>

2. 確認 Selenium 版本。

    ```bash
    pip show selenium
    ```

<br>

## 安裝 chromedriver

_樹莓派是 ARM 架構，需要下載適用於 aarch64 的 chromedriver，雖官方目前並未釋出 ARM 架構的 chromedriver，但可以使用以下方法進行安裝。_

<br>

1. 查看 Chrome 瀏覽器版本。

    ```bash
    chromium-browser --version
    ```

<br>

2. 使用 chromium-browser 自帶的 chromedriver。

    ```bash
    sudo apt install chromium-chromedriver
    ```

<br>

3. 查詢版本並確認安裝完成。

    ```bash
    chromedriver --version
    ```

<br>

4. 依據輸出的路徑設定代碼。

    ```bash
    CHROMEDRIVER_PATH = "/usr/bin/chromedriver"
    ```

<br>

5. 確認 chromedriver 是否具有執行權限。

    ```bash
    chmod +x /home/sam6238/Documents/chromedriver/chromedriver
    ```

<br>

## 代碼

1. 以下是專案代碼。

    ```python
    import re
    import pandas as pd
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    from bs4 import BeautifulSoup
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from dotenv import load_dotenv
    import os
    import requests
    from datetime import datetime, timedelta

    # 載入環境變數
    load_dotenv()

    # 定義 URL
    URL = "https://www.worldgymtaiwan.com/aerobic-schedule-list/taipei-minquan-east"

    # 讀取環境變數 LINE Notify Token
    LINE_NOTIFY_TOKEN = os.getenv("LINE_NOTIFY")

    # 定義關鍵字
    ALLOWED_KEYWORDS = [
        "派對", "活力有氧", "Body Jam", "熱舞", "街舞", "MV", "舞蹈"
    ]

    # 設置 ChromeDriver 路徑
    CHROMEDRIVER_PATH = "/usr/bin/chromedriver"

    # 設定 Selenium WebDriver 實例
    def setup_webdriver():
        try:
            chrome_options = Options()
            # 啟用無頭模式
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--blink-settings=imagesEnabled=false")
            chrome_options.add_argument(
                "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/115.0.0.0 Safari/537.36"
            )
            # 設定服務，傳入路徑
            service = Service(executable_path=CHROMEDRIVER_PATH)
            # 傳入服務與選項設定
            driver = webdriver.Chrome(
                service=service, 
                options=chrome_options
            )
            return driver
        except Exception as e:
            print(f"初始化 WebDriver 時發生錯誤：{e}")
            return None

    # 使用 Selenium 獲取頁面 HTML
    def download_html_selenium(url):
        driver = setup_webdriver()
        if not driver:
            return None
        try:
            print(f"正在打開網址：{url}")
            driver.get(url)
            print("等待頁面加載...")
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((
                    By.ID, 
                    "schedule-store"
                ))
            )
            page_source = driver.page_source
            print("成功獲取頁面源碼。")
            return page_source
        except Exception as e:
            print(f"使用 Selenium 獲取頁面內容時發生錯誤：{e}")
            return None
        finally:
            driver.quit()

    # 解析 HTML 內容，提取課程數據
    def parse_schedule(html_content):
        try:
            soup = BeautifulSoup(html_content, "lxml")
            schedule_store = soup.find(id="schedule-store")
            if not schedule_store:
                print("未找到課程表區域，請檢查 HTML 結構。")
                return pd.DataFrame()

            # 映射星期幾
            weekday_map = {
                "monday": "星期一",
                "tuesday": "星期二",
                "wednesday": "星期三",
                "thursday": "星期四",
                "friday": "星期五",
                "saturday": "星期六",
                "sunday": "星期日"
            }

            schedule_data = []
            for column in schedule_store.find_all(
                "div", class_="column"
            ):
                # 提取日期信息，從 `data-weekday` 屬性中提取
                weekday_attr = column.get("data-weekday")
                if not weekday_attr:
                    print(
                        "未找到 `data-weekday` 屬性，"
                        f"跳過該列: {column.prettify()[:200]}"
                    )
                    continue

                # 根據 `data-weekday` 提取對應的中文日期
                weekday = weekday_map.get(
                    weekday_attr.lower(), 
                    "未知星期"
                )
                print(f"正在處理日期: {weekday_attr} ({weekday})")

                # 提取課程信息
                for course in column.find_all("div", class_="class"):
                    # 課程名稱
                    course_name_element = course.select_one(
                        "div.class-name > p.zh"
                    )
                    if not course_name_element:
                        print(
                            "未找到課程名稱元素，"
                            f"跳過該課程: {course.prettify()[:200]}"
                        )
                        continue
                    course_name = course_name_element.get_text(strip=True)

                    # 課程時間
                    course_time_element = course.select_one("div.class-time")
                    if not course_time_element:
                        print(
                            "未找到課程時間元素，"
                            f"跳過該課程: {course.prettify()[:200]}"
                        )
                        continue
                    course_time = course_time_element.get_text(strip=True)

                    # 添加課程到數據列表
                    schedule_data.append({
                        "日期": weekday,
                        "時間": course_time,
                        "課程名稱": course_name
                    })
            
            if not schedule_data:
                print("未找到任何課程資料。")
                return pd.DataFrame()

            # 將數據轉為 DataFrame
            return pd.DataFrame(schedule_data)
        except Exception as e:
            print(f"解析課表時發生錯誤：{e}")
            return pd.DataFrame()

    # 發送 LINE Notify 通知
    def send_line_notify(message):
        try:
            url = "https://notify-api.line.me/api/notify"
            headers = {"Authorization": f"Bearer {LINE_NOTIFY_TOKEN}"}
            data = {"message": message}
            response = requests.post(url, headers=headers, data=data)
            if response.status_code == 200:
                print("成功發送 LINE 通知。")
            else:
                print(f"發送 LINE 通知失敗，狀態碼：{response.status_code}")
        except Exception as e:
            print(f"發送 LINE 通知時發生錯誤：{e}")

    # 保存課程表為 CSV
    def save_schedule_to_csv(
        schedule_df, 
        output_file="weekly_schedule.csv"
    ):
        try:
            schedule_df.to_csv(
                output_file, 
                encoding="utf-8-sig", 
                index=False
            )
            print(f"課程表已保存到 '{output_file}'。")
        except Exception as e:
            print(f"保存 CSV 文件時發生錯誤：{e}")

    # 主函數
    def main():
        html_content = download_html_selenium(URL)
        if not html_content:
            print("無法獲取頁面源碼，腳本終止。")
            return

        schedule_df = parse_schedule(html_content)
        if schedule_df.empty:
            print("課程表為空或解析失敗。")
            return

        save_schedule_to_csv(schedule_df)

        # 發送 LINE 通知
        today = datetime.now()
        next_day = today + timedelta(days=1)
        next_weekday_str = [
            "星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"
        ][next_day.weekday()]

        # 篩選目標日期的課程
        filtered_courses = schedule_df[
            schedule_df['日期'] == next_weekday_str
        ]

        if filtered_courses.empty:
            message = f"明天 ({next_weekday_str}) 沒有課程。"
        else:
            message = f"明天 ({next_weekday_str}) 的課程表如下：\n"
            for _, row in filtered_courses.iterrows():
                course_name = row['課程名稱']
                # 檢查課程名稱是否包含關鍵字
                if any(keyword in course_name for keyword in ALLOWED_KEYWORDS):
                    time = row['時間']
                    message += f"- {time}: {course_name}\n"

            # 如果沒有符合條件的課程，通知沒有符合條件的課程
            if message.strip() == f"明天 ({next_weekday_str}) 的課程表如下：":
                message = f"明天 ({next_weekday_str}) 沒有符合條件的課程。"

        send_line_notify(message)
        print(message)

    # 主程序
    if __name__ == "__main__":
        main()
    ```

<br>

___

_END_