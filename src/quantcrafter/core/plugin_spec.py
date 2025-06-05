# src/quantcrafter/core/plugin_spec.py
import pluggy

hookspec = pluggy.HookspecMarker("quantcrafter")


class QuantCrafterPluginSpec:
    @hookspec
    def register_advisors(self):
        """Возвращает словарь {name: class}, где class наследуется от Advisor"""
        pass

    @hookspec
    def register_filters(self):
        """Возвращает словарь {name: class}, где class наследуется от Filter"""
        pass

    @hookspec
    def register_data_providers(self):
        """Возвращает словарь {name: class}, где class наследуется от DataProvider"""
        pass

    @hookspec
    def register_execution_strategies(self):
        """Возвращает словарь {name: class}, где class наследуется от ExecutionLogic"""
        pass

    @hookspec
    def register_visualizers(self):
        """Возвращает словарь {name: class}, где class наследуется от Visualizer"""
        pass

    @hookspec
    def register_cli_commands(self):
        """Возвращает Typer-приложение или список подкоманд"""
        pass
