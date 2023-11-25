# main.py
import data_types
from scraper import MyScraper  # 確保這裡的導入路徑正確
from firebase_service import initialize_firebase, save_data_to_firebase

def main():
    # 展示基本數據類型操作
    data_types.string_operations()
    data_types.number_operations()
    data_types.list_operations()
    data_types.dictionary_operations()

    # 初始化Firebase
    initialize_firebase()

    # 使用網頁抓取類
    scraper = MyScraper('https://www.cnyes.com/')
    titles = scraper.fetch_data()
    
    # 判斷是否成功獲取到數據，如果有，則打印並儲存
    if titles:
        for idx, title in enumerate(titles):
            print(f"標題 {idx+1}：{title}")
        # 儲存標題到Firebase
        save_data_to_firebase('news_titles', {'titles': titles})
    else:
        print("無法獲取網頁數據")

if __name__ == '__main__':
    main()
