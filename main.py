from fastapi import FastAPI
from api.routes import company_routes
from api.routes import type_product_routes
from api.routes import supplier_routes
from api.routes import product_routes
from api.routes import stock_routes


app = FastAPI()

app.include_router(company_routes.router)
app.include_router(type_product_routes.router)
app.include_router(supplier_routes.router)
app.include_router(product_routes.router)
app.include_router(stock_routes.router)


@app.get("/")
async def read_root():
    return {"PROJETO": "PRIMEIRA VA",
            "BANCO DE DADOS": "TEM TODO O SCRIPT NO ARQUIVO 'script alimentar banco.sql' PARA O BANCO DE DADOS FUNCIONAR. BASTA APENAS COPIAR E COLOCAR ESSE SCRIPT NA BASEDATA DO PGADMIN."}