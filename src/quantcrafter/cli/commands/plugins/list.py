# src/quantcrafter/cli/commands/plugins/list.py
import typer
from loguru import logger
import pkg_resources


def list_plugins():
    """Показать список зарегистрированных плагинов"""
    logger.info("Ищу зарегистрированные плагины...")

    eps = list(pkg_resources.iter_entry_points("quantcrafter"))
    plugins = set(ep.dist.project_name for ep in eps)

    if not plugins:
        logger.warning("Нет зарегистрированных плагинов.")
        return

    for plugin in sorted(plugins):
        logger.opt(colors=True).info(f"- <green>{plugin}</green>")
