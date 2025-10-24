from modules.type_product.repository import TypeProductRepository
from modules.type_product.schemas import TypeProductCreate


class TypeProductService:
    def __init__(self):
        self.repository = TypeProductRepository()

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, id: int):
        return self.repository.get_id(id)

    def create(self, type_product: TypeProductCreate):
        return self.repository.save(type_product)