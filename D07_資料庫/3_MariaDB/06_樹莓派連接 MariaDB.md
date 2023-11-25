# 連接 MariaDB

<br>

## 說明

_在樹莓派上使用 Python 連接 MariaDB 做應用，有多個資料庫可以選擇，以下將介紹其中三個。_

<br>

## pymysql

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

# 資料庫連接資訊
host = 'localhost'
user = 'your_username'
password = 'your_password'
db_name = 'your_database'
your_table = 'your_table'


# 建立資料庫連接，但暫時不指定特定的資料庫
conn = pymysql.connect(
    host=host, 
    user=user, 
    password=password, 
    # 在 MySQL 中，utf8 是一種字元集，最多能夠編碼 3 個位元的 Unicode 字元
    # utf8mb4 是 utf8 的超集，支持最多 4 個位元的 Unicode 字元。
    # utf8mb4 能夠編碼所有當前的 Unicode 字元。
    charset='utf8mb4'
)

try:
    cursor = conn.cursor()
    # 檢查資料庫是否存在
    cursor.execute(f"SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{db_name}'")
    result = cursor.fetchone()
    if not result:
        # 如果資料庫不存在，則創建它
        cursor.execute(f"CREATE DATABASE {db_name}")
        print(f"資料庫 {db_name} 建立成功。")
    else:
        print(f"資料庫 {db_name} 已經存在。")

    # 關閉游標
    cursor.close()

    # 重新建立連接到新建或已存在的資料庫
    conn.close()
    conn = pymysql.connect(host=host, user=user, password=password, db=db_name, charset='utf8mb4')

    # 
    with conn.cursor() as cursor:
        sql = f"SELECT * FROM {your_table}"
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            print(row)

finally:
    # 確保最後關閉連接
    conn.close()
```

<br>

6. 以上腳本會先檢查資料庫是否存在，假如沒有檢查，當資料庫不存在時，會出現 `OperationalError: (1049, "Unknown database 'XXXX'")` 錯誤。

<br>

7. 可前往樹莓派資料庫查詢是否確實建立。

    ```bash
    show databases;
    ```

<br>

## mysql-connector-python

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
## mariadb

_後續將以這個套件為主_

<br>

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

---

_END_