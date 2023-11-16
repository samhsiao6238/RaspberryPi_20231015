# widgets 的方法

<br>

## 1. `select()`

1. 功能：選取或取消選擇控制元件。
2. 可調用物件：Checkbutton, Radiobutton。
3. 調用方式。

    ```python
    # Checkbutton 實例 checkbutton
    checkbutton.select()
    ```
    
4. 詳細範例

    ```python
    import tkinter as tk
    from tkinter import ttk

    # 初始化 Tkinter
    root = tk.Tk()
    root.title("基本模板")

    # 創建一個 Checkbutton
    checkbutton = tk.Checkbutton(
        root, 
        text="選項"
    )
    checkbutton.pack()

    # 按鈕點擊事件處理函數
    def select_checkbutton():
        # 調用 Checkbutton 的 select() 方法
        checkbutton.select()

    # 創建一個按鈕來觸發 Checkbutton 的 select() 方法
    select_button = ttk.Button(
        root, 
        text="選取 Checkbutton", 
        command=select_checkbutton
    )
    select_button.pack()

    # 主循環
    root.mainloop()
    ```

<br>

## 2. `deselect()`

1. 功能：取消選取已選取的控制元件。
2. 可調用物件：Checkbutton, Radiobutton。
3. 調用方式。

    ```python
    # Checkbutton 實例 checkbutton
    checkbutton.deselect()
    ```

4. 詳細範例。

    ```python
    import tkinter as tk
    from tkinter import ttk

    # 初始化 Tkinter
    root = tk.Tk()
    root.title("基本模板")

    # 創建一個 Checkbutton
    checkbutton = tk.Checkbutton(
        root, 
        text="選項"
    )
    checkbutton.pack()

    # 按鈕點擊事件處理函數
    def deselect_checkbutton():
        # 調用 Checkbutton 的 deselect() 方法
        checkbutton.deselect()

    # 創建一個按鈕來觸發 Checkbutton 的 deselect() 方法
    deselect_button = ttk.Button(
        root, 
        text="取消選取 Checkbutton", 
        command=deselect_checkbutton
    )
    deselect_button.pack()

    # 主循環
    root.mainloop()
    ```

<br>

## 3. `flash()`

1. 功能：使按鈕快速變化其正常和活動狀態。
2. 可調用物件：Button。

3. 調用方式。

    ```python
    # Button 實例 button
    button.flash()
    ```

4. 詳細範例。

    ```python
    import tkinter as tk

    # 初始化 Tkinter
    root = tk.Tk()
    root.title("基本模板")

    # 使用標準 Tkinter Button 而不是 ttk.Button
    button = tk.Button(
        root, 
        text="閃爍按鈕"
    )
    button.pack()

    # 按鈕點擊事件處理函數
    def flash_button():
        # 調用 Button 的 flash() 方法
        button.flash()

    # 創建一個按鈕來觸發 Button 的 flash() 方法
    flash_button = tk.Button(
        root, 
        text="觸發閃爍", 
        command=flash_button
    )
    flash_button.pack()

    # 主循環
    root.mainloop()
    ```

<br>

## 4. `invoke()`

1. 功能：手動觸發控制元件的命令。
2. 可調用物件：Button, Menu。

3. 調用方式。
   
    ```python
    # Button 實例 button
    button.invoke()
    ```

    _詳細範例_

    ```python
    import tkinter as tk

    # 初始化 Tkinter
    root = tk.Tk()
    root.title("示範 invoke 方法")

    # 創建一個按鈕，當被點擊時會顯示一條訊息
    def button_clicked():
        print("按鈕被點擊了！")

    button = tk.Button(
        root,
        text="點擊我",
        command=button_clicked
    )
    button.pack()

    # 按鈕點擊事件處理函數
    def trigger_button_click():
        # 使用 invoke 方法手動觸發 button 的點擊事件
        button.invoke()

    # 創建另一個按鈕，用於觸發第一個按鈕的點擊事件
    invoke_button = tk.Button(
        root,
        text="觸發第一個按鈕的點擊",
        command=trigger_button_click
    )
    invoke_button.pack()

    # 主循環
    root.mainloop()
    ```
    - 第一個按鈕 button 綁定了 button_clicked 函數，在按鈕被點擊時會觸發所綁定的函數。
    - 第二個按鈕 invoke_button 則使用 trigger_button_click 函數，該函數呼叫 button.invoke()，這會模擬第一個按鈕被點擊的行為。
    - 這種模式常用於程式測試或者在某些特定情況下需要程式自動觸發按鈕事件的場景。

<br>

## 5. `toggle()`

1. 功能：切換控制元件的狀態。
2. 可調用物件：Checkbutton。

3. 調用方式。

    ```python
    # Checkbutton 實例 checkbutton
    checkbutton.toggle()
    ```


4. 詳細範例。

    ```python
    import tkinter as tk

    # 初始化 Tkinter
    root = tk.Tk()
    root.title("示範 toggle 方法")

    # 創建一個 Checkbutton
    check_var = tk.BooleanVar()  # Checkbutton 的變量
    checkbutton = tk.Checkbutton(
        root, 
        text="選項", 
        variable=check_var
    )
    checkbutton.pack()

    # 按鈕點擊事件處理函數
    def toggle_checkbutton():
        # 調用 Checkbutton 的 toggle() 方法來切換其狀態
        checkbutton.toggle()

    # 創建一個按鈕來觸發 Checkbutton 的 toggle() 方法
    toggle_button = tk.Button(
        root, 
        text="切換 Checkbutton 狀態", 
        command=toggle_checkbutton
    )
    toggle_button.pack()

    # 主循環
    root.mainloop()
    ```

<br>

## 6. `get()`

1. 功能：獲取控制元件的當前值。
2. 可調用物件：Entry, Spinbox。

3. 調用方式。

    ```python
    # Entry 實例 entry
    value = entry.get()
    ```


4. 詳細範例。

    ```python
    import tkinter as tk

    # 初始化 Tkinter
    root = tk.Tk()
    root.title("示範 get 方法")

    # 創建一個 Entry
    entry = tk.Entry(root)
    entry.pack()

    # 按鈕點擊事件處理函數
    def show_entry_content():
        # 使用 get() 方法獲取 Entry 控制元件的當前值
        content = entry.get()
        print("Entry 中的內容:", content)

    # 創建一個按鈕來顯示 Entry 中的內容
    show_button = tk.Button(
        root, 
        text="顯示 Entry 內容", 
        command=show_entry_content
    )
    show_button.pack()

    # 主循環
    root.mainloop()
    ```

<br>

## 7. `set()`

1. 功能：設置控制元件的值。
2. 可調用物件：StringVar, IntVar。
3. 調用方式。

    ```python
    # StringVar 實例 string_var
    string_var.set('Hello World')
    ```

4. 詳細範例。

    ```python
    import tkinter as tk
    import random

    # 初始化 Tkinter
    root = tk.Tk()
    root.title("示範 set 方法")

    # 創建一個 StringVar 變量
    text_var = tk.StringVar()

    # 創建一個 Label，並將其 text 屬性與 StringVar 變量綁定
    label = tk.Label(
        root, 
        textvariable=text_var
    )
    label.pack()

    # 定義一組隨機選擇的文本
    texts = [
        "你好，Tkinter！", 
        "歡迎使用 Python！", 
        "祝您有美好的一天！", 
        "探索 Tkinter 的樂趣！", 
        "隨機文本展示！"
    ]

    # 按鈕點擊事件處理函數
    def update_text():
        # 從 texts 列表中隨機選取一個文本
        selected_text = random.choice(texts)
        # 使用 set() 方法更新 StringVar 變量的值
        text_var.set(selected_text)

    # 創建一個按鈕來更新 Label 中的文字
    update_button = tk.Button(
        root, 
        text="更新文字", 
        command=update_text
    )
    update_button.pack()

    # 主循環
    root.mainloop()
    ```

<br>

## 8. `delete()`

1. 功能：刪除文本框或文字控件中的內容。
2. 可調用物件：Entry, Text。
3. 調用方式。

    ```python
    # Entry 實例 entry
    entry.delete(0, 'end')
    ```

4. 詳細範例。

    ```python
    import tkinter as tk

    # 初始化 Tkinter
    root = tk.Tk()
    root.title("示範 delete 方法")

    # 創建一個 Entry
    entry = tk.Entry(root)
    entry.pack()

    # 按鈕點擊事件處理函數，用於刪除 Entry 中的內容
    def delete_entry_content():
        # 使用 delete() 方法刪除 Entry 控制元件中的所有文本
        # 第一個參數是刪除開始的位置，第二個參數是刪除結束的位置
        # '0' 表示從文本的開始，'end' 表示到文本的結尾
        entry.delete(0, 'end')

    # 創建一個按鈕來刪除 Entry 中的內容
    delete_button = tk.Button(
        root, 
        text="清空 Entry 內容", 
        command=delete_entry_content
    )
    delete_button.pack()

    # 主循環
    root.mainloop()
    ```

<br>

## 9. `insert()`

1. 功能：在文本框或文字控件中插入內容。
2. 可調用物件：Entry, Text。

3. 調用方式。

    ```python
    # Entry 實例 entry
    entry.insert(0, 'Hello World')
    ```

4. 詳細範例。

    ```python
    import tkinter as tk

    # 初始化 Tkinter
    root = tk.Tk()
    root.title("示範 insert 方法")

    # 創建一個 Entry
    entry = tk.Entry(root)
    entry.pack()

    # 按鈕點擊事件處理函數，用於在 Entry 中插入文本
    def insert_text():
        # 使用 insert() 方法在 Entry 控制元件的當前光標位置插入文本
        # 第一個參數是插入文本的位置，'0' 表示文本的開始位置
        # 第二個參數是要插入的文本
        entry.insert(0, "你好，Tkinter！")

    # 創建一個按鈕來插入文本到 Entry 中
    insert_button = tk.Button(
        root, 
        text="插入文本到 Entry", 
        command=insert_text
    )
    insert_button.pack()

    # 主循環
    root.mainloop()
    ```

<br>

## 10. `configure()`

1. 功能：用於動態地改變控制元件的配置。

2. 可調用物件：多數。

3. 調用方式。

    ```python
    # Button 實例 button
    button.configure(text='Click Me')
    ```
4. 詳細範例。

    ```python
    import tkinter as tk
    import random

    # 初始化 Tkinter
    root = tk.Tk()
    root.title("示範 configure 方法")

    # 創建一個 Label
    label = tk.Label(root, text="這是一個 Label")
    label.pack()

    # 定義三個隨機顏色
    colors = [
        "yellow", 
        "green", 
        "blue"
    ]

    # 按鈕點擊事件處理函數，用於更改 Label 的屬性
    def change_label_properties():
        # 從 colors 列表中隨機選擇一個顏色
        selected_color = random.choice(colors)
        # 使用 configure() 方法更新 Label 的背景顏色
        label.configure(text="文本已改變", bg=selected_color)

    # 創建一個按鈕來更改 Label 的屬性
    change_button = tk.Button(
        root, 
        text="更改 Label 屬性", 
        command=change_label_properties
    )
    change_button.pack()

    # 主循環
    root.mainloop()
    ```

<br>

## 11. `bind()`

1. 功能：將事件綁定到函數或方法上。

2. 可調用物件：全部。

3. 調用方式。

    ```python
    # Entry 實例 entry
    entry.bind('<Return>', lambda e: print('Return key pressed'))
    ```
4. 詳細範例。

    ```python
    import tkinter as tk

    # 初始化 Tkinter
    root = tk.Tk()
    root.title("示範 bind 方法")

    # 創建一個 Entry
    entry = tk.Entry(root)
    entry.pack()

    # 事件處理函數，當在 Entry 中按下鍵盤時觸發
    def on_key_press(event):
        print(f"按下了鍵: {event.char}")

    # 使用 bind() 方法為 Entry 控制元件綁定鍵盤事件
    # '<Key>' 是鍵盤按鍵事件的標示符
    entry.bind('<Key>', on_key_press)

    # 主循環
    root.mainloop()
    ```
    - 使用 entry.bind('<Key>', on_key_press) 方法為 Entry 控制元件綁定了一個鍵盤事件，每當用戶在 Entry 中按下任何鍵時，都會觸發 on_key_press 函數。

<br>

_以下是三種佈局，詳細請參考佈局管理器_

<br>

## 12. `pack()`

1. 功能：使用包裝管理器來排列控制元件。
2. 可調用物件：全部。

3. 調用方式。

    ```python
    # Button 實例 button
    button.pack()
    ```

4. 詳細範例。

    ```python
    import tkinter as tk

    # 初始化 Tkinter
    root = tk.Tk()
    root.title("示範 pack 方法")

    # 創建多個 Label，並使用 pack() 來排列
    label1 = tk.Label(root, text="第一個 Label", bg="yellow")
    label2 = tk.Label(root, text="第二個 Label", bg="green")
    label3 = tk.Label(root, text="第三個 Label", bg="blue")

    # 使用 pack() 方法排列 Label
    # pack() 允許指定排列方式，如 top, bottom, left, right
    label1.pack(side="top")
    label2.pack(side="top")
    label3.pack(side="top")

    # 主循環
    root.mainloop()
    ```

<br>

## 13. `grid()`

1. 功能：使用網格管理器來排列控制元件。
2. 可調用物件：全部。

3. 調用方式。

    ```python
    # Button 實例 button
    button.grid(row=0, column=0)
    ```

4. 詳細範例。

    ```python
    import tkinter as tk

    # 初始化 Tkinter
    root = tk.Tk()
    root.title("示範 grid 方法")

    # 創建多個 Label，並使用 grid() 來排列
    label1 = tk.Label(root, text="第一行，第一列", bg="yellow")
    label2 = tk.Label(root, text="第一行，第二列", bg="green")
    label3 = tk.Label(root, text="第二行，第一列", bg="blue")

    # 使用 grid() 方法排列 Label
    # grid() 允許指定控制元件應該放置在網格的哪一行和哪一列
    label1.grid(row=0, column=0)
    label2.grid(row=0, column=1)
    label3.grid(row=1, column=0)

    # 主循環
    root.mainloop()
    ```

<br>

## 14. `place()`

1. 功能：使用放置管理器來排列控制元件，可以精確指定控制元件的位置和大小。
2. 可調用物件：全部。

3. 調用方式。

    ```python
    # Button 實例 button
    button.place(x=50, y=100)
    ```

4. 詳細範例。

    ```python
    import tkinter as tk

    # 初始化 Tkinter
    root = tk.Tk()
    root.title("示範 place 方法")

    # 創建多個 Label，並使用 place() 來定位
    label1 = tk.Label(root, text="A", bg="yellow")
    label2 = tk.Label(root, text="B", bg="green")
    label3 = tk.Label(root, text="C", bg="blue")

    # 使用 place() 方法定位 Label
    # place() 允許指定控制元件的精確位置和大小
    # x 和 y 指定了控制元件的位置，width 和 height 指定了控制元件的大小
    label1.place(x=0, y=0, width=100, height=50)
    label2.place(x=150, y=0, width=20, height=50)
    label3.place(x=75, y=100, width=50, height=50)

    # 主循環
    root.mainloop()
    ```

<br>

---

_END_
