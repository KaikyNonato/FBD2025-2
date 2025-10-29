from core.db import DataBase
from modules.type_product.schemas import TypeProductCreate
from fastapi import HTTPException, status

class TypeProductRepository:
    QUERY_ALL = "SELECT * FROM type_product ORDER BY id;"
    QUERY_GET_ID = "SELECT * FROM type_product WHERE id = %s;"
    QUERY_CREATE = "INSERT INTO type_product (name, cod, company_id) VALUES (%s, %s, %s) RETURNING *;"

    def get_all(self):
        try:
            with DataBase() as db:
                return db.execute(self.QUERY_ALL)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail=f"Erro ao buscar tipos de produto")
                                

    def get_id(self, id: int):
        try:
            with DataBase() as db:
                return db.execute(self.QUERY_GET_ID, (id,), many=False)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail=f"Erro ao encontrar tipo de produto por id: {id}")

    def save(self, type_product: TypeProductCreate):
        with DataBase() as db:
            params = (type_product.name, type_product.cod, type_product.company_id)
            return db.commit(self.QUERY_CREATE, params)