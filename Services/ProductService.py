from Storage.ProductStorage import ProductStorage
from Model.ProductModel import ProductModel

class ProductService:
    def __init__(self):
        self.conn = ProductStorage()
        
    def validate_product(self, ProductModel):
        if not ProductModel.name or not ProductModel.dest or not ProductModel.quantity or not ProductModel.price or ProductModel.price <= 0:
            raise ValueError("Um ou mais valores não estão preenchidos, verifique!")    
        else:
            print("Chamei")