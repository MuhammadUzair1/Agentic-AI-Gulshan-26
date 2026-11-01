# 📓 Jupyter Notebooks: A Beginner's Guide

From Class 6 onwards, some of our class code is in **Jupyter Notebook** files (`.ipynb`) instead of normal Python files (`.py`). This guide explains what notebooks are, when to use them, and the shortcuts that will make you fast.

---

## 🤔 What Is a Jupyter Notebook?

A notebook is a file made of small boxes called **cells**. You can write code in one cell, run **only that cell**, and see the result **right below it**.

It's like a notebook where you can write notes, run code, and see the answers on the same page.

```
┌──────────────────────────────────────┐
│ ## Dictionaries          ← Markdown  │   (notes / headings)
├──────────────────────────────────────┤
│ [1]  car = {'brand': 'toyota'}       │   ← Code cell
│      car                             │
│                                      │
│      {'brand': 'toyota'}             │   ← Output appears right here
└──────────────────────────────────────┘
```

---

## 🆚 `.py` File vs `.ipynb` Notebook

| | Python File (`.py`) | Jupyter Notebook (`.ipynb`) |
|---|---|---|
| **How it runs** | The whole file runs from top to bottom | Each cell runs on its own, one at a time |
| **Output** | Shown in the terminal | Shown under each cell |
| **Notes & headings** | Only `#` comments | Rich **Markdown** text, tables and images |
| **Best for** | Apps, scripts, projects, automation | Learning, experimenting, data analysis, AI/ML |
| **Shows a value without `print()`?** | ❌ No | ✅ Yes (the last line of a cell) |

---

## 🎯 Where Are Notebooks Used?

- **Learning & practice**: try one idea at a time and see results instantly
- **Data science & analysis**: explore data, draw charts, clean datasets
- **AI & machine learning**: test models and prompts step by step
- **Teaching & sharing**: code, explanation and output in one file
- **Prototyping**: test an idea quickly before turning it into a real `.py` program

> 💡 Professionals often **experiment in a notebook**, then **move the final code into `.py` files** for real projects.

---

## ⚙️ Setting Up Notebooks in VS Code

1. Open **VS Code** and go to **Extensions** (`Ctrl + Shift + X`).
2. Search for **Jupyter** and install the one by **Microsoft**.
3. Install the notebook engine (the **kernel**) by running this in the terminal:
   ```bash
   pip install ipykernel
   ```
4. Open any `.ipynb` file. Click **Select Kernel** in the top-right corner and choose your **Python** version.
5. Click a cell and press **Shift + Enter** to run it. 🎉

> 💡 VS Code may offer to install `ipykernel` for you the first time you run a cell. Just click **Install**.

### Other ways to use notebooks
| Option | How |
|---|---|
| **Google Colab** | Free, runs in the browser, nothing to install: [colab.research.google.com](https://colab.research.google.com) |
| **Jupyter in the browser** | `pip install notebook`, then run `jupyter notebook` in the terminal |

---

## 🧱 Cell Types

| Cell Type | Used For | How to create |
|---|---|---|
| **Code** | Python code you can run | `+ Code` button, or press `Y` in Command Mode |
| **Markdown** | Notes, headings, lists, tables | `+ Markdown` button, or press `M` in Command Mode |

### Quick Markdown cheat sheet
| You type | You get |
|---|---|
| `# Heading` | Big heading |
| `## Heading` | Smaller heading |
| `**bold**` | **bold** |
| `*italic*` | *italic* |
| `- item` | • bullet point |
| `` `code` `` | `code` |

---

## ⌨️ Keyboard Shortcuts

Notebooks have **two modes**:

| Mode | How to enter | What it's for | You'll see |
|---|---|---|---|
| ✏️ **Edit Mode** | Press `Enter` or click inside a cell | Typing code or text | A blinking cursor inside the cell |
| 🧭 **Command Mode** | Press `Esc` | Working with whole cells (add, delete, move) | The cell is highlighted, with no cursor |

### ▶️ Running cells (work in both modes)
| Shortcut | What it does |
|---|---|
| `Shift + Enter` | Run the cell and **move to the next** one ⭐ *(most used)* |
| `Ctrl + Enter` | Run the cell and **stay** on it |
| `Alt + Enter` | Run the cell and **insert a new cell below** |

### 🧭 Command Mode shortcuts (press `Esc` first)
| Shortcut | What it does |
|---|---|
| `A` | Add a new cell **above** |
| `B` | Add a new cell **below** |
| `D` `D` *(press D twice)* | **Delete** the cell |
| `Z` | **Undo** a deleted cell |
| `M` | Change the cell to **Markdown** |
| `Y` | Change the cell to **Code** |
| `↑` / `↓` or `K` / `J` | Move between cells |
| `L` | Show / hide **line numbers** |
| `Shift + ↑ / ↓` | Select several cells |
| `C` / `X` / `V` | Copy / Cut / Paste cells |

### ✏️ Edit Mode shortcuts
| Shortcut | What it does |
|---|---|
| `Ctrl + /` | Comment / uncomment the selected lines |
| `Ctrl + Z` | Undo typing |
| `Tab` | Auto-complete, or indent |
| `Ctrl + Space` | Show code suggestions |

> 💡 In VS Code, press `Ctrl + Shift + P` and type **"Notebook"** to see every notebook command and its shortcut.

---

## 🧠 Important Things to Know

### 1. The number next to a cell = run order
`[1]`, `[2]`, `[3]`... shows the **order** cells were run in, **not** their position on the page. An empty `[ ]` means the cell hasn't been run yet.

### 2. Variables live in memory between cells
If cell 1 creates `name = 'Ali'`, every other cell can use `name`, but **only after cell 1 has been run**.

```
NameError: name 'name' is not defined   ← You forgot to run the cell above!
```

### 3. Running cells out of order can confuse you
If you run cells in a random order or edit old cells, your results may not match what you see on the page.
**Fix:** Click **Restart** and then **Run All** to run everything fresh from top to bottom.

### 4. The last line shows automatically
```python
x = 10
x        # ← shows 10, no print() needed
```
Only the **last** line shows. Use `print()` if you want to see more than one value from the same cell.

### 5. Useful toolbar buttons (VS Code)
| Button | What it does |
|---|---|
| **▶▶ Run All** | Run every cell from top to bottom |
| **↻ Restart** | Clear all variables from memory and start fresh |
| **⏹ Interrupt** | Stop a cell that is taking too long or stuck in a loop |
| **Clear All Outputs** | Remove all outputs (useful before sharing) |
| **Variables** | See every variable in memory and its current value |
| **Outline** | Jump between headings in a long notebook |

---

## ✅ Good Habits

- 📝 Start each notebook with a **Markdown heading** that says what it's about.
- 🔢 Keep cells **small**, with one idea per cell.
- 🔁 Before sharing or submitting, do **Restart → Run All** to make sure everything works top to bottom.
- 💾 Save often with `Ctrl + S`.
- 📁 Use clear file names with no typos, like `dictionary_practice.ipynb`.

---

## 📂 Files in This Class

| Order | File | Topics |
|---|---|---|
| 1 | [dictionary recap.ipynb](dictionary%20recap.ipynb) | Nested dictionaries, keys/values/items, add/update/remove, copy vs deepcopy, renaming a key |
| 2 | [sets.py](sets.py) | Creating sets, removing duplicates, add(), pop(), remove() |
