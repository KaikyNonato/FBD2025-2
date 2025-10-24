from typing import Optional, List
from fastapi import APIRouter, Depends
from modules.stock import schemas
from modules.stock.service import StockService

router = APIRouter(prefix="/estoque", tags=["Stock"])

def get_service():
    return StockService()

@router.get("/", response_model=List[schemas.StockOut])
def list_stock(service: StockService = Depends(get_service)):
    return service.get_all()

@router.get("/{id}/", response_model=Optional[schemas.StockOut])
def get_stock_by_id(id: int, service: StockService = Depends(get_service)):
    return service.get_by_id(id)

@router.post("/", response_model=schemas.StockOut, status_code=201)
def add_stock(stock_in: schemas.StockCreate, service: StockService = Depends(get_service)):
    return service.create(stock_in)