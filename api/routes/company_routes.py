from typing import Optional, List

from fastapi import APIRouter, Depends

from modules.company import schemas
from modules.company.schemas import CompanyCreate
from modules.company.service import CompanyService
from modules.product.schemas import ProductOut 
from modules.product.service import ProductService 


router = APIRouter(prefix="/company", tags=["Company"])


def get_company_service():
    return CompanyService()

def get_product_service():
    return ProductService()


@router.get("/", response_model=List[schemas.Company])
def list_companies(service: CompanyService = Depends(get_company_service)):
    """
    Retorna uma lista de empresas.
    """
    return service.get_companies()


@router.get("/{id}/", response_model=Optional[schemas.Company])
def get_company_by_id(id: int, service: CompanyService = Depends(get_company_service)):
    """
    Retorna uma empresa pelo ID.
    """
    return service.get_company_id(id)


@router.post("/", response_model=schemas.Company, status_code=201)
def add_company(company: CompanyCreate, service: CompanyService = Depends(get_company_service)):
    """
    Adiciona uma nova empresa.
    """
    return service.create_company(company)


@router.get("/{id}/produtos/", response_model=List[ProductOut], tags=["Product"])
def get_products_by_company(id: int, service: ProductService = Depends(get_product_service)):
    """
    Retorna os produtos de uma empresa pelo ID.
    """
    return service.get_products_by_company(id)