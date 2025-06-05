# setup.py
import os
from setuptools import setup, find_packages

def read_requirements(file_name: str) -> list:
    """Читает зависимости из файла requirements."""
    requirements = []
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    requirements.append(line)
    except FileNotFoundError:
        print(f"Файл {file_name} не найден. Продолжаю без него.")
    return requirements


# Чтение зависимостей
requirements = read_requirements("requirements.txt")
requirements_dev = read_requirements("requirements-dev.txt")

setup(
    name="quantcrafter",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=requirements,
    extras_require={
        "dev": requirements_dev,
    },
    entry_points={
        "console_scripts": [
            "qc=quantcrafter.cli.main:app",  # CLI интерфейс
        ],
        "quantcrafter.plugins": [
            # Здесь будут подключаться плагины
        ]
    },
    author="Sergey Chekh",
    description="QuantCrafter — система построения торговых алгоритмов на основе декларативных конфигураций",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/chekh/QuantCrafter", 
    python_requires=">=3.11",
)