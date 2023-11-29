# Place

_Place 佈局管理器_

<br>

## 說明

1. `place` 佈局管理器允許將控制元件放置在視窗的絕對或相對位置，主要用於需要精確控制控制元件位置和大小的場景。

<br>

## 參數

_說明以下各項目_

1. anchor
2. x、y
3. relx、rely
4. width、height
5. relwidth、relheight
6. bordermode

<br>

### 1. anchor

1. 說明：設置控制元件在其父控制元件中的對齊方式。
2. 取值：N、E、S、W、NW、NE、SW、SE、CENTER。
3. 範例：

    ```python
    widget.place(anchor="nw")
    ```

<br>

### 2. x、y

1. 說明：設置控制元件左上角的絕對座標（像素為單位）。
2. 範例：

    ```python
    widget.place(x=50, y=100)
    ```

<br>

### 3. relx、rely

1. 說明：設置控制元件相對於父容器的位置。
2. 範例：

    ```python
    widget.place(relx=0.5, rely=0.5)
    ```

<br>

### 4. width、height

1. 說明：設置控制元件的寬度和高度。
2. 範例：

    ```python
    widget.place(width=100, height=50)
    ```

<br>

### 5. relwidth、relheight

1. 說明：設置控制元件相對於父容器的寬度和高度。
2. 範例：

    ```python
    widget.place(relwidth=0.5, relheight=0.3)
    ```

<br>

### 6. bordermode

1. 說明：設置控制元件大小和位置是相對於內部還是包括邊框。
2. 取值：INSIDE、OUTSIDE。
3. 範例：

    ```python
    widget.place(bordermode="outside")
    ```

<br>

## place 的函數

_說明以下函數_

1. place_slaves()
    - 返回本組件的所有子組件物件列表。
    - 範例：
        ```python
        slaves = root.place_slaves()
        print("使用 place 的子組件:", slaves)
        ```

<br>

2. place_configure(option=value)
    - 為 place 佈局管理器設置屬性。
    - 範例：
        ```python
        widget.place_configure(x=100, y=50)
        ```

<br>

3. place_info()
    - 返回 place 提供的選項所對應的值。
    - 範例：
        ```python
        info = widget.place_info()
        print("Widget place 信息:", info)
        ```

<br>

4. place_forget()
    - 將使用 place 佈局的控制元件隱藏。
    - 範例：
        ```python
        widget.place_forget()
        ```

<br>

---

_END_