# src/quantcrafter/cli/commands/analytics.py
import typer
from loguru import logger

app = typer.Typer()


@app.command(name="report")
def generate_report(
    strategy_id: str = typer.Argument(...),
    output: str = typer.Option("report.html", "--output", "-o"),
):
    """Сгенерировать отчёт по стратегии"""
    logger.info(f"Генерация отчёта для {strategy_id} → {output}")
