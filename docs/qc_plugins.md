# 🧩 Работа с плагинами через CLI (`qc plugins`)

QuantCrafter поддерживает расширяемую архитектуру, где новые модули (советники, фильтры и т.д.) могут быть добавлены как **внешние плагины**, без изменения ядра библиотеки.

В этой инструкции ты узнаешь, как:

- Устанавливать плагины
- Просматривать список установленных плагинов
- Получать информацию о них

---

## 📦 1. Установка плагина

### Способ A: Установка внешнего плагина

Если плагин опубликован на PyPI или доступен через репозиторий:

```bash
pip install qc-my-plugin
```

или через Git:

```bash
pip install git+https://github.com/example/qc-my-plugin.git
```

### Способ B: Установка локального плагина

Если вы разрабатываете плагин локально, например в папке `plugins/my_plugin/`, и там есть `setup.py`:

```bash
cd plugins/my_plugin
pip install -e .
```

> Флаг `-e` позволяет редактировать код плагина без повторной установки.

---

## 🔍 2. Просмотр списка установленных плагинов

После установки используй команду:

```bash
qc plugins list
```

Пример вывода:

```
INFO     Ищу зарегистрированные плагины...
INFO     - sma_advisor: my_plugin:register_advisors
INFO     - volatility_filter: my_plugin:register_filters
```

Это показывает, какие плагины были найдены и какие типы модулей они предоставляют.

---

## ℹ️ 3. Информация о конкретном плагине

Чтобы узнать версию, зависимости и местоположение установленного плагина:

```bash
qc plugins info <plugin_name>
```

Пример:

```bash
qc plugins info my_quantcrafter_plugin
```

Пример вывода:

```
INFO     Имя: my_quantcrafter_plugin
INFO     Версия: 0.1.0
INFO     Локация: /home/user/quantcrafter/plugins/my_plugin
INFO     Зависимости:
INFO      - quantcrafter >= 
```

---

## ⚙️ 4. Добавление нового типа модуля

Ты можешь создать собственный плагин, который регистрирует:

- Советников (`Advisor`)
- Фильтры (`Filter`)
- Источники данных (`DataProvider`)
- Визуализаторы (`Visualizer`)
- CLI-команды

Для этого реализуй соответствующие функции в `__init__.py` плагина:

```python
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
```

И зарегистрируй их в `setup.py`:

```python
entry_points={
    "quantcrafter": [
        "sma_advisor = my_plugin:register_advisors",
        "volatility_filter = my_plugin:register_filters"
    ]
}
```

---

## 🧪 5. Проверка работы плагина в стратегии

После установки и регистрации плагина ты можешь использовать его в конфигурационном файле YAML:

```yaml
advisor:
  type: sma_crossover
  params:
    short_period: 10
    long_period: 30
```

Затем запусти стратегию:

```bash
qc run --config configs/my_strategy.yaml
```

---

## 🧹 6. Удаление плагина (опционально)

Если ты больше не нуждаешься в плагине:

```bash
pip uninstall <plugin_name>
```

Например:

```bash
pip uninstall my_quantcrafter_plugin
```

---

## ✅ Что дальше?

| Задача | Команда |
|--------|--------|
| Установить плагин | `pip install qc-my-plugin` |
| Установить локальный плагин | `cd plugins/my_plugin && pip install -e .` |
| Посмотреть список плагинов | `qc plugins list` |
| Получить информацию о плагине | `qc plugins info my_quantcrafter_plugin` |
| Удалить плагин | `pip uninstall my_quantcrafter_plugin` |

---