# src/quantcrafter/cli/commands/plugins/create.py
import typer
from loguru import logger
from pathlib import Path
import os


def create_plugin(
    plugin_name: str = typer.Argument(..., help="Имя нового плагина"),
    output_dir: Path = typer.Option("plugins", "--dir", "-d", help="Папка для сохранения плагина"),
):
    """Создать шаблон нового плагина"""
    plugin_path = output_dir / plugin_name

    if plugin_path.exists():
        logger.error(f"Плагин '{plugin_name}' уже существует.")
        raise typer.Exit(code=1)

    logger.info(f"Создаю новый плагин: {plugin_name}")
    plugin_path.mkdir(parents=True, exist_ok=True)
    (plugin_path / "advisors").mkdir(exist_ok=True, parents=True)

    _create_setup_py(plugin_path, plugin_name)
    _create_init_py(plugin_path, plugin_name)
    _create_advisor_example(plugin_path, plugin_name)

    logger.success(f"Плагин '{plugin_name}' успешно создан в {plugin_path}")
    logger.info("Установите его с помощью: pip install -e .")


def _create_setup_py(plugin_path: Path, plugin_name: str):
    content = f"""from setuptools import setup, find_packages

setup(
    name="{plugin_name}",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["quantcrafter"],
    entry_points={{
        "quantcrafter": [
            "{plugin_name.replace('_', '-')}_advisor = {plugin_name}:register_advisors"
        ]
    }},
)
"""
    with open(plugin_path / "setup.py", "w") as f:
        f.write(content)


def _create_init_py(plugin_path: Path, plugin_name: str):
    content = f"""from .advisors.sma_crossover import SMACrossoverAdvisor


def register_advisors():
    return {{
        "{plugin_name.replace('_', '-')}_advisor": SMACrossoverAdvisor,
    }}
"""
    with open(plugin_path / "__init__.py", "w") as f:
        f.write(content)


def _create_advisor_example(plugin_path: Path, plugin_name: str):
    content = '''from quantcrafter.core.interfaces import Advisor
from quantcrafter.core.context import StrategyContext


class SMACrossoverAdvisor(Advisor):
    def __init__(self, short_period=10, long_period=30):
        self.short_period = short_period
        self.long_period = long_period

    def generate_signals(self, context: StrategyContext):
        close_prices = context.market_data.get("close")
        if not close_prices or len(close_prices) < self.long_period:
            return []

        sma_short = sum(close_prices[-self.short_period:]) / self.short_period
        sma_long = sum(close_prices[-self.long_period:]) / self.long_period

        if sma_short > sma_long:
            return [{"type": "buy", "symbol": "BTC/USDT"}]
        elif sma_short < sma_long:
            return [{"type": "sell", "symbol": "BTC/USDT"}]
        else:
            return []
'''
    with open(plugin_path / "advisors" / "sma_crossover.py", "w") as f:
        f.write(content)