import logging

# ログフォーマットを指定
logging.basicConfig(format="[%(levelname)s]%(asctime)s : %(message)s")

logging.warning("Info log...")
