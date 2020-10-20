#!/usr/bin/env bash

#
# Скрипт для запуска сервиса
#

msg() {
    echo "-> $@"
    "$@"
}

echo 'path: '$PWD

# Сервис который надо запустить
APP="src.ccxx.fastapi.main:app"

if [ "$1" == "dev" ]; then
#  указывать параметр --log-level debug бесполезно, он игнорируется если указан --log-config, все значения беруться из конфига
# --reload-dir src/ нужен обязательно (для докера) иначе начинается отслеживание в паке venv
# где некоторые файлы это симлинки за пределами доступности докера
  COMMAND="uvicorn --reload --reload-dir src/ --host 0.0.0.0 --port 8001 --log-config ./logger/conf.base.yaml $APP"
else
#  Прочие параметры в конфиге
  COMMAND="gunicorn -c config/gunicorn/conf.py $APP"
fi

msg $COMMAND
