class product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class order:
    def __init__(self, status):
        self.status = status
        self.products = []
        self.deliveryman = None
    
    def add_product(self, product):
        self.products.append(product)
        print(f"товар {product.name} добавлен в заказ")
    
    def set_deliveryman(self, deliveryman):
        self.deliveryman = deliveryman
        print(f"доставщик назначен: {deliveryman.name}")

class deliveryman:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

class courier(deliveryman):
    def call_client(self):
        return f"курьер {self.name} звонит клиенту"

class drone(deliveryman):
    def fly(self):
        return f"дрон {self.name} летит"

tovar1 = product("телефон", 50000)
tovar2 = product("унитаз", 5000)

zakaz = order("в обработке")
zakaz.add_product(tovar1)
zakaz.add_product(tovar2)

kurier = courier("мага", 10)
zakaz.set_deliveryman(kurier)

print(kurier.call_client())