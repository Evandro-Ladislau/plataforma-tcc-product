from App.Storage.ProductStorage import ProductStorage
from App.Model.ProductModel import ProductModel
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    logging.basicConfig(level=logging.INFO)
    product_storage = ProductStorage()
    product = ProductModel('Product G', 'Destination B', 45, 35.5)
    product_storage.insert(product)

if __name__ == "__main__":
    main()
