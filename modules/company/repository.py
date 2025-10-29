from fastapi import HTTPException, status
from core.db import DataBase
from modules.company.schemas import CompanyCreate


class CompanyRepository:
    QUERY_ALL = "SELECT * FROM company ORDER BY id;"
    QUERY_GET_ID = "SELECT * FROM company WHERE id = %s;"
    QUERY_CREATE = "INSERT INTO company (name, cnpj, status) VALUES (%s, %s, %s) RETURNING *;"

    def get_all(self):
        try:
            with DataBase() as db:
                return db.execute(self.QUERY_ALL)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail=f"Erro ao buscar empresas")

    def get_id(self, id: int):
        try:
            with DataBase() as db:
                return db.execute(self.QUERY_GET_ID, (id,), many=False)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail=f"Erro ao encontrar empresa por id: {id}")

    def save(self, company: CompanyCreate):
        try:
            with DataBase() as db:
                params = (company.name, company.cnpj, company.status)
                created_company = db.commit(self.QUERY_CREATE, params)
                if not created_company:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                        detail="Não foi possível criar a empresa.")
                return created_company
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail=f"Erro ao salvar empresa: {e}")