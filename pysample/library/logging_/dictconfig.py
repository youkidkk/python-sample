import logging
import logging.config
import json
import yaml

logging.config.dictConfig(yaml.load(open("config/logging.yaml").read()))
logger = logging.getLogger("sample")
logger.error("Yaml log!!!")

logging.config.dictConfig(json.loads(open("config/logging.json").read()))
logger = logging.getLogger("sample")
logger.error("Json log!!!")
