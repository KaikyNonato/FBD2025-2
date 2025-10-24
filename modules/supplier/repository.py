from core.db import DataBase
from modules.supplier.schemas import SupplierCreate


class SupplierRepository:
    QUERY_ALL = "SELECT * FROM supplier ORDER BY id;"
    QUERY_GET_ID = "SELECT * FROM supplier WHERE id = %s;"
    QUERY_CREATE = "INSERT INTO supplier (name, cnpj, status, company_id) VALUES (%s, %s, %s, %s) RETURNING *;"

    def get_all(self):
        with DataBase() as db:
            return db.execute(self.QUERY_ALL)

    def get_id(self, id: int):
        with DataBase() as db:
            return db.execute(self.QUERY_GET_ID, (id,), many=False)

    def save(self, supplier: SupplierCreate):
        with DataBase() as db:
            params = (supplier.name, supplier.cnpj, supplier.status, supplier.company_id)
            return db.commit(self.QUERY_CREATE, params)