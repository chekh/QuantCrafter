# src/quantcrafter/cli/commands/run.py
import typer
from loguru import logger

app = typer.Typer()


@app.command(name="strategy")
def run_strategy(
    config: str = typer.Option(..., "--config", "-c"),
    dry_run: bool = typer.Option(False, "--dry-run"),
):
    """Запустить торговую стратегию"""
    logger.info(f"Запуск стратегии из {config}, dry_run={dry_run}")
