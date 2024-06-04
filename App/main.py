from App.Service.ProductService import ProductService
from App.Model.ProductModel import ProductModel
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    logging.basicConfig(level=logging.INFO)
    product_service = ProductService()
    product = ProductModel('Product G', 'Destination B', 45, 0)
    product_service.insert(product)

if __name__ == "__main__":
    main()
