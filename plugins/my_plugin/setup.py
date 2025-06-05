# plugins/my_plugin/setup_plugin.py
from setuptools import setup, find_packages

setup(
    name="my_quantcrafter_plugin",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["quantcrafter"],
    entry_points={
        "quantcrafter": [
            "sma_advisor = my_plugin:register_advisors",
            "volatility_filter = my_plugin:register_filters"
        ]
    }
)
