from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class StockBase(BaseModel):
    produto_id: int
    quantidade: int

class StockCreate(StockBase):
    pass

class Stock(StockBase):
    id: int
    data_atualizacao: datetime

    class Config:
        from_attributes = True

class StockOut(Stock):
    produto_nome: str