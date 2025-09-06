import os

class Settings:
    APP_NAME = "url-shortener"
    BASE_URL = os.getenv("BASE_URL", "http://localhost")
    DDB_TABLE = os.getenv("DDB_TABLE", "urls")
    CODE_LENGTH = int(os.getenv("CODE_LENGTH", "7"))
    RATE_LIMIT_PER_MIN = int(os.getenv("RATE_LIMIT_PER_MIN", "60"))
settings = Settings()
