from pydantic import BaseModel
from typing import Literal

StatusEnum = Literal['ATIVO', 'INATIVO', 'SUSPENSO']

class SupplierBase(BaseModel):
    name: str
    cnpj: str
    status: StatusEnum
    company_id: int

class SupplierCreate(SupplierBase):
    pass

class Supplier(SupplierBase):
    id: int

    class Config:
        from_attributes = True