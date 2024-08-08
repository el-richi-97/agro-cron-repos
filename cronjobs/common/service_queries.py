import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import os

load_dotenv()


class PostgreSQLManager:
    def __init__(self):
        self.host = os.getenv("HOST_AGRO")
        self.port = os.getenv("PORT_AGRO")
        self.database = os.getenv("DB_AGRO")
        self.user = os.getenv("USER_AGRO")
        self.password = os.getenv("PWD_AGRO")
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
        except Exception as e:
            print(f"Error connecting to PostgreSQL database: {e}")
            raise

    def execute_query(self, query, params=None, fetch=None):
        if self.connection is None:
            self.connect()
        cursor = self.connection.cursor(cursor_factory=RealDictCursor)
        try:
            cursor.execute(query, params)
            if fetch == 'one':
                result = dict(cursor.fetchone())
            elif fetch == 'all':
                result = [dict(row) for row in cursor.fetchall()]
            else:
                self.connection.commit()
                result = None

        except Exception as e:
            print(f"Error executing query: {e}")
            self.connection.rollback()
            raise
        finally:
            cursor.close()
        return result

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None


if __name__ == "__main__":
    manager = PostgreSQLManager()
    manager.connect()
    query = "SELECT * FROM empresa"
    res = manager.execute_query(query, fetch='all')
    print(res)
    manager.close()
