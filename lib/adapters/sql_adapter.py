"""file for handling connecting and executing sql commands"""

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import os

# path for sql certs if required
module_path = os.path.abspath(__file__)
root_dir = os.path.abspath(os.path.join(module_path, "..", ".."))
SSL_CERT = os.path.join(root_dir, "")


class SqlAdapter:
    """base adapter for sql operations"""

    def __init__(self, conn_str, use_ssl=False):
        self.conn_str = conn_str
        self.engine = None
        self.create_engine(use_ssl)

    def create_engine(self, use_ssl):
        """Creates SQLAlchemy engine with optional SSL"""
        try:
            if use_ssl:
                self.engine = create_engine(
                    self.conn_str,
                    connect_args={"sslmode": "require", "sslrootcert": SSL_CERT},
                )
            else:
                self.engine = create_engine(self.conn_str)
        except SQLAlchemyError as e:
            raise ConnectionError(f"Failed to create SQL engine: {str(e)}")

    def execute(self, query, fetch_all=True):
        """executes query to sql client"""
        try:
            with self.engine.connect() as conn:
                result = conn.execute(query)
                if result.returns_rows:
                    return result.fetchall() if fetch_all else result.fetchone()
                else:
                    return None
        except SQLAlchemyError as e:
            raise

    def insert(self, query):
        """Executes an insert query to the SQL client"""
        try:
            with self.engine.connect() as conn:
                conn.execute(query)
        except SQLAlchemyError as e:
            raise


class PostgresAdapter(SqlAdapter):
    """Adapter for PostgreSQL-specific operations"""

    def __init__(self, conn_str, use_ssl=False):
        super().__init__(conn_str, use_ssl)
