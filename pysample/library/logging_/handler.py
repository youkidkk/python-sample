import logging

logger = logging.getLogger()
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

# ファイルハンドラ -> ファイル出力
fileHandler = logging.FileHandler(filename="tmp/filehandler.log")
fileHandler.setFormatter(formatter)

# ストリームハンドラ -> コンソール出力
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(formatter)

# ハンドラをロガーに設定
logger.addHandler(fileHandler)
logger.addHandler(streamHandler)

logger.error("log!!!")
# -> ファイル、コンソールにログ出力
