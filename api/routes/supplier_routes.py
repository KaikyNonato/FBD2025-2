from typing import Optional, List
from fastapi import APIRouter, Depends
from modules.supplier import schemas
from modules.supplier.service import SupplierService

router = APIRouter(prefix="/fornecedor", tags=["Supplier"])

def get_service():
    return SupplierService()

@router.get("/", response_model=List[schemas.Supplier])
def list_suppliers(service: SupplierService = Depends(get_service)):
    return service.get_all()

@router.get("/{id}/", response_model=Optional[schemas.Supplier])
def get_supplier_by_id(id: int, service: SupplierService = Depends(get_service)):
    return service.get_by_id(id)

@router.post("/", response_model=schemas.Supplier, status_code=201)
def add_supplier(supplier_in: schemas.SupplierCreate, service: SupplierService = Depends(get_service)):
    return service.create(supplier_in)