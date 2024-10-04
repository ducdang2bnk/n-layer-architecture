from app.repositories.product import ProductRepository

class ProductService:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def get_all_products(self):
        return self.repository.get_all()

    def get_product(self, product_id: int):
        return self.repository.get(product_id)

    def create_product(self, name: str, description: str):
        return self.repository.create(name, description)
