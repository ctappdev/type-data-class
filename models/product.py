class Product:
    product_id: int
    product_name: str
    product_price: float

    def __init__(self, prd_id, prd_name, prd_price):
        self.product_id = prd_id
        self.product_name = prd_name
        self.product_price = prd_price
