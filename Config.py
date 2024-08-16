import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "JMTHON_ROBOT")
    SUPPORT = os.environ.get("SUPPORT", "JMTHON_SUPPORT")
    CHANNEL = os.environ.get("CHANNEL", "JMTHON")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/9e8cb8fcee7549cc063aa.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/57940a2cd0d617ff9e44a.jpg")

