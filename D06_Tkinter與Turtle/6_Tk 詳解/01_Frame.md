# Tkinter - Frame

<br>

## 說明

1. Frame 的主要用途就是作為其他元件的 `根容器` 。

2. 除了 Frame 以外，其他可作為根容器的元件有 Canvas 及 PanedWindow，但不如 Frame 好用。

<br>

## Frame 的參數

| 參數                    | 說明                             | 預設 | 範例                             |
| ----------------------- | -------------------------------- | ---- | -------------------------------- |
| `bg / background`     | 背景色                           | 系統 | `background='red'`             |
| `bd / borderwidth`    | 邊界寬度                         | 2    | `borderwidth=5`                |
| `cursor`              | 鼠標滑過形狀                     | 無   | `cursor='cross'`               |
| `height`              | 高度（行數）                     | 0    | `height=5`                     |
| `width`               | 寬度（字符數）                   | 0    | `width=10`                     |
| `highlightbackground` | 非焦點時的顏色                   | 系統 | `highlightbackground='yellow'` |
| `highlightcolor`      | 取得焦點時的顏色                 | 系統 | `highlightcolor='blue'`        |
| `highlighthickness`   | 取得焦點的厚度                   | 1    | `highlighthickness=3`          |
| `relief`              | 框架型式                         | FLAT | `relief='sunken'`              |
| `pack_propagate`      | Frame 是否自動適應內部部件的大小 | True |  `pack_propagate(0)`  |        

<br>

## 補充說明

1. `frame.pack_propagate(0)` 與 `frame.pack_propagate(1)`

   - 可使用布林值如 `pack_propagate(False)` 與 `pack_propagate(True)`。
   - 用於控制容器（如Frame）大小，參數設為 0 則容器的大小將不會根據其內部部件的大小自動變化。
   - `pack_propagate(0)` 會關閉擴散（propagation）行為，即使容器內部部件增大或縮小，容器仍將保持不變。
   - 如不使用 `pack_propagate(0)` 或使用 `pack_propagate(1)`（這是預設行為），那容器的大小就會根據內部部件的大小自動調整。
   - `pack_propagate()` 方法只有兩種參數：0 或 1，分別代表關閉和開啟擴散行為。
   - 使用 `pack_propagate(0)` 可禁止 Frame 的大小自動適應內部元件的大小，這通常與手動設定的 `height` 和 `width` 屬性一起使用。

<br>

2. relief

   _它還有許多設定值，可用於控制 Frame 的外觀，讓邊界看起來是凸起或凹陷等效果。_

   - FLAT
   - SUNKEN
   - RAISED
   - GROOVE
   - RIDGE

<br>

3. height 和 width
   
   預設值為 0，表示如果未指定或由幾何管理器管理，Frame 的大小將適應其內部部件。

<br>

## 實作練習

1. 可使用前面基本架構說明的模式，先複製貼上。

   ```python
   '''導入函數'''
   # import tkinter as tk

   '''全局變數'''
   # 變數 ...

   '''實作函數'''
   # 函數 ...

   '''建立 Tk 物件'''
   # tk.Tk() ...

   '''建立根容器'''
   # tk.Frame() ...

   '''建立控件'''
   # tk.Label() ...

   '''主循環'''
   # mainloop()
   ``` 

<br>

2. 逐步將以下物件與部件加入並完成腳本。

   ```python
   # 導入函數
   import tkinter as tk

   # 建立主視窗
   root = tk.Tk()
   # 建立 Title
   root.title('Tkinter Frame 範例')

   # 建立 Frame 作為根容器
   frame = tk.Frame(
      root, 
      bg='red', 
      bd=5, 
      relief='sunken', 
      width=200, 
      height=100
   )
   # 關閉自動適應內部部件的大小，預設是開啟的，關閉後才會讓寬高等參數生效
   frame.pack_propagate(False)  
   # 切記一定要設置佈局，這裡是使用 pack() 不矩，並設置 Frame 四周有增加空間
   frame.pack(padx=10, pady=10)  

   # 在 Frame 內建立一個標籤
   label = tk.Label(
      frame, 
      text='Hello, Tkinter!', 
      bg='yellow'
   )
   # 切記要佈局
   label.pack()

   # 在 Frame 內建立一個按鈕
   button = tk.Button(
      frame, 
      text='Click Me', 
      command=lambda: label.config(text='Button Clicked!')
   )
   button.pack()

   # 啟動主循環
   root.mainloop()
   ```

<br>

___

_END_
