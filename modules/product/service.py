from modules.product.repository import ProductRepository
from modules.product.schemas import ProductCreate


class ProductService:
    def __init__(self):
        self.repository = ProductRepository()

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, id: int):
        return self.repository.get_id(id)

    def get_products_by_company(self, company_id: int):
        return self.repository.get_by_company_id(company_id)

    def create(self, product: ProductCreate):
        return self.repository.save(product)