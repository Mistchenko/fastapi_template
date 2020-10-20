"""
ccxx.fastapi.main — стартовый модуль сервиса.
"""
import logging
from fastapi import FastAPI
from logger.middleware import LoggerMiddleware

app = FastAPI()
app.add_middleware(LoggerMiddleware)
logger = logging.getLogger(__name__)


@app.get("/")
async def hello():
    """
    Получить приветственное сообщение.
    """
    logger.info('Demo logger info')
    logger.debug('Demo logger DEBUG')
    message = f"Hello"
    return {"message": message}
