import logging


# logging.Filter を継承する
class SampleFilter(logging.Filter):
    def filter(self, record):
        msg = record.getMessage()
        # ログメッセージが hoge で開始しない場合のみ出力する
        return not msg.startswith("hoge")


logger = logging.getLogger()
logger.addFilter(SampleFilter())


logger.error("hoge!!!")
# -> 出力されない

logger.error("fuga!!!")
logger.error("piyo!!!")
# -> 出力される
