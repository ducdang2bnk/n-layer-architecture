from sqlalchemy.orm import Session
from app.models.product import Product

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Product).all()

    # def get(self, product_id: int):
    #     return self.db.query(Product).filter(Product.id == product_id).first()

    def get(self, product_id: int):
        return self.db.query(Product).filter(Product.id == product_id).with_entities(Product.name,
                                                                                     Product.description).first()

        return ProductResponse(name=result.name, price=result.description)


    def create(self, name: str, description: str):
        product = Product(name=name, description=description)
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product
