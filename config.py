import os

class Config:
    # DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_USER = os.environ.get('DB_USER', 'bnk')
    DB_PASS = os.environ.get('DB_PASS', 'admin')
    DB_NAME = os.environ.get('DB_NAME', 'n_layer')

    DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

    PORT = int(os.getenv("PORT", 8002))  # Mặc định là 8000 nếu không có biến môi trường

config = Config()


# from pydantic_settings import BaseSettings
#
# class Settings(BaseSettings):
#     DATABASE_URL: str
#
#     class Config:
#         env_file = ".env"
#
# settings = Settings()