from quantcrafter.core.interfaces import Advisor
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
