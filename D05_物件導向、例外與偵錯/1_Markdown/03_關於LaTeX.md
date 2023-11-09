# LaTeX

_Github 並不支援，所以這裡僅作參考_

<br>

## 說明

1. Markdown 不直接支援 LaTeX，但是許多處理 Markdown 的編輯器和系統如 Jupyter Notebooks 或 GitHub 的 README 文件是支援在 Markdown 文件中嵌入 LaTeX 語法以顯示數學公式。

2. 通常是通過一對美元符號（`$`）來實現的。

<br>

## 範例

_當需要在 Markdown 中插入 LaTeX 語法以呈現數學公式時，通常會用下面的方式_

<br>

### 行內公式
   
1. 對於行內公式（inline formulas），使用單個美元符號包圍 LaTeX 語法，例如 `$E=mc^2$`。



2. 這裡是一個簡單的 Markdown 中嵌入 LaTeX 的示範，如果要在文本中插入一個數學表達式，如愛因斯坦的質能等價公式，可以這樣寫。
   
   ```markdown
   能量公式 $E=mc^2$ 計算，其中 $m$ 代表質量，$c$ 代表光速。
   ```

   這樣會在句子中直接顯示公式。

<br>

### 獨立公式

1. 對於展示模式公式（display formulas），使用兩個美元符號包圍 LaTeX 語法，例如 `$$E=mc^2$$`。

2. 這裡是展示如果想要讓公式獨立於文字並且居中顯示，可使用兩個美元符號實現，在支持 LaTeX 的 Markdown 渲染器中，這樣會讓 `E=mc^2` 這個公式單獨顯示在一行上。。

   ```markdown
   愛因斯坦的質能等價公式可以表示為：

   $$E=mc^2$$

   這裡，$m$ 代表質量，而 $c$ 是光速。
   ```

<br>

## 補充說明

1. 並不是所有的 Markdown 渲染器都支援 LaTeX。
2. 在不支援 LaTeX 的環境中，上述語法不會產生數學公式，而只是顯示原始的文字。
3. 如果正在使用如 Jupyter 或支援 LaTeX 的平台，上面的語法應該可以正常工作。


<br>

---

_END_