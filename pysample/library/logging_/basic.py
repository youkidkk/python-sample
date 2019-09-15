import logging

# ログ出力レベルの設定 ※デフォルトはWARNING
logging.basicConfig(level=logging.INFO)

logging.critical("Critical!!!")
logging.error("Error!")
logging.warning("Warning.")
logging.info("Info...")
logging.debug("Debug......")
