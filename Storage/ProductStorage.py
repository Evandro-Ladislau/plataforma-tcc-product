import logging  # Importe o módulo logging aqui
import psycopg2
from Model.ProductModel import ProductModel
from config.Logging import LoggingConfig

class ProductStorage:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                host='localhost',
                port=5432,
                database='product_data',
                user='root',
                password='plataforma_tcc_2024'
            )

            self.cursor = self.conn.cursor()

            print("Connection successful!")
        except Exception as e:
            print(f"Error connecting to database: {e}")

    def insert(self, ProductModel):
        try:
            query = 'INSERT INTO products (name, dest, quantity, price) VALUES (%s, %s, %s, %s);'
            self.cursor.execute(query, (ProductModel.name, ProductModel.dest, ProductModel.quantity, ProductModel.price))
            self.conn.commit()
            logging.info('Product inserted successfully!: %s', ProductModel.name)
        except Exception as e:
            logging.error('Error inserting product: %s', str(e))

product_storage = ProductStorage()
product = ProductModel('Product G', 'Destination B', 45, 35.5)
product_storage.insert(product)
