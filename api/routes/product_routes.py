from typing import Optional, List
from fastapi import APIRouter, Depends
from modules.product import schemas
from modules.product.service import ProductService
from modules.product.schemas import ProductOut 


router = APIRouter(prefix="/produto", tags=["Product"])

def get_service():
    return ProductService()

def get_product_service():
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

@router.get("/{id}/produtos/", response_model=List[ProductOut])
def get_products_by_company(id: int, service: ProductService = Depends(get_product_service)):
    """
    Retorna os produtos de uma empresa pelo ID.
    """
    return service.get_products_by_company(id)