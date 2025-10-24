from modules.company.repository import CompanyRepository
from modules.company.schemas import CompanyCreate


class CompanyService:
    def __init__(self):
        self.repository = CompanyRepository()

    def get_companies(self):
        return self.repository.get_all()

    def get_company_id(self, id: int):
        return self.repository.get_id(id)

    def create_company(self, company: CompanyCreate):
        return self.repository.save(company)