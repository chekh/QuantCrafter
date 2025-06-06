# QuantCrafter

---

## О проекте

**QuantCrafter** — модульная кросс-платформенная система для разработки, бэктестинга и исполнения алгоритмических торговых стратегий.  
Платформа построена на декларативном подходе, позволяющем собирать и конфигурировать торговые алгоритмы полностью через YAML-конфигурации без необходимости написания кода.

Ключевые особенности QuantCrafter:

- **Декларативное программирование стратегий** — полное описание логики через конфигурационные файлы для быстрой разработки и адаптации.  
- **Разделение бизнес-логики на два слоя**:  
  - *Советник (Advisor)* — генерация торговых сигналов на основе индикаторов и рыночных данных;  
  - *Исполнитель (Executor)* — контроль исполнения сигналов, управление рисками и мани-менеджмент.  
- **Единый универсальный контекст исполнения (StrategyContext)** — объект, доступный всем модулям для получения данных о состоянии рынка, портфеля и позиций.  
- **Гибкая модульная архитектура**, позволяющая легко добавлять новые индикаторы, фильтры, исполнителей и другие компоненты.  
- **Поддержка нескольких режимов работы** — исторический бэктестинг, реальное исполнение сделок через брокеров, песочница для безопасного тестирования.  
- **Мощные инструменты визуализации** — отображение индикаторов, сигналов, сделок, equity curve, рисков и статистики.

---

## About the project

**QuantCrafter** is a modular, cross-platform system for developing, backtesting, and executing algorithmic trading strategies.  
Built on a declarative approach, it allows assembling and configuring trading algorithms entirely through YAML files without writing code.

Key features of QuantCrafter:

- **Declarative strategy programming** — full logic described via configuration files for rapid development and iteration.  
- **Separation of business logic into two layers**:  
  - *Advisor* — generating trading signals based on indicators and market data;  
  - *Executor* — managing signal execution, risk control, and money management.  
- **Unified execution context (StrategyContext)** — accessible to all modules, providing market, portfolio, and position state.  
- **Flexible modular architecture** enabling easy extension with new indicators, filters, executors, and components.  
- **Support for multiple operation modes** — historical backtesting, live execution via brokers, and sandbox testing.  
- **Powerful visualization tools** — displaying indicators, signals, trades, equity curves, risks, and statistics.
