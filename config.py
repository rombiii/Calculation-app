import os

class Config:
    DB_NAME = os.getenv("DB_NAME")




config = Config()