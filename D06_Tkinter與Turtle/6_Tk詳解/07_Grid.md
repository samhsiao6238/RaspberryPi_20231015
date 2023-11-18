# grid

_Tkinter 佈局管理器，以下分別針對 Grid 的參數與函數進行說明_

<br>

## grid 的參數

_說明以下各項目_

1. row、column
2. sticky
3. rowspan、columnspan
4. ipadx、ipady
5. padx、pady

<br>

### 1. row、column

1. 說明：指定組件所在的行號和列號。
2. 取值：以序號取值，序號從 0 開始。
3. 範例：

    ```python
    # 將元件放置在第二行第三列
    widget.grid(row=1, column=2)
    ```

<br>

### 2. sticky

1. 說明：決定組件在網格中的對齊方式（若有額外空間）。
2. 取值：N、E、S、W、NW、NE、SW、SE。
3. 範例：

    ```python
    # 將元件對齊到單元格的北（上）和東（右）邊
    widget.grid(sticky="NE")
    ```

<br>

### 3. rowspan、columnspan

1. 說明：指定組件所跨越的行數或列數。
2. 範例：

    ```python
    # 讓元件跨越3行2列
    widget.grid(rowspan=3, columnspan=2)
    ```

<br>

### 4. ipadx、ipady

1. 說明：設置元件的內部間隙。
2. 範例：

    ```python
    # 設置元件內部水平和垂直間隙
    widget.grid(ipadx=5, ipady=5)
    ```

<br>

### 5. padx、pady

1. 說明：設置元件的外部間隙。
2. 範例：

    ```python
    # 設置元件外部水平和垂直間隙
    widget.grid(padx=10, pady=10)
    ```

<br>

## grid 的函數

_說明以下函數_

1. grid_slaves()
    - 返回本組件的所有子組件物件列表。
    - 範例：
        ```python
        slaves = root.grid_slaves()
        print("使用 grid 的子組件:", slaves)
        ```

<br>

2. grid_configure(option=value)
    - 為 grid 佈局管理器設置屬性。
    - 範例：
        ```python
        widget.grid_configure(row=1, column=1)
        ```

<br>

3. grid_propagate(boolean)
    - 若設置為 True，則父組件的大小由子組件決定。
    - 範例：
        ```python
        frame.grid_propagate(False)
        ```

<br>

4. grid_info()
    - 返回 grid 提供的選項所對應的值。
    - 範例：
        ```python
        info = widget.grid_info()
        print("Widget grid 信息:", info)
        ```

<br>

5. grid_forget()
    - 將使用 grid 佈局的組件隱藏，但不銷毀。
    - 範例：
        ```python
        widget.grid_forget()
        ```

<br>

6. grid_location(x, y)
    - 根據像素點返回單元格行列坐標。
    - 範例：
        ```python
        loc = frame.grid_location(50, 50)
        print("單元格位置:", loc)
        ```

<br>

7. size()
    - 返回組件所包含的單元格數量，揭示組件大小。
    - 範例：

        ```python
        size = frame.size()
        print("組件大小:", size)
        ```

<br>

---

_END_