import os

class Config(object):
                API_ID = int(os.environ.get("APP_ID", "32206364"))
    API_HASH = os.environ.get("API_HASH", "c4ea0475a4e15f979cc4c646e754e8ae")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8528154803:AAGxkLqS_8hZ79tFahI70R1cyuzdMXFp8gk")
    STRING_SESSION = os.environ.get("STRING_SESSION", "AgHrbhwAPtVI1_-iZmMkZQUbDeyWtOvnibHYdqrIqRpvZNeZKdwGH8qKnwvkHdr9ECqjmDk9gF9uIcj7qKoB2xgR2MQembhZ6zhE1TuXLvj4_PhegreBu_wF5EcsP0pXfW1XmCnvCVfNjzuA8sSFqEaJ53Hl7EwGqRgp4ZQub-YQHXfg9SJcwohhDbRCESPldWHaQ4lSAL4S_KzbpjMHPXDq7eInDTTB46HRIHVbf953voUv55B9mn5u5Ie1fqeogtO1UX4WID-Bm3ItZZkk0irLeOWvYjmdP1z2hDMMu2BKykGyqi-hM-NwcDaNXOSfYRqY9KYEISTZ073E3lVWp_K-Cr7TZQAAAAHvlYtJAA")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "JMTHON_ROBOT")
    SUPPORT = os.environ.get("SUPPORT", "JMTHON_SUPPORT")
    CHANNEL = os.environ.get("CHANNEL", "JMTHON")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/9e8cb8fcee7549cc063aa.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/57940a2cd0d617ff9e44a.jpg")

