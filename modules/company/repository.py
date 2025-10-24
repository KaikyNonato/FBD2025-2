from core.db import DataBase
from modules.company.schemas import CompanyCreate


class CompanyRepository:
    QUERY_ALL = "SELECT * FROM company ORDER BY id;"
    QUERY_GET_ID = "SELECT * FROM company WHERE id = %s;"
    QUERY_CREATE = "INSERT INTO company (name, cnpj, status) VALUES (%s, %s, %s) RETURNING *;"

    def get_all(self):
        with DataBase() as db:
            return db.execute(self.QUERY_ALL)

    def get_id(self, id: int):
        with DataBase() as db:
            return db.execute(self.QUERY_GET_ID, (id,), many=False)

    def save(self, company: CompanyCreate):
        with DataBase() as db:
            params = (company.name, company.cnpj, company.status)
            return db.commit(self.QUERY_CREATE, params)