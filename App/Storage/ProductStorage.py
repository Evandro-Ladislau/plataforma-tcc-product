import psycopg2
import logging

class ProductStorage:
    
    
    def __init__(self):
        # Configura a conexão com o banco de dados
        self.conn = psycopg2.connect(
            host='localhost',
            port=5432,
            database='product_data',
            user='root',
            password='plataforma_tcc_2024'
        )
        self.cursor = self.conn.cursor()
        
    def insert(self, product):
        try:
            query = '''
            INSERT INTO products (name, dest, quantity, price)
            VALUES (%s, %s, %s, %s);
            '''
            self.cursor.execute(query, (product.name, product.dest, product.quantity, product.price))
   
        except ValueError as ve: 
            logging.error('Validation error when inserting product: %s', str(ve)) 
            
        except Exception as e:
            logging.error('Error inserting product: %s', str(e))

