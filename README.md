# python-packages

Minimalist Python Packages to solve the `import` issues and forget PYTHONPATH or `sys.path` tweaks.

The package is used for development

## Clone this repos 

CD in your directory for repos.

```
git clone https://github.com/RboDev/python-packages.git
```

Or just use the green CODE button to copy the URL, open VS Code and git clone from the palette. (CTRL-Shift-P)


## Create a virtual environment

```
py -3 -m pip install --upgrade pip
```

- Optional but always a good practice to start any new project.
- if shared by multiples projects the virtual env can be created in the user profile  
(detected by VSCode)
- or used to create it inside the workspace in `.venv` for example.  
The `.` in prefix will put the file at the top of the dir and grey it out in VS Code.  
Do not forget to exclude it in `.gitignore` (by default for repos created with Github)  

```
py -3 -m venv .venv
```

## Install the package in development mode

After activating the virtual environment (usually detected automatically by VS Code)
_(had an issue with poweshell needed to execute `Set-ExecutionPolicy RemoteSigned`)_

```
pip install -e .
```

With the package installed in dev mode, a symbolic link is created in the `site-packages`.
So for Python our package looks like a normal package and end of the `import` issues.

Check the package installation with `pip list`

```
(.venv) PS D:\repos\python-packages> pip list
Package    Version Location
---------- ------- ------------------------------
example    0.0.1   d:\_github\python-packages\src
pip        21.1.1
setuptools 56.0.0
```

## Import in the script

Open the Python interpreter in the console (Ipython or ptpython to get autocomplete can help).

Here we import the function `add_one()` from the pkg.helper module.

```
>>> from pkg.helper import add_one  
>>> add_one(1)
2
```

In fact we have a namespace package here, it's possible to create other directories 
side by side with /pkg and get access.

To be continued...


## References

- https://packaging.python.org/tutorials/packaging-projects/

