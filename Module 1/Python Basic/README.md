# 🐍 Python Basics: Setup Guide

Before we write any code, we need two things on your computer:

1. **Python**: the language itself (the "engine" that runs your code)
2. **VS Code**: the code editor where you'll write your code

Follow the steps below in order. It takes about **10–15 minutes**.

---

## 📥 Part 1: Install Python

### Step 1: Download Python

1. Go to the official website: **[python.org/downloads](https://www.python.org/downloads/)**
2. Click the big yellow **Download Python 3.x.x** button. *(Any recent > 3.10 version is fine.)*

> ⚠️ Only download Python from **python.org**. Avoid third-party websites.

> 💡 **On Windows**, if python.org offers a **"Python install manager"** instead of a normal installer, scroll down and open the latest release, then under **Files** download the **Windows installer (64-bit)**. This guide follows that installer.

### Step 2: Run the Installer (Windows)

Open the downloaded file (e.g. `python-3.x.x-amd64.exe`). On the **very first screen**, **before** clicking anything else:

✅ Tick **"Use admin privileges when installing py.exe"**
✅ Tick **"Add python.exe to PATH"** ← ⚠️ **Most important step!**

```
┌──────────────────────────────────────────────────────┐
│  Install Python 3.x.x (64-bit)                       │
│                                                      │
│   ➜  Install Now                                     │
│      Customize installation                          │
│                                                      │
│   [✔] Use admin privileges when installing py.exe    │
│   [✔] Add python.exe to PATH          ◀── TICK THIS! │
└──────────────────────────────────────────────────────┘
```

Then click **Install Now**. If Windows asks *"Do you want to allow this app to make changes?"*, click **Yes**.

#### Why do these options matter?

| Option | What it does | If you skip it |
|---|---|---|
| **Add python.exe to PATH** | Lets you type `python` in any terminal and Windows knows where to find it | You'll get the error `'python' is not recognized...` |
| **Use admin privileges** | Installs the `py` launcher for **all users** on the computer, so it works everywhere | The launcher may not work for every account or terminal |

### Step 3: Finish the Installation

When you see **"Setup was successful"**:

- If you see **"Disable path length limit"**, click it (needs admin). This avoids errors with long file paths later.
- Click **Close**.

### Step 4: Check That Python Works ✅

1. Press the **Windows key**, type **`cmd`**, and open **Command Prompt**.
2. Type these commands one by one and press **Enter**:

   ```bash
   python --version
   pip --version
   ```

3. You should see something like:

   ```
   Python 3.x.x
   pip 2x.x from ...
   ```

🎉 If you see the version numbers, Python is installed correctly!

### 🍎 Using macOS or 🐧 Linux?

- **macOS:** Download the **macOS installer** from python.org and follow the steps. Then check with `python3 --version` in **Terminal**.
- **Linux:** Python is usually already installed. Check with `python3 --version`. If it's missing, install it with your package manager, e.g. `sudo apt install python3 python3-pip` on Ubuntu.

> On macOS and Linux, use `python3` and `pip3` instead of `python` and `pip`.

---

## 💻 Part 2: Install VS Code

### Step 1: Download VS Code

1. Go to **[code.visualstudio.com](https://code.visualstudio.com/)**
2. Click **Download for Windows** (it detects your system automatically).

### Step 2: Run the Installer

1. Open the downloaded file and **accept the agreement**.
2. Keep the default install location and click **Next**.
3. On the **"Select Additional Tasks"** screen, tick these boxes:

   ```
   [✔] Create a desktop icon
   [✔] Add "Open with Code" action to Windows Explorer file context menu
   [✔] Add "Open with Code" action to Windows Explorer directory context menu
   [✔] Register Code as an editor for supported file types
   [✔] Add to PATH (requires shell restart)        ◀── KEEP THIS TICKED
   ```

   > 💡 The **"Open with Code"** options let you right-click any folder and open it straight in VS Code, which is very handy!

4. Click **Next**, then **Install**, then **Finish**.

---

## ⚙️ Part 3: Set Up VS Code for Python

### Step 1: Install the Python Extension

1. Open **VS Code**.
2. Click the **Extensions** icon on the left sidebar (four squares), or press **`Ctrl + Shift + X`**.
3. Search for **`Python`**.
4. Install the one by **Microsoft** (it has a blue ✔ verified badge).

> This extension gives you code suggestions, error highlighting, and a ▶ **Run** button. It also installs **Pylance** and **Python Debugger** automatically.

### Step 2: Open Your Course Folder

1. Go to **File → Open Folder...**
2. Select your `Agentic-AI-Gulshan-26` folder and click **Select Folder**.
3. If VS Code asks *"Do you trust the authors of the files in this folder?"*, click **Yes, I trust the authors**.

### Step 3: Select the Python Interpreter

This tells VS Code which Python to use.

1. Press **`Ctrl + Shift + P`** to open the Command Palette.
2. Type **`Python: Select Interpreter`** and press **Enter**.
3. Choose the Python version you just installed (e.g. `Python 3.x.x 64-bit`).

### Step 4: Run Your First Python File 🚀

1. Create a new file called **`hello.py`** (the `.py` ending is important!).
2. Type this code:

   ```python
   print("Assalam Alaikum! My Python setup is working!")
   ```

3. Run it in **any one** of these ways:
   - Click the **▶ Run** button in the top-right corner, **or**
   - Right-click in the file → **Run Python File in Terminal**, **or**
   - Open the terminal with **`` Ctrl + ` ``** and type:
     ```bash
     python hello.py
     ```

4. You should see the message in the **Terminal** at the bottom. 🎉

---

## 🛠️ Troubleshooting

| Problem | Fix |
|---|---|
| `'python' is not recognized as an internal or external command` | You missed **"Add python.exe to PATH"**. Run the Python installer again → **Modify** → **Next** → tick **"Add Python to environment variables"** → **Install**. Then **close and reopen** your terminal and VS Code. |
| Typing `python` opens the **Microsoft Store** | Open Windows **Settings → Apps → Advanced app settings → App execution aliases**, and turn **OFF** both `python.exe` and `python3.exe`. |
| `python` doesn't work but Python is installed | Try `py --version` instead. The `py` launcher works even when PATH isn't set. |
| VS Code doesn't show your Python version | Restart VS Code, then repeat **Select Interpreter** (Part 3, Step 3). |
| The ▶ Run button doesn't appear | Make sure the file ends with **`.py`** and the **Python extension** by Microsoft is installed. |

> 🔁 **Golden rule:** After installing or changing anything, **close and reopen** your terminal and VS Code. Most "it's not working" problems are fixed by this!

---

## ✅ Setup Checklist

Before the next class, make sure you can tick all of these:

- [ ] `python --version` shows a version number
- [ ] `pip --version` shows a version number
- [ ] VS Code is installed
- [ ] The **Python extension** by Microsoft is installed in VS Code
- [ ] You ran `hello.py` and saw the output in the terminal

---

## 📂 Classes in This Section

| Class | Topics | File |
|---|---|---|
| Class 1 | print(), Comments, Variables, input(), Variable Naming Rules | [Class 1/intro.py](Class%201/intro.py) |

*(More classes will be added as the course progresses.)*
