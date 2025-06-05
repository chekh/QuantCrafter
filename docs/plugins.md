# 🧩 Создание плагинов для QuantCrafter

Этот документ описывает, как разрабатывать и регистрировать собственные модули (плагины) для проекта **QuantCrafter**, такие как советники (`Advisor`), фильтры (`Filter`) и CLI-команды.

> ✅ Поддерживается через `pluggy` и `entry_points`. Плагины можно устанавливать отдельно, без изменения основного кода библиотеки.

---

## 📁 Структура плагина

Пример структуры внешнего плагина:

```
my_quantcrafter_plugins/
├── setup.py
└── my_plugin/
    ├── __init__.py
    └── advisors/
        └── sma_crossover.py
```

---

## 🔧 Шаг 1: Создайте файл реализации

Создайте Python-модуль с вашей логикой. Пример: `sma_crossover.py`.

```python
# my_plugin/advisors/sma_crossover.py
from quantcrafter.core.interfaces import Advisor
from quantcrafter.core.context import StrategyContext


class SMACrossoverAdvisor(Advisor):
    def __init__(self, short_period=10, long_period=30):
        self.short_period = short_period
        self.long_period = long_period

    def generate_signals(self, context: StrategyContext):
        # Пример простой логики SMA crossover
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
```

---

## 📦 Шаг 2: Регистрация модуля

В файле `__init__.py` вашего пакета определите функцию регистрации.

```python
# my_plugin/__init__.py
from .advisors.sma_crossover import SMACrossoverAdvisor


def register_advisors():
    return {
        "sma_crossover": SMACrossoverAdvisor,
    }
```

Можно также добавить другие типы модулей:

- `register_filters()`
- `register_data_providers()`
- `register_execution_strategies()`
- `register_visualizers()`
- `register_cli_commands()` (для CLI)

---

## 🧪 Шаг 3: Объявите entry point в `setup.py`

```python
# setup.py
from setuptools import setup

setup(
    name="my_quantcrafter_plugins",
    version="0.1.0",
    packages=["my_plugin"],
    package_dir={"": "."},
    install_requires=["quantcrafter"],
    entry_points={
        "quantcrafter": [
            "sma_advisor = my_plugin:register_advisors"
        ]
    },
)
```

---

## 📦 Шаг 4: Установите плагин

Установите его в режиме разработки:

```bash
cd my_quantcrafter_plugins
pip install -e .
```

Теперь ваш плагин будет автоматически загружен в `QuantCrafter`.

---

## 🧪 Шаг 5: Проверьте установку

### В Python:

```python
from quantcrafter.utils.plugin_manager import PluginManager
from quantcrafter.modules.registry import ADVISOR_REGISTRY

pm = PluginManager().load_plugins()
print("Доступные советники:", list(ADVISOR_REGISTRY.keys()))
```

Вы должны увидеть: `'sma_crossover'`.

### Или через CLI (если реализован):

```bash
qc plugins list
```

---

## 🆕 Как добавить новые типы плагинов?

### Добавление нового типа, например `Filter`

#### 1. Реализуйте класс:

```python
# my_plugin/filters/volatility_filter.py
from quantcrafter.core.interfaces import Filter
from quantcrafter.core.context import StrategyContext


class VolatilityFilter(Filter):
    def __init__(self, threshold=0.05):
        self.threshold = threshold

    def apply(self, signals, context: StrategyContext):
        volatility = context.indicators.get("volatility", 0)
        if volatility > self.threshold:
            return []
        return signals
```

#### 2. Зарегистрируйте его:

```python
# my_plugin/__init__.py
from .filters.volatility_filter import VolatilityFilter


def register_filters():
    return {
        "volatility_filter": VolatilityFilter,
    }
```

#### 3. Добавьте в `setup.py`:

```python
entry_points={
    "quantcrafter": [
        "sma_advisor = my_plugin:register_advisors",
        "volatility_filter = my_plugin:register_filters"
    ]
}
```

---

## 📚 Поддерживаемые типы плагинов

| Тип | Метод регистрации | Назначение |
|-----|--------------------|------------|
| `Advisor` | `register_advisors()` | Генерация сигналов |
| `Filter` | `register_filters()` | Фильтрация сигналов |
| `DataProvider` | `register_data_providers()` | Источники данных |
| `ExecutionLogic` | `register_execution_strategies()` | Логика исполнения сделок |
| `Visualizer` | `register_visualizers()` | Визуализация |
| `CLI` | `register_cli_commands()` | Дополнительные команды CLI |

---

## ✅ Что дальше?

Теперь вы можете:

- Создавать свои модули и расширять систему.
- Делиться своими плагинами с другими пользователями.
- Интегрировать их в конфигурации YAML.
- Использовать в разных режимах: backtest, paper, live.

---

> 💡 Совет: Чтобы не дублировать логику, используйте шаблоны и общие абстракции из `quantcrafter.core.interfaces`.

---