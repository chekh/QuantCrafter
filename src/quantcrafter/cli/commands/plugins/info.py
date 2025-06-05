# src/quantcrafter/cli/commands/plugins/info.py
import typer
from loguru import logger
import pkg_resources


def info(
    name: str = typer.Argument(..., help="Имя установленного пакета"),
    verbose: bool = typer.Option(False, "--verbose", "-v")
):
    """Показать информацию о конкретном плагине"""
    try:
        dist = pkg_resources.get_distribution(name)
        logger.info(f"Имя: {dist.project_name}")
        logger.info(f"Версия: {dist.version}")
        logger.info(f"Локация: {dist.location}")
        logger.info("Зависимости:")
        for req in dist.requires():
            logger.opt(colors=True).info(f" - {req.project_name} >= {req.specs[0][1] if req.specs else ''}")

        if verbose:
            logger.info("Поддерживаемые модули:")
            eps = list(pkg_resources.iter_entry_points("quantcrafter"))
            for ep in eps:
                if ep.dist and ep.dist.project_name == name:
                    logger.opt(colors=True).info(f" - {ep.name}: {ep.module_name}")

    except pkg_resources.DistributionNotFound:
        logger.error(f"Плагин '{name}' не найден.")
