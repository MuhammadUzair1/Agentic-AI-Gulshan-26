r"""
================================================================
 Module 1 - Python Basics | Class 13 (Part 2): Virtual Environments
================================================================

Read README.md in this folder FIRST - it explains what a virtual
environment is, why we need it, and every command step by step.

This file is a small CHECKER. Run it twice to SEE the difference:

    1. BEFORE activating a virtual environment:
           python "virtual envs.py"

    2. AFTER creating and activating one:
           python -m venv .venv
           .venv\Scripts\activate            (Windows)
           source .venv/bin/activate         (macOS / Linux)
           pip install requests
           python "virtual envs.py"

Compare the two outputs: the Python location and the installed
packages will be different!
"""

import sys
import os
from importlib import metadata


# ==============================================================
# 1. WHICH PYTHON IS RUNNING THIS FILE?
# ==============================================================
# sys.executable -> the full path of the python.exe running this code
print('Python version :', sys.version.split()[0])
print('Python location:', sys.executable)
print()


# ==============================================================
# 2. ARE WE INSIDE A VIRTUAL ENVIRONMENT?
# ==============================================================
# sys.prefix      -> the folder of the CURRENT environment
# sys.base_prefix -> the folder of the MAIN (system) Python
# Inside a venv these two are DIFFERENT.

in_venv = sys.prefix != sys.base_prefix

if in_venv:
    print('YES - you are inside a virtual environment')
    print('Environment folder:', sys.prefix)
else:
    print('NO - you are using the main (global) Python')
    print('Tip: create one with  python -m venv .venv')

# When a venv is activated, the terminal also sets this variable:
print('VIRTUAL_ENV variable:', os.environ.get('VIRTUAL_ENV', 'not set'))
print()


# ==============================================================
# 3. WHICH PACKAGES ARE INSTALLED HERE?
# ==============================================================
# A brand-new venv has only 'pip'. The global Python may have many.
packages = sorted(
    (dist.metadata['Name'], dist.version) for dist in metadata.distributions()
)

print('Installed packages:', len(packages))
for name, version in packages:
    print(f'   {name}=={version}')
print()


# ==============================================================
# 4. TRY USING AN EXTERNAL PACKAGE
# ==============================================================
# 'requests' is NOT built in. It only works where it is installed.
try:
    import requests
    print('requests is installed, version', requests.__version__)
except ModuleNotFoundError:
    print("requests is NOT installed in this environment.")
    print("Install it with:  pip install requests")
