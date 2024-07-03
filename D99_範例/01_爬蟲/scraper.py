# 這個模組定義了一個抽象父類和一個從它繼承的子類來實現網頁抓取。
import requests
from lxml import html

# 定義一個基礎的網頁抓取類別
class WebScraper:
    # 初始化方法，設置URL
    def __init__(self, url):
        self.url = url

    # 定義一個方法，該方法需要被子類實現
    def fetch_data(self):
        raise NotImplementedError("Subclasses must implement this method")

# 定義一個從WebScraper繼承的類別
class MyScraper(WebScraper):
    # 覆寫fetch_data方法
    def fetch_data(self):
        # 發送HTTP請求取得網頁內容
        response = requests.get(self.url)
        # 如果HTTP響應狀態碼為200，表示成功取得網頁
        if response.status_code == 200:
            # 解析HTML內容
            tree = html.fromstring(response.content)
            # 初始化一個空列表來儲存標題
            titles = []
            # 使用XPath抓取前九個新聞標題
            for i in range(1, 10):  # 從1到9
                # 構造XPath查詢表達式
                xpath_expression = f"//div[@class='jsx-755818609 news__content__panel--item'][{i}]/a[@class='jsx-755818609 ']"
                # 執行XPath查詢
                title_element = tree.xpath(xpath_expression)
                # 檢查是否有找到標題元素
                if title_element:
                    # 取得標題文本
                    full_title = title_element[0].text_content().strip()
                    # 透過空格分割標題文本，以移除日期部分
                    title_parts = full_title.split(' ', 1)
                    # 檢查分割後是否有兩部分
                    if len(title_parts) > 1:
                        # 將日期部分移除，僅保留標題
                        title_text = title_parts[1]
                    else:
                        # 如果分割後沒有兩部分，保留原標題
                        title_text = full_title
                    # 將處理後的標題添加到列表中
                    titles.append(title_text)
                else:
                    # 如果找不到標題元素，結束循環
                    break
            # 返回所有抓取到的標題
            return titles
        else:
            # 如果網頁無法成功取得，返回None
            return None

if __name__ == '__main__':
    # 實例化MyScraper，並傳入鉅亨網新聞的URL
    scraper = MyScraper('https://www.cnyes.com/')
    # 調用fetch_data方法抓取數據
    titles = scraper.fetch_data()
    # 如果成功取得到標題，則列印出來
    if titles:
        for idx, title in enumerate(titles):
            print(f"標題 {idx+1}：{title}")
    else:
        print("無法取得網頁數據")

