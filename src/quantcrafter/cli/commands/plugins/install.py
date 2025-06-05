
@app.command("install")
def install_plugin(package: str):
    """Установить плагин из PyPI или локального пути"""
    import subprocess
    import sys

    logger.info(f"Устанавливаю плагин: {package}")
    result = subprocess.run([sys.executable, "-m", "pip", "install", package], check=False)
    if result.returncode == 0:
        logger.success(f"Плагин '{package}' успешно установлен.")
    else:
        logger.error(f"Ошибка при установке плагина '{package}'.")