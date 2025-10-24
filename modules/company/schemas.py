from pydantic import BaseModel
from typing import Literal

# Status permitido pela constraint do banco
StatusEnum = Literal['ATIVO', 'INATIVO', 'SUSPENSO']

class CompanyBase(BaseModel):
    name: str
    cnpj: str
    status: StatusEnum

class CompanyCreate(CompanyBase):
    pass

class Company(CompanyBase):
    id: int

    class Config:
        from_attributes = True 