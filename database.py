from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError


from config import config

SQLALCHEMY_DATABASE_URL = config.DATABASE_URL

# from config import settings
#
# engine = create_engine(settings.DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def check_connection():
    try:
        with engine.connect() as connection:
            print("Kết nối thành công đến cơ sở dữ liệu!")
    except SQLAlchemyError as e:
        print(f"Lỗi kết nối: {e}")
