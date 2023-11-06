# 專案模組



<br>

1. data_types.py

    ```python
    # 這個模組展示了不同的基本數據類型和基本操作。

    # 字串操作
    def string_operations():
        my_string = "Hello, World!"
        print(my_string.upper())  # 轉大寫

    # 數字操作
    def number_operations():
        my_number = 42
        print(my_number + 1)  # 加法

    # 列表操作
    def list_operations():
        my_list = [1, 2, 3]
        my_list.append(4)  # 添加元素
        print(my_list)

    # 字典操作
    def dictionary_operations():
        my_dict = {'name': 'Alice', 'age': 25}
        print(my_dict['name'])  # 獲取元素
    ```

<br>

2. scraper.py

    ```python
    # 這個模組定義了一個抽象父類和一個從它繼承的子類來實現網頁抓取。

    import requests

    class WebScraper:
        def __init__(self, url):
            self.url = url

        def fetch_data(self):
            raise NotImplementedError("Subclasses must implement this method")

    class MyScraper(WebScraper):
        def fetch_data(self):
            response = requests.get(self.url)
            if response.status_code == 200:
                return response.text
            else:
                return None
    ```

<br>

3. firebase_service.py

    ```python
    # 這個模組處理與Firebase相關的操作。

    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import firestore

    # 初始化Firebase服務
    def initialize_firebase():
        cred = credentials.Certificate("path/to/your/firebase-sdk.json")
        firebase_admin.initialize_app(cred)

    # 保存數據到Firebase
    def save_data_to_firebase(collection_name, data):
        db = firestore.client()
        db.collection(collection_name).add(data)
    ```

<br>

4. main.py

    ```python
    # 這是主文件，整合所有的模組並執行程序。

    import data_types
    from scraper import MyScraper
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
        scraper = MyScraper('http://example.com')
        data = scraper.fetch_data()
        print(data)

        # 將獲取的數據存儲到Firebase（這裡僅是示例，實際數據應從抓取的內容獲得）
        dummy_data = {'name': 'John Doe', 'age': 30}
        save_data_to_firebase('users', dummy_data)

    if __name__ == '__main__':
        main()
    ```

<br>

---

_END_