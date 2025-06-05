# src/quantcrafter/core/orchestrator.py
from quantcrafter.utils.plugin_manager import PluginManager
from quantcrafter.modules.registry import (
    ADVISOR_REGISTRY,
    FILTER_REGISTRY,
    DATAPROVIDER_REGISTRY,
)


class StrategyOrchestrator:
    def __init__(self):
        self.plugin_manager = PluginManager().load_plugins()
        self._register_plugins()

    def _register_plugins(self):
        for hook in self.plugin_manager.hook.register_advisors():
            ADVISOR_REGISTRY.update(hook)

        for hook in self.plugin_manager.hook.register_filters():
            FILTER_REGISTRY.update(hook)

        for hook in self.plugin_manager.hook.register_data_providers():
            DATAPROVIDER_REGISTRY.update(hook)

        # Аналогично можно добавить execution, visualizer и т.д.
