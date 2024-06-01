import psycopg2
import os
import logging
from App.Model.ProductModel import ProductModel
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

class ProductStorage:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                host=os.getenv('DB_HOST', 'localhost'),
                port=os.getenv('DB_PORT', 5432),
                database=os.getenv('DB_NAME', 'product_data'),
                user=os.getenv('DB_USER', 'root'),
                password=os.getenv('DB_PASSWORD', 'plataforma_tcc_2024')
            )
            self.cursor = self.conn.cursor()
            logging.info("Connection successful!")
        except Exception as e:
            logging.error(f"Error connecting to database: {e}")
            raise


    def get_cursor(self):
        try:
            yield self.cursor
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            logging.error(f"Error during transaction: {e}")
            raise
        finally:
            self.cursor.close()
            self.conn.close()

    def insert(self, product):
        with self.get_cursor() as cursor:
            try:
                query = '''
                INSERT INTO products (name, dest, quantity, price, active, created_at)
                VALUES (%s, %s, %s, %s, %s, %s);
                '''
                cursor.execute(query, (product.name, product.dest, product.quantity, product.price, product.active, product.created_at))
                logging.info(f'Product inserted successfully: {product.name}')
            except Exception as e:
                logging.error(f'Error inserting product: {e}')
                raise
