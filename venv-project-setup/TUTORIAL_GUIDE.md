# Python Virtual Environments: `venv`, `pip`, and `uv`

A quick guide to creating and managing Python virtual environments, installing packages, and using `requirements.txt`.

[CLick here to watch the full tutorial on YouTube](https://youtube.com/playlist?list=PLVYouuCRZZgE&si=OYZdHKJc8mMkBi3O)

## 1. Creating a virtual environment using Python

Python includes the built-in `venv` module for creating isolated environments.

```bash
python -m venv .venv
```

This creates a virtual environment named `.venv` in the current directory.

> On some systems, you may need to use `python3` instead of `python`.

## 2. Activating the virtual environment

### Windows — Command Prompt

```cmd
.venv\Scripts\activate
```

### Windows — PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### macOS / Linux

```bash
source .venv/bin/activate
```

After activation, your shell usually shows `(.venv)` at the beginning of the prompt.

To leave the virtual environment:

```bash
deactivate
```

## 3. Adding packages using `pip`

With the virtual environment activated:

```bash
pip install requests
```

Install multiple packages:

```bash
pip install requests flask pandas
```

You can also install a specific version:

```bash
pip install requests==2.32.4
```

## 4. Removing packages using `pip`

Remove a package:

```bash
pip uninstall requests
```

To skip the confirmation prompt:

```bash
pip uninstall -y requests
```

## 5. `pip show` and `pip list`

### `pip show`

Displays information about a particular installed package:

```bash
pip show requests
```

This can show details such as the package version, installation location, dependencies, and project information.

### `pip list`

Shows packages currently installed in the active environment:

```bash
pip list
```

Example:

```text
Package    Version
---------- -------
pip        25.x
requests   2.x
```

## 6. Using `requirements.txt`

A `requirements.txt` file records the packages needed by a project.

### Create `requirements.txt`

You can export the packages installed in the current environment:

```bash
pip freeze > requirements.txt
```

The file may look like:

```text
requests==2.32.4
flask==3.1.1
```

### Install from `requirements.txt`

```bash
pip install -r requirements.txt
```

This is useful when setting up the same project on another machine or in CI/CD.

### Remove a package and update the file

```bash
pip uninstall requests
pip freeze > requirements.txt
```

> `pip freeze` records the installed environment, including transitive dependencies. For larger projects, dependency management tools can provide more control.

---

# Using `uv` instead of `pip`

[`uv`](https://docs.astral.sh/uv/) is a fast Python package and project manager. It can handle virtual environments and package installation, so you can use it instead of manually combining `venv` and `pip`.

Install `uv` using the method recommended for your operating system from the official documentation.

## 7. Creating a virtual environment with `uv`

```bash
uv venv
```

By default, this creates a `.venv` directory.

You can also choose a different directory:

```bash
uv venv myenv
```

## 8. Activating a `uv` virtual environment

`uv` creates a standard Python virtual environment, so activation works the same way as with `venv`.

### Windows — Command Prompt

```cmd
.venv\Scripts\activate
```

### Windows — PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### macOS / Linux

```bash
source .venv/bin/activate
```

Alternatively, you can use `uv` commands without activating the environment:

```bash
uv run python script.py
```

## 9. Adding packages with `uv`

Install a package into the virtual environment:

```bash
uv pip install requests
```

Install multiple packages:

```bash
uv pip install requests flask pandas
```

Install a specific version:

```bash
uv pip install requests==2.32.4
```

The `uv pip` interface is designed to be familiar to users of `pip`.

## 10. Removing packages with `uv`

```bash
uv pip uninstall requests
```

## 11. `uv pip show` and `uv pip list`

### Show package information

```bash
uv pip show requests
```

### List installed packages

```bash
uv pip list
```

These commands provide functionality similar to:

```bash
pip show requests
pip list
```

## 12. Using `requirements.txt` with `uv`

Install dependencies from a requirements file:

```bash
uv pip install -r requirements.txt
```

You can generate a requirements file from the current environment:

```bash
uv pip freeze > requirements.txt
```

Then another developer can install the same requirements with:

```bash
uv pip install -r requirements.txt
```

---

## Quick command comparison

| Task | Python + `pip` | `uv` |
|---|---|---|
| Create venv | `python -m venv .venv` | `uv venv` |
| Activate | `source .venv/bin/activate` | Same activation commands |
| Install package | `pip install requests` | `uv pip install requests` |
| Uninstall package | `pip uninstall requests` | `uv pip uninstall requests` |
| Show package | `pip show requests` | `uv pip show requests` |
| List packages | `pip list` | `uv pip list` |
| Install requirements | `pip install -r requirements.txt` | `uv pip install -r requirements.txt` |
| Export requirements | `pip freeze > requirements.txt` | `uv pip freeze > requirements.txt` |

## Recommended project setup

For a simple project using the traditional Python tools:

```bash
python -m venv .venv
source .venv/bin/activate       # macOS/Linux
pip install -r requirements.txt
```

Using `uv`:

```bash
uv venv
source .venv/bin/activate       # macOS/Linux
uv pip install -r requirements.txt
```

For new projects, `uv` can also manage the project itself, dependencies, and lockfile rather than using `requirements.txt` alone. However, `uv pip` is a convenient choice when you specifically want a `pip`-compatible workflow.

<p align="center">
  Crafted with ❤️ by <a href="https://github.com/yahyazoom17">Yahya</a>
</p>
