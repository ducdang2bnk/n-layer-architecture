from fastapi import FastAPI
from app.controllers.product import router as product_router
from database import Base, engine, check_connection
import uvicorn
from config import config  # Import cấu hình

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(product_router)

# Kiểm tra kết nối đến cơ sở dữ liệu
check_connection()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Product API"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=config.PORT, reload=True)
