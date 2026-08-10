# Python and Visual Studio Code Setup

This guide briefly explains how to install Python, install Visual Studio Code, and verify that both are working correctly.

## [Click here to watch the full tutorial on YouTube](https://youtube.com/playlist?list=PLVYouuCRZZgE&si=OYZdHKJc8mMkBi3O)

## 1. Install Python

1. Download Python from the official Python website:
   https://www.python.org/downloads/
2. Run the installer.
3. On Windows, **check “Add Python to PATH”** before selecting **Install Now**.
4. Complete the installation.

### Verify Python

Open a new terminal or Command Prompt and run:

```bash
python --version
```

If that command does not work on Windows, try:

```bash
py --version
```

You should see a Python version, for example:

```text
Python 3.x.x
```

You can also verify that `pip` is available:

```bash
python -m pip --version
```

## 2. Install Visual Studio Code

1. Download Visual Studio Code from:
   https://code.visualstudio.com/
2. Install it using the default options.
3. Open Visual Studio Code after installation.

## 3. Install the Python Extension

1. Open Visual Studio Code.
2. Select **Extensions** from the left sidebar.
3. Search for **Python**.
4. Install the **Python** extension published by Microsoft.

## 4. Verify Python in Visual Studio Code

1. Open a new folder in Visual Studio Code.
2. Create a file named `hello.py`.
3. Add:

```python
print("Python is working!")
```

4. Select the installed Python interpreter using **Python: Select Interpreter** from the Command Palette (`Ctrl+Shift+P` on Windows/Linux or `Cmd+Shift+P` on macOS).
5. Run the file using the **Run Python File** button or from the integrated terminal:

```bash
python hello.py
```

You should see:

```text
Python is working!
```

## Quick Verification Checklist

- [ ] `python --version` (or `py --version` on Windows) displays a Python version.
- [ ] `python -m pip --version` displays a pip version.
- [ ] Visual Studio Code opens successfully.
- [ ] The Microsoft Python extension is installed.
- [ ] VS Code detects the correct Python interpreter.
- [ ] `hello.py` runs successfully.

## Official Downloads

- Python: https://www.python.org/downloads/
- Visual Studio Code: https://code.visualstudio.com/
