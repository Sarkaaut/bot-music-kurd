import os

class Config(object):
                API_ID = int(os.environ.get("APP_ID", "32206364"))
    API_HASH = os.environ.get("API_HASH", "c4ea0475a4e15f979cc4c646e754e8ae")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8528154803:AAGxkLqS_8hZ79tFahI70R1cyuzdMXFp8gk")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1ApWapzMBuxvBruhNA_Sizsp-FpVInOpVfK5tUhi2F7LOWhVtFxFrLkoMuGZl3LBdsH1hwO8rZKrfXPgoXlWPFcdoSlRzVtJBF0_UF6riK9rBeRpNhP13A-Wix3YgJ-dd5wK_82FDDi14tMuUWX6TEv8Sjvq2NTy9OK34MyUy-F_IMnwtsUsJNImJDVCF8Ckon76-ozvEeSj4E3KXKudUPNq-_fVBXb9YE0FFZYmBWGoXfgo4g0T_qvdsAJ11iKv_AUd6p_xLmcYZqT-0_Yd2Z1g2Vkju0pEgiUr5gR-RSaoA9dCSdq1XobuGZ-cSLFm_yD9S0YvTN9WJ075lW9eP2jGrBl3lAQQ=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "JMTHON_ROBOT")
    SUPPORT = os.environ.get("SUPPORT", "JMTHON_SUPPORT")
    CHANNEL = os.environ.get("CHANNEL", "JMTHON")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/9e8cb8fcee7549cc063aa.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/57940a2cd0d617ff9e44a.jpg")

