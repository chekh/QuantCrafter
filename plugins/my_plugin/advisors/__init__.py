# plugins/my_plugin/__init__.py
from .advisors.sma_crossover import SMACrossoverAdvisor
from .filters.volatility_filter import VolatilityFilter


def register_advisors():
    return {
        "sma_crossover": SMACrossoverAdvisor,
    }


def register_filters():
    return {
        "volatility_filter": VolatilityFilter,
    }
