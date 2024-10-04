from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from app.repositories.product import ProductRepository
from app.services.product import ProductService

router = APIRouter()

@router.get("/products/")
def get_products(db: Session = Depends(get_db)):
    repository = ProductRepository(db)
    service = ProductService(repository)
    return service.get_all_products()

@router.get("/products/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    repository = ProductRepository(db)
    service = ProductService(repository)
    product = service.get_product(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/products/")
def create_product(name: str, description: str, db: Session = Depends(get_db)):
    repository = ProductRepository(db)
    service = ProductService(repository)
    return service.create_product(name, description)
