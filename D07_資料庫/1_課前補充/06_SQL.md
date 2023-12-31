# 關聯式資料庫管理系統（RDBMS）

_Relational Database_

<br>

## 成員

MySQL、PostgreSQL、Oracle Database 和 Microsoft SQL Server 等。

<br>

## 主要特點

1. 表格結構

   - 資料以表格的形式儲存，每個表格稱為一個 `關聯`（relation），相當於一個二維表。
   - 表格由 `行（records）` 和 `欄位（columns）` 組成，每行代表一條 `記錄` ，每欄位代表一個數據類型。

<br>

2. 資料類型

   - 每個欄位都有指定的資料類型，如整數、浮點數、字串等。

<br>

3. 主鍵和外鍵

   - 每個表格通常有一個 `主鍵 (primary key)` ，用於唯一識別表中的每條記錄。
   - 表格間可以通過 `外鍵 (foreign key)` 建立關聯，外鍵是一個表中的欄位，它是另一個表的主鍵。

<br>

4. 標準化查詢語言（SQL）

   - 使用結構化查詢語言（SQL）進行資料的查詢、更新、插入和刪除。
   - 支援建立視圖、儲存程序和函數等進階資料庫功能。

<br>

5. 交易管理

   - 支援 `交易（transactions）`，這是一組原子性（Atomicity）的資料庫操作序列，要麼全部執行，要麼全部不執行，以確保資料庫的一致性和完整性。

<br>

6. 數據完整性

   - 通過完整性約束（如唯一性約束、檢查約束）來確保資料的準確性和可靠性。

<br>

7. 數據保護

   - 提供用戶權限管理，以控制對數據的訪問和操作。

<br>

8. 支援標準化

   - 符合 ACID 屬性（原子性、一致性、隔離性、持久性），確保了資料庫交易是可靠和穩定的。

<br>

9. 擴展性和維護性

   - 設計來應對不同大小的數據集，從小型應用程序到大型企業系統。
   - 通過索引、分區和優化查詢等技術提高性能。

<br>

10. 多用戶環境

    - 支援多用戶環境，允許多個用戶同時訪問和操作資料庫。

<br>

---

_END_