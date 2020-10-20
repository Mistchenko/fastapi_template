import logging
from uuid import uuid1
from starlette.types import ASGIApp, Receive, Scope, Send


class LoggerMiddleware:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        old_factory = logging.getLogRecordFactory()

        def record_factory(*args, **kwargs):
            record = old_factory(*args, **kwargs)
            # Формируем (rid) уникальный идентификатор запроса
            record.unique_id = str(uuid1().hex)
            # Добавляем другие параметры для лога
            # record.custom_param = param_value
            return record

        logging.setLogRecordFactory(record_factory)
        logging.info('LoggerMiddleware')
        await self.app(scope, receive, send)
