from core.db import DataBase
from modules.stock.schemas import StockCreate
from fastapi import HTTPException, status

class StockRepository:
    
    QUERY_BASE = """
        SELECT  e.*,  p.nome as produto_nome FROM estoque e
        JOIN product p ON e.produto_id = p.id
    """
    
    QUERY_ALL = f"{QUERY_BASE} ORDER BY e.id"
    QUERY_GET_ID = f"{QUERY_BASE} WHERE e.id = %s"
    
  
    QUERY_CREATE = """
        INSERT INTO estoque (produto_id, quantidade, data_atualizacao) 
        VALUES (%s, %s, NOW()) 
        RETURNING id, produto_id, quantidade, data_atualizacao;
    """
    
    QUERY_GET_CREATED = f"""
        SELECT e.*,
            (SELECT nome FROM product WHERE id = e.produto_id) as produto_nome
        FROM estoque e WHERE e.id = %s
    """

    def get_all(self):
        try:
            with DataBase() as db:
                return db.execute(self.QUERY_ALL)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail=f"Erro ao buscar estoque")


    def get_id(self, id: int):
        try:
            with DataBase() as db:
                return db.execute(self.QUERY_GET_ID, (id,), many=False)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail=f"Erro ao encontrar estoque por id: {id}")

    def save(self, stock: StockCreate):
        with DataBase() as db:
            params = (stock.produto_id, stock.quantidade)
            
            created_stock = db.commit(self.QUERY_CREATE, params)
            if not created_stock:
                return None
            
            return db.execute(self.QUERY_GET_CREATED, (created_stock['id'],), many=False)