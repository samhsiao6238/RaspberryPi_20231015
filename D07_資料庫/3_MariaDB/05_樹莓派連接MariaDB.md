# 連接 MariaDB

_在樹莓派上使用 Python 連接 MariaDB 做應用，有多個資料庫可以選擇，以下將介紹其中三個_

<br>

## 說明

<br>

### mariadb

1. 開發與維護：MariaDB 官方推薦的 Python 連接器。
2. 實現方式：使用了 C 擴展。
3. 特色：專注於 MariaDB，效能佳。
4. 套件安裝

    ```bash
    sudo apt-get install libmariadb-dev
    pip install mariadb
    ```

<br>

5. 範例

    ```python
    import mariadb

    config = {
        'user': 'your_username',
        'password': 'your_password',
        'host': 'localhost',
        'database': 'your_database',
        'port': 3306
    }

    # 連接資料庫
    conn = mariadb.connect(**config)
    cursor = conn.cursor()

    # 查詢
    cursor.execute("SELECT * FROM your_table")
    for row in cursor:
        print(row)

    # 關閉連線
    cursor.close()
    conn.close()
    ```


<br>

### pymysql

1. 開發與維護：Oracle（MySQL 的擁有者和開發者）官方。
2. 實現方式：可以使用純 Python 實現，也可以使用 C 擴展。
3. 特色：主要針對 MySQL 通用庫，效能佳。
4. 套件安裝

    ```bash
    pip install pymysql
    ```

<br>

5. 範例

    ```python
    import pymysql

    conn = pymysql.connect(
        host='localhost',
        user='your_username',
        password='your_password',
        db='your_database',
        charset='utf8mb4'
    )

    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM your_table"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                print(row)
    finally:
        conn.close()
    ```

<br>

### mysql-connector-python

1. 開發與維護：由社區維護的獨立項目。
2. 實現方式：完全用 Python 寫的，使得更易於安裝和分發。
3. 特色：是個通用庫，並與多個版本 Python 兼容。
4. 套件安裝

    ```bash
    pip install mysql-connector-python    
    ```

<br>

5. 範例

    ```python
    import mysql.connector

    config = {
        'user': 'your_username',
        'password': 'your_password',
        'host': 'localhost',
        'database': 'your_database',
        'port': 3306
    }

    conn = mysql.connector.connect(**config)

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM your_table")

    for row in cursor:
        print(row)

    cursor.close()
    conn.close()
    ```


<br>

---

_END_