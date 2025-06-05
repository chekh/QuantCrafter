# src/quantcrafter/cli/main.py
import typer
from loguru import logger
import sys

# Настройка логгера
logger.remove()
logger.add(sys.stderr, level="INFO", colorize=True)

app = typer.Typer()


@app.callback(invoke_without_command=True)
def callback(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        typer.echo("Доступные команды: run, validate, plugins")
    else:
        logger.info(f"Запуск команды: {ctx.invoked_subcommand}")

# Подключаем подкоманды
from quantcrafter.cli.commands.run import app as run_app
# from quantcrafter.cli.commands.validate import app as validate_app
from quantcrafter.cli.commands.plugins import app as plugins_app

app.add_typer(run_app, name="run", help="Запустить торговую стратегию")
# app.add_typer(validate_app, name="validate", help="Проверить конфигурацию")
app.add_typer(plugins_app, name="plugins", help="Работа с плагинами")

if __name__ == "__main__":
    app()
