from pydantic import BaseModel

class TypeProductBase(BaseModel):
    name: str
    cod: str
    company_id: int

class TypeProductCreate(TypeProductBase):
    pass

class TypeProduct(TypeProductBase):
    id: int

    class Config:
        from_attributes = True