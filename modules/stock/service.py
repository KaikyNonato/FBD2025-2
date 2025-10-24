from modules.stock.repository import StockRepository
from modules.stock.schemas import StockCreate


class StockService:
    def __init__(self):
        self.repository = StockRepository()

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, id: int):
        return self.repository.get_id(id)

    def create(self, stock: StockCreate):
        return self.repository.save(stock)