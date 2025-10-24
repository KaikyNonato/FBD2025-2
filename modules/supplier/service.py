from modules.supplier.repository import SupplierRepository
from modules.supplier.schemas import SupplierCreate


class SupplierService:
    def __init__(self):
        self.repository = SupplierRepository()

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, id: int):
        return self.repository.get_id(id)

    def create(self, supplier: SupplierCreate):
        return self.repository.save(supplier)