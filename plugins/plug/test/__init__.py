from .advisors.sma_crossover import SMACrossoverAdvisor


def register_advisors():
    return {
        "test_advisor": SMACrossoverAdvisor,
    }
