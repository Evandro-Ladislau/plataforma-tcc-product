# App/Service/ProductService.py
import logging
from App.Model.ProductModel import ProductModel
from App.Storage.ProductStorage import ProductStorage

class ProductService:
    def __init__(self):
        self.storage = ProductStorage()

    def validate_product(self, product):
        if not product.name or not product.dest:
            raise ValueError("Product name and description are required.")
        if not isinstance(product.quantity, int) or product.quantity < 0:
            raise ValueError("The quantity must be a non-negative integer.")
        if not isinstance(product.price, (int, float)) or product.price <= 0:
            raise ValueError("The price must be a positive number.")

    def insert(self, product):
        try:
            logging.debug(f'Validating product: {product.name}')
            self.validate_product(product)
            logging.debug(f'Product validated successfully: {product.name}')
            
            self.storage.insert(product)
            logging.info(f'Product inserted successfully: {product.name}')
        except ValueError as ve:
            logging.error(f'Validation error: {str(ve)}')
            raise
        except Exception as e:
            logging.error(f'Error inserting product: {str(e)}')
            raise
