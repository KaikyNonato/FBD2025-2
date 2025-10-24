from core.db import DataBase
from modules.product.schemas import ProductCreate

class ProductRepository:
    
    QUERY_BASE = """
        SELECT 
            p.id,
            p.nome,
            p.descricao,
            p.preco,
            p.tipo_id,
            p.fornecedor_id,
            p.empresa_id,
            tp.name as tipo_nome,
            s.name as fornecedor_nome,
            c.name as empresa_nome
        FROM product p
        JOIN type_product tp ON p.tipo_id = tp.id
        JOIN supplier s ON p.fornecedor_id = s.id
        JOIN company c ON p.empresa_id = c.id
    """
    
    QUERY_ALL = f"{QUERY_BASE} ORDER BY p.nome"
    QUERY_GET_ID = f"{QUERY_BASE} WHERE p.id = %s"
    QUERY_GET_BY_COMPANY = f"{QUERY_BASE} WHERE p.empresa_id = %s ORDER BY p.nome"
    
    QUERY_CREATE = """
        INSERT INTO product (nome, descricao, preco, tipo_id, fornecedor_id, empresa_id) 
        VALUES (%s, %s, %s, %s, %s, %s) 
        RETURNING id;
    """

    def get_all(self):
        with DataBase() as db:
            return db.execute(self.QUERY_ALL)

    def get_id(self, id: int):
        with DataBase() as db:
            return db.execute(self.QUERY_GET_ID, (id,), many=False)

    def get_by_company_id(self, company_id: int):
        with DataBase() as db:
            return db.execute(self.QUERY_GET_BY_COMPANY, (company_id,))

    def save(self, product: ProductCreate):
        with DataBase() as db:
            params = (
                product.nome,
                product.descricao,
                product.preco,
                product.tipo_id,
                product.fornecedor_id,
                product.empresa_id
            )
            
            created_product = db.commit(self.QUERY_CREATE, params)
            if not created_product:
                return None
            
            return self.get_id(created_product['id'])

