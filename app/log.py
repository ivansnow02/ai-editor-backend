from logging.config import dictConfig
from colorlog import ColoredFormatter
from config import settings


def init_log():
    log_config = {
        "version": 1,
        "disable_existing_loggers": True,
        "formatters": {
            "sample": {"format": "%(asctime)s %(levelname)s %(message)s"},
            "verbose": {
                "()": "colorlog.ColoredFormatter",
                "format": "%(log_color)s%(levelname)-10s%(reset)s%(asctime)s %(name)s %(process)d %(thread)d %(message)s",
                "log_colors": {
                    "DEBUG": "cyan",
                    "INFO": "green",
                    "WARNING": "yellow",
                    "ERROR": "red",
                    "CRITICAL": "red,bg_white",
                },
            },
            "access": {
                "()": "uvicorn.logging.AccessFormatter",
                "fmt": '%(asctime)s %(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s',
            },
        },
        "handlers": {
            "console": {
                "formatter": "verbose",
                "level": "DEBUG",
                "class": "logging.StreamHandler",
            },
        },
        "loggers": {
            "": {"level": settings.LOG_LEVEL, "handlers": ["console"]},
        },
    }

    dictConfig(log_config)
