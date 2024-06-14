# tk 與 ttk

<br>

## 特別說明

1. 一般在腳本中看到的 `tk` 其實是 `tkinter` 自定義的縮寫。

   ```python
   import tkinter as tk
   ```

<br>

2. `ttk` 是 Tk 8.5 之後加入的模組。

   ```python
   import tkinter.ttk as ttk
   ```

<br>

3. 簡單說，`tkinter` 是一個模組，包含很多的 Class，如 `Tk`、`Label`、`Button` 等都是 `tkinter` 的 Class，而 `ttk` 則是 `tkinter` 的一個子模組（Submodule），這個子模組對 `tkinter` 進行了優化。

<br>

4. `ttk` 新增了6個控制元件。

   | 控件        | 名稱         | 說明                         |
   | ----------- | ------------ | ---------------------------- |
   | Combobox    | 下拉選單     | 從下拉選單中選擇或輸入一個值 |
   | Notebook    | 選項卡容器   | 多個頁面的容器               |
   | Progressbar | 進度條       |                              |
   | Separator   | 分隔線       |                              |
   | Sizegrip    | 變動視窗大小 |                              |
   | Treeview    | 多層次數據   |                              |

<br>

5. 原本的控制元件中有 11 個在 `ttk` 中進行了擴展（優化）。

   | NO | 控件        | 名稱     | 說明                                                     |
   | -- | ----------- | -------- | -------------------------------------------------------- |
   | 1  | Button      | 按鈕     |                                                          |
   | 2  | Checkbutton | 多選匡   | 可選擇或取消                                             |
   | 3  | Entry       | 輸入框   | 單行文本框                                               |
   | 4  | Frame       | 框架     | 用於組織其他控件                                         |
   | 5  | Label       | 標籤     | 用於顯示文本或圖片                                       |
   | 6  | LabelFrame  | 標籤框架 | 帶有標題的框架                                           |
   | 7  | Menubutton  | 選單按鈕 | 可以顯示下拉選單的按鈕                                   |
   | 8  | PanedWindow | 分割視窗 | 包含兩個或多個窗格的視窗                                 |
   | 9  | Radiobutton | 單選按鈕 | 從一組選項中選擇其中一個                                 |
   | 10 | Scale       | 滑動條   | 通過滑動選擇一個值                                       |
   | 11 | Scrollbar   | 滾動條   | 對支援的元件（文字域、畫布、清單框、文本框）提供滾動功能 |

<br>

___

_END_
