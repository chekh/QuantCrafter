# plugins/my_plugin/advisors/sma_crossover.py
from quantcrafter.core.interfaces import Advisor
from quantcrafter.core.context import StrategyContext


class SMACrossoverAdvisor(Advisor):
    def generate_signals(self, context: StrategyContext):
        # Твоя логика
        return [{"type": "buy", "symbol": "BTC/USDT"}]
