from typing import Optional, List
from fastapi import APIRouter, Depends
from modules.product import schemas
from modules.product.service import ProductService

router = APIRouter(prefix="/produto", tags=["Product"])

def get_service():
    return ProductService()

@router.get("/", response_model=List[schemas.ProductOut])
def list_products(service: ProductService = Depends(get_service)):
    """
    Retorna uma lista de produtos.
    """
    return service.get_all()

@router.get("/{id}/", response_model=Optional[schemas.ProductOut])
def get_product_by_id(id: int, service: ProductService = Depends(get_service)):
    """
    Retorna um produto pelo ID.
    """
    return service.get_by_id(id)

@router.post("/", response_model=schemas.ProductOut, status_code=201)
def add_product(product_in: schemas.ProductCreate, service: ProductService = Depends(get_service)):
    """
    Adiciona um novo produto.
    """
    
    return service.create(product_in)