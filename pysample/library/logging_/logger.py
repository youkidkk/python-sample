import logging

logging.basicConfig(level=logging.DEBUG)

# ロガーの取得
logger = logging.getLogger(__name__)
# ロガーのログレベルを設定
logger.setLevel(logging.INFO)
logger.error("Info...")  # -> ERROR:__main__:Info...
logger.debug("Debug...")  # -> 出力されない
