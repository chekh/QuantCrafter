# src/quantcrafter/cli/commands/plugins.py
import typer
from loguru import logger

app = typer.Typer()


@app.command(name="list")
def list_plugins():
    """Показать список загруженных плагинов"""
    logger.info("Загрузка списка плагинов...")
    # Здесь можно вызвать plugin_manager и получить список
    logger.opt(colors=True).info("- advisor: <green>sma_crossover</green>")


@app.command(name="add")
def add_plugin(name: str):
    """Добавить новый плагин по имени"""
    logger.info(f"Добавляем плагин: {name}")
