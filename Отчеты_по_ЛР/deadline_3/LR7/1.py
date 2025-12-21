from dataclasses import dataclass, field

@dataclass(frozen=True)
class Product:
    name: str
    price: float
    weight: float
    is_available: bool = True
    
    def order_cost(self, quantity: int) -> float:
        return self.price * quantity

apple = Product("Apple", 15.0, 0.5, True)
print(apple)
print(apple.order_cost(10))
