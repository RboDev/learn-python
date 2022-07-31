# Shiny for Python

* https://shiny.rstudio.com/py/

<3 Shiny for R.

## Create venv

Upgrade regularly as still in Apha version

```
pip install --upgrade shiny htmltools
```

## Create an app

```
shiny create .
```

```
shiny run --reload
```

Nice, a VSCode extension !
https://marketplace.visualstudio.com/items?itemName=rstudio.pyshiny

* code snipets

  * `shinyapp` : template for app
  * `shinymodule` : template for module

The extension allows to start the app with the `run` button.  
> Does not work (looks like error on Windows with path as c:/ ?)

* setting.json 

About Pyright configuration (full list)
https://github.com/microsoft/pyright/blob/main/docs/configuration.md
Nice possible to set in the project (toml)

* Debugger 

same issue `c:\` cannot import `c`...


https://shiny.rstudio.com/py/docs/server.html