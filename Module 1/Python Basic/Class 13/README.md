# 🧪 Class 13: Virtual Environments in Python

A **virtual environment** (often called a **venv**) is a private, separate copy of Python **for one project**, with its **own set of installed packages**.

> 🏠 **Think of it like this:** your computer is a big house, and every project gets its **own room**.
> Whatever you put in one room (packages) does **not** mess up the other rooms.

---

## 📑 Contents

1. [First, what is a package and pip?](#1--first-what-is-a-package-and-pip)
2. [The problem: why do we need virtual environments?](#2--the-problem-why-do-we-need-virtual-environments)
3. [How a virtual environment works](#3--how-a-virtual-environment-works)
4. [Step by step: create and use a virtual environment](#4--step-by-step-create-and-use-a-virtual-environment)
5. [Installing packages with pip](#5--installing-packages-with-pip)
6. [requirements.txt: share your project](#6--requirementstxt-share-your-project)
7. [Using a virtual environment in VS Code](#7--using-a-virtual-environment-in-vs-code)
8. [Don't upload `.venv` to GitHub (.gitignore)](#8--dont-upload-venv-to-github-gitignore)
9. [Troubleshooting](#9--troubleshooting)
10. [Cheat sheet](#10--cheat-sheet)
11. [Hands-on practice](#11--hands-on-practice)

---

## 1. 📦 First, What is a Package and pip?

- A **package** (or library) is code written by other people that you can install and use, so you don't have to write everything yourself.
  - `requests`: talk to websites and APIs
  - `pandas`: work with tables of data (like Excel)
  - `openai`, `anthropic`: build AI apps and agents 🤖
- **pip** is Python's **package installer**. It downloads packages from **[PyPI](https://pypi.org)** (the Python Package Index, the "Play Store" for Python packages).

```bash
pip install requests
```

In Class 11 we learned **modules**. Built-in modules like `math` and `json` come with Python. **Packages from pip have to be installed first.**

---

## 2. 🤔 The Problem: Why Do We Need Virtual Environments?

Without a virtual environment, `pip install` puts **every package into one global (shared) Python** on your computer. That causes problems:

### Problem 1: Version conflicts 💥

```
Your computer (ONE global Python)
│
├── Project A: an old chatbot   → needs  pandas 1.5
└── Project B: a new AI agent   → needs  pandas 2.2
```

Only **one** version of `pandas` can be installed globally at a time.
Upgrade it for Project B, and Project A **breaks**. Downgrade it for Project A, and Project B **breaks**. 😩

### Problem 2: "It works on my computer!" 🤷

You send your project to a friend, and it doesn't run on their computer, because you never wrote down **which** packages (and which versions) it needs.

### Problem 3: A messy global Python 🗑️

After a few months, your global Python has 100+ packages and you have no idea which project needs which one.

### ✅ The solution: one virtual environment per project

```
Your computer
│
├── Global Python (keep it clean!)
│
├── Project A/
│   └── .venv/   → pandas 1.5   ✅
│
└── Project B/
    └── .venv/   → pandas 2.2   ✅
```

Each project has its **own** packages with its **own** versions. No conflicts!

### Benefits at a glance

| Benefit | What it means |
|---|---|
| 🧱 **Isolation** | Packages of one project can't break another project |
| 🔢 **Different versions** | Project A and Project B can use different versions of the same package |
| 🤝 **Easy sharing** | A `requirements.txt` file lets anyone install the exact same packages |
| 🧹 **Clean computer** | Done with a project? Delete its `.venv` folder and everything is gone |
| 🔒 **No admin rights needed** | Packages are installed inside your project folder |
| 🏢 **Industry standard** | Every professional Python project uses one |

---

## 3. 🔧 How a Virtual Environment Works

When you create a venv, Python makes a **folder** (we'll call it `.venv`) inside your project:

```
my_project/
├── .venv/                  ← the virtual environment (Python makes this)
│   ├── Scripts/            ← Windows: python.exe, pip.exe, activate
│   │   (bin/ on macOS / Linux)
│   ├── Lib/site-packages/  ← packages you install go HERE
│   └── pyvenv.cfg          ← settings (which Python it was made from)
├── main.py                 ← YOUR code
└── requirements.txt        ← list of packages your project needs
```

**Activating** the venv simply tells your terminal:
> *"When I type `python` or `pip`, use the ones inside `.venv`, not the global ones."*

You can see it's active because the terminal shows the name in brackets:

```
(.venv) D:\my_project>
```

> 💡 The `.venv` folder is **not** your project code. It's just the "room" your code runs in. You can always delete it and create it again.

---

## 4. 🚀 Step by Step: Create and Use a Virtual Environment

### Step 1: Open your project folder in the terminal

In VS Code: **File → Open Folder...**, then open the terminal with **`` Ctrl + ` ``**.

### Step 2: Create the virtual environment

```bash
python -m venv .venv
```

| Part | Meaning |
|---|---|
| `python` | Use Python... |
| `-m venv` | ...to run its built-in module called `venv` |
| `.venv` | ...and name the new folder `.venv` |

> 📝 You can choose any name (`env`, `myenv`, `venv`), but **`.venv`** is the most common name and VS Code finds it automatically.
> You only create it **once per project**.

### Step 3: Activate it

The command depends on your operating system and terminal:

| System / Terminal | Command to activate |
|---|---|
| **Windows: Command Prompt (cmd)** | `.venv\Scripts\activate` |
| **Windows: PowerShell** *(VS Code default)* | `.venv\Scripts\Activate.ps1` |
| **Windows: Git Bash** | `source .venv/Scripts/activate` |
| **macOS / Linux** | `source .venv/bin/activate` |

✅ It worked if you see **`(.venv)`** at the start of the terminal line:

```
(.venv) PS D:\my_project>
```

> ⚠️ **PowerShell error: "running scripts is disabled on this system"?**
> Run this **once**, then try activating again:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

### Step 4: Check that it's working

```bash
python -c "import sys; print(sys.prefix)"
```

The path should end with **`.venv`**. You can also run the checker in this folder:

```bash
python "virtual envs.py"
```

### Step 5: Work on your project

Install packages and run your code as normal. Everything now happens **inside** the venv.

```bash
pip install requests
python main.py
```

### Step 6: Deactivate when you're done

```bash
deactivate
```

The `(.venv)` disappears and you're back to the global Python.

> 🔁 **Next time** you open the project, you **don't** create it again. Just **activate** it (Step 3).

### Deleting a virtual environment

Just delete the `.venv` folder. That's it! Your code is not affected.

```bash
# Windows (PowerShell)
Remove-Item -Recurse -Force .venv

# macOS / Linux
rm -rf .venv
```

---

## 5. 📥 Installing Packages with pip

Make sure the venv is **active** (you see `(.venv)`) before installing!

| Command | What it does |
|---|---|
| `pip install requests` | Install the latest version |
| `pip install requests==2.32.3` | Install an **exact** version |
| `pip install requests pandas` | Install several packages at once |
| `pip install --upgrade requests` | Upgrade to the newest version |
| `pip uninstall requests` | Remove a package |
| `pip list` | Show all installed packages |
| `pip show requests` | Show details about one package |
| `pip freeze` | Show packages in `name==version` format |
| `python -m pip install --upgrade pip` | Upgrade pip itself |

### Example: using an installed package

```python
# main.py
import requests

response = requests.get('https://api.github.com')
print('Status code:', response.status_code)    # 200 means OK
```

> 💡 If you get `ModuleNotFoundError: No module named 'requests'`, the package is not installed **in the Python that is running your file**. Check that the venv is active and VS Code is using it (see [Section 7](#7--using-a-virtual-environment-in-vs-code)).

---

## 6. 📋 requirements.txt: Share Your Project

`requirements.txt` is a simple text file that lists all the packages your project needs.

### Save your packages to the file

```bash
pip freeze > requirements.txt
```

The file will look like this:

```
certifi==2025.8.3
charset-normalizer==3.4.3
idna==3.10
requests==2.32.5
urllib3==2.5.0
```

*(Your exact version numbers may be different. `requests` needs a few helper packages, so pip installed those too.)*

### Install everything from the file (on another computer)

```bash
python -m venv .venv
.venv\Scripts\activate              # or the command for your system
pip install -r requirements.txt
```

🎉 Now your friend has **exactly** the same packages and versions as you.

> 🔄 Every time you install a new package, run `pip freeze > requirements.txt` again to keep the file up to date.

---

## 7. 💻 Using a Virtual Environment in VS Code

VS Code needs to know **which Python** to use when you click ▶ Run.

1. Press **`Ctrl + Shift + P`**.
2. Type **`Python: Select Interpreter`** and press **Enter**.
3. Choose the one that shows **`('.venv': venv)`**, e.g. `Python 3.x.x ('.venv': venv) .\.venv\Scripts\python.exe`.

After this:
- The **bottom-right corner** of VS Code shows the selected Python with `.venv`.
- New terminals you open in VS Code **activate the venv automatically**.

> 💡 **Shortcut:** you can also create a venv from VS Code: `Ctrl + Shift + P` → **`Python: Create Environment`** → **Venv** → choose your Python version.

> 📓 **Jupyter notebooks:** run `pip install ipykernel` inside the venv, then pick `.venv` from **Select Kernel** in the top-right of the notebook.

---

## 8. 🙈 Don't Upload `.venv` to GitHub (.gitignore)

The `.venv` folder can be **hundreds of MB** and only works on **your** computer. Never commit it to Git.

Create a file called **`.gitignore`** in your project folder and add:

```
.venv/
__pycache__/
```

✅ Upload your **code** and **`requirements.txt`**.
❌ Don't upload `.venv`. Anyone can rebuild it with `pip install -r requirements.txt`.

---

## 9. 🆘 Troubleshooting

| Problem | Fix |
|---|---|
| `running scripts is disabled on this system` (PowerShell) | Run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` once, or use **Command Prompt** instead. |
| `'python' is not recognized...` | Python isn't on PATH. See the Troubleshooting section of the [main setup guide](../README.md). On Windows you can also try `py -m venv .venv`. |
| `ModuleNotFoundError: No module named '...'` | The venv isn't active, or VS Code is using a different Python. Activate it and re-select the interpreter (Section 7). |
| I installed a package but it's missing in my project | You installed it **before** activating the venv, so it went into the global Python. Activate first, then install again. |
| No `(.venv)` in the terminal | You haven't activated it, or you're in the wrong folder. Use `cd` to go to the project folder, then activate. |
| I moved or renamed my project folder and the venv stopped working | Venvs can't be moved. Delete `.venv`, create it again, and run `pip install -r requirements.txt`. |
| On macOS / Linux `python` doesn't work | Use `python3 -m venv .venv`. After activating, `python` works. |

---

## 10. 📝 Cheat Sheet

| Task | Windows | macOS / Linux |
|---|---|---|
| Create | `python -m venv .venv` | `python3 -m venv .venv` |
| Activate (cmd) | `.venv\Scripts\activate` | n/a |
| Activate (PowerShell) | `.venv\Scripts\Activate.ps1` | n/a |
| Activate (bash / zsh) | `source .venv/Scripts/activate` | `source .venv/bin/activate` |
| Install a package | `pip install <name>` | `pip install <name>` |
| Save requirements | `pip freeze > requirements.txt` | `pip freeze > requirements.txt` |
| Install requirements | `pip install -r requirements.txt` | `pip install -r requirements.txt` |
| Deactivate | `deactivate` | `deactivate` |
| Delete | delete the `.venv` folder | `rm -rf .venv` |

### 🔁 The everyday workflow

```
New project:     create  →  activate  →  pip install ...  →  pip freeze > requirements.txt
Coming back:     activate  →  code  →  deactivate
Cloned project:  create  →  activate  →  pip install -r requirements.txt
```

> 🚀 **Going further:** you may hear about **`uv`**, a newer and much faster tool that creates virtual environments and installs packages (`uv venv`, `uv pip install ...`). The ideas are exactly the same as what you learned here.

---

## 11. 🎯 Hands-on Practice

Do this in your own practice folder (for example, on your Desktop):

1. Create a folder called `venv_practice` and open it in VS Code.
2. Copy [`virtual envs.py`](virtual%20envs.py) into it.
3. Run it **without** a venv:
   ```bash
   python "virtual envs.py"
   ```
   👉 It says **NO**, you're using the global Python.
4. Create and activate a venv:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
5. Run it again. 👉 Now it says **YES**, and only `pip` is installed.
6. Install a package and run it again:
   ```bash
   pip install requests
   python "virtual envs.py"
   ```
   👉 `requests` now appears in the list!
7. Save your requirements and look inside the file:
   ```bash
   pip freeze > requirements.txt
   ```
8. Type `deactivate`, run the file one last time and notice `requests` is **gone**, because it was only installed inside the venv. 🎉

---

## 📂 Files in This Class

| File | What's inside |
|---|---|
| [file handling.py](file%20handling.py) | Reading, writing, appending, creating and deleting files; `with`; file modes; `os` module; JSON files |
| [virtual envs.py](virtual%20envs.py) | A checker that shows which Python is running, whether a venv is active, and which packages are installed |
| [sample.txt](sample.txt) | A 10-line text file used for the **reading** examples |
| [sample1.txt](sample1.txt) | The file that `file handling.py` **writes** to |
