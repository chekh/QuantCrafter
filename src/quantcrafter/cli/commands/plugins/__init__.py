# src/quantcrafter/cli/commands/plugins/__init__.py
import typer

from quantcrafter.cli.commands.plugins import list, info, create

app = typer.Typer(invoke_without_command=True)


@app.callback()
def plugins_callback():
    """
    Работа с плагинами.
    """


# Регистрация подкоманд
app.command(name="list")(list.list_plugins)
app.command(name="info")(info.info)
app.command(name="create")(create.create_plugin)
