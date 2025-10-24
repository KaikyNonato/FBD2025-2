from typing import Optional, List
from fastapi import APIRouter, Depends
from modules.type_product import schemas
from modules.type_product.service import TypeProductService

router = APIRouter(prefix="/tipo", tags=["Type Product"])

def get_service():
    return TypeProductService()

@router.get("/", response_model=List[schemas.TypeProduct])
def list_types(service: TypeProductService = Depends(get_service)):
    """
    Retorna uma lista de tipos.
    """
    return service.get_all()

@router.get("/{id}/", response_model=Optional[schemas.TypeProduct])
def get_type_by_id(id: int, service: TypeProductService = Depends(get_service)):
    """
    Retorna um tipo pelo ID.
    """
    return service.get_by_id(id)

@router.post("/", response_model=schemas.TypeProduct, status_code=201)
def add_type(type_in: schemas.TypeProductCreate, service: TypeProductService = Depends(get_service)):
    """
    Adiciona um novo tipo.
    """
    return service.create(type_in)