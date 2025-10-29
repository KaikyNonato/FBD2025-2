from core.db import DataBase
from modules.supplier.schemas import SupplierCreate
from fastapi import HTTPException, status

class SupplierRepository:
    QUERY_ALL = "SELECT * FROM supplier ORDER BY id;"
    QUERY_GET_ID = "SELECT * FROM supplier WHERE id = %s;"
    QUERY_CREATE = "INSERT INTO supplier (name, cnpj, status, company_id) VALUES (%s, %s, %s, %s) RETURNING *;"

    def get_all(self):
        try:
            with DataBase() as db:
                return db.execute(self.QUERY_ALL)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail=f"Erro ao buscar fornecedores")

    def get_id(self, id: int):
        try:
            with DataBase() as db:
                return db.execute(self.QUERY_GET_ID, (id,), many=False)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail=f"Erro ao encontrar fornecedor por id: {id}")
                                
    def save(self, supplier: SupplierCreate):
        with DataBase() as db:
            params = (supplier.name, supplier.cnpj, supplier.status, supplier.company_id)
            return db.commit(self.QUERY_CREATE, params)