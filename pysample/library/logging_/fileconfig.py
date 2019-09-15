import logging
import logging.config

logging.config.fileConfig("config/logging.ini")
logger = logging.getLogger("sampleLoger")

logger.error("Logger Config!!!")
