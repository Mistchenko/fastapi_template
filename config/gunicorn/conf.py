import os
import yaml


bind = "0.0.0.0:8001"
loglevel = os.getenv("LOG_LEVEL", "info")
workers = 6

# файлы для вывода логов указаны в conf.base.yaml (по умолчанию),
# при желании после загрузки `logconfig_dict` можно заменить на другие значения
# так же как меняется параметр `loglevel`
# errorlog = '_error.log'
# accesslog = '_access.log'

# Класс воркера Uvicorn`а вместо параметра `-k`
worker_class = 'uvicorn.workers.UvicornWorker'

file_config = './logger/conf.base.yaml'
# загружаем конфигурацию логера в словарь для гуникорна
# yaml хорош тем что поддерживается и ювикорном и гуникорном
# можно использовать одинаковый конфиг для обоих режимов запуска
# с другой стороны гуникорн позволяет заменить (после загрузки в словарь) некоторые параметры (средствами python)
with open(file_config, 'r') as f:
    logconfig_dict = yaml.safe_load(f.read())
    # Меняем дефолтовое значение на новый параметр
    logconfig_dict['root']['level'] = loglevel.upper()
