# src/quantcrafter/utils/plugin_manager.py
import pluggy
from quantcrafter.core.plugin_spec import QuantCrafterPluginSpec


class PluginManager:
    def __init__(self):
        self.pm = pluggy.PluginManager("quantcrafter")
        self.pm.add_hookspecs(QuantCrafterPluginSpec)

    def load_plugins(self):
        # Загрузка через entry_points в setup.py
        self.pm.load_setuptools_entrypoints("quantcrafter")
        return self.pm
