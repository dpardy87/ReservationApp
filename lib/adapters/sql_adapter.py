from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import psycopg2
from psycopg2.extras import RealDictCursor
import os


class SqlAdapter:
    """adapter for SQL operations"""

    def __init__(self, conn_str):
        self.conn_str = conn_str
        self.connection = self.create_connection()

    def create_connection(self):
        """Creates and returns a psycopg2 connection."""
        try:
            self.connection = psycopg2.connect(self.conn_str)
            return self.connection
        except psycopg2.OperationalError as e:
            raise ConnectionError(f"Failed to connect to the database: {str(e)}")

    def execute(self, query):
        """Executes a SQL query and returns the result as a list of dictionaries."""
        cur = self.connection.cursor()
        try:
            cur.execute(query)
            rows = cur.fetchall()
            columns = [
                desc[0] for desc in cur.description
            ]  # Get column names from the cursor
            results = [
                dict(zip(columns, row)) for row in rows
            ]  # Map each row to a dictionary
            self.connection.commit()
            return results
        except Exception as e:
            self.connection.rollback()
            print(f"Error occurred: {e}")
            return None
        finally:
            cur.close()
