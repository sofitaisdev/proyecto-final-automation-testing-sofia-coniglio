import logging
from pathlib import Path

LOG_DIR = Path(__file__).resolve().parent.parent / "reports"
LOG_FILE = LOG_DIR / "test_execution.log"


def get_logger(name):
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    LOG_DIR.mkdir(exist_ok=True)

    formato = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
    handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    handler.setFormatter(formato)
    logger.addHandler(handler)
    return logger
