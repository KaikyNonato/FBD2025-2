import psycopg2
from psycopg2 import sql as psycopg2_sql
from psycopg2.extras import RealDictCursor

from core import settings


class DataBase:
    """
    Classe de gerenciamento de conexão com o banco de dados.
    Utiliza um padrão de context manager para garantir que as conexões sejam fechadas.
    """
    def __init__(self):
        self.conn = None

    def __enter__(self):
        try:
            self.conn = psycopg2.connect(
                host=settings.DB_HOST,
                database=settings.DB_NAME,
                user=settings.DB_USER,
                password=settings.DB_PASSWORD,
                port=settings.DB_PORT,
                cursor_factory=RealDictCursor  # Define o cursor padrão
            )
            return self
        except psycopg2.OperationalError as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()

    def execute(self, sql, params=None, many=True):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql, params)
                if many:
                    return cursor.fetchall()
                return cursor.fetchone()
        except psycopg2.Error as e:
            print(f"Erro ao executar query: {e}")
            self.conn.rollback()
            raise  # Re-lança a exceção para ser tratada na camada de serviço/rota

    def commit(self, sql, params=None):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql, params)
                self.conn.commit()
                # Para queries com RETURNING, o resultado estará disponível
                return cursor.fetchone()
        except psycopg2.Error as e:
            print(f"Erro ao executar commit: {e}")
            self.conn.rollback()
            raise # Re-lança a exceção para que a camada superior saiba do erro