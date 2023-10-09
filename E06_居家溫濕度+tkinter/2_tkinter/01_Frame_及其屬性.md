# Tkinter

## 1_Frame 及其屬性

### 說明

- 首先介紹的就是 **Frame**
- **Frame** 的主要用途就是用來作為其他元件的容器
- 其他元件如 **Canvas** 及 **PaneWindow** 也有類似 **Frame** 作為根容器的效果，但不如 **Frame** 好用。

### Frame 的參數

| 參數                    | 說明                             | 預設 | 範例                             |
| ----------------------- | -------------------------------- | ---- | -------------------------------- |
| `bg / background`     | 背景色                           | 系統 | `background='red'`             |
| `db / borderwidth`    | 邊界寬度                         | 2    | `borderwidth=5`                |
| `cursor`              | 鼠標滑過形狀                     | 無   | `cursor='circle'`              |
| `height`              | 高度（行數）                     | 0    | `height=5`                     |
| `width`               | 寬度（字符數）                   | 0    | `width=10`                     |
| `highlightbackground` | 非焦點時的顏色                   | 系統 | `highlightbackground='yellow'` |
| `highlightcolor`      | 取得焦點時的顏色                 | 系統 | `highlightcolor='blue'`        |
| `highlighthickness`   | 取得焦點的厚度                   | 1    | `highlighthickness=3`          |
| `relief`              | 框架型式                         | FLAT | `relief='sunken'`              |
| `pack_propagate(0)`   | Frame 是否自動適應內部部件的大小 | 1    |                                  |
| `pack_propagate(1)`   |                                  |      |                                  |

### 說明

1. `frame.pack_propagate(0)` 或 `frame.pack_propagate(1)`

   1. 用於控制容器（如Frame）大小，參數設為 0 則容器的大小將不會根據其內部部件的大小自動變化。
   2. `pack_propagate(0)` 會關閉擴散（propagation）行為，即使容器內部部件增大或縮小，容器仍將保持不變。
   3. 如不使用 `pack_propagate(0)` 或使用 `pack_propagate(1)`（這是預設行為），那容器的大小就會根據內部部件的大小自動調整。
   4. `pack_propagate()` 方法只有兩種參數：0 或 1，分別代表關閉和開啟擴散行為。
   5. 使用 `pack_propagate(0)` 可禁止 Frame 的大小自動適應內部元件的大小，這通常與手動設定的 `height` 和 `width` 屬性一起使用。
2. **relief**：它還有其他值如：SUNKEN、RAISED、GROOVE、RIDGE，控制 Frame 的三維外觀。
3. **height** 和 **width** 預設值為 0，表示它們會自動適應內容或手動設定的大小。

---END---
