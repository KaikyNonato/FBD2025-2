from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

class ProductBase(BaseModel):
    nome: str
    descricao: Optional[str] = None
    preco: Decimal
    tipo_id: int
    fornecedor_id: int
    empresa_id: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True

# Schema de saída com nomes (DICA) 
class ProductOut(Product):
    tipo_nome: str
    fornecedor_nome: str