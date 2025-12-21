class credit_card:
    def __init__(self, number, cvc, owner_name, balance, pin):
        self.__number = number
        self.__cvc = cvc
        self.owner_name = owner_name
        self._balance = balance
        self.__pin = pin
    
    def __check_pin(self, pin):
        return pin == self.__pin
    
    def pay(self, amount, pin):
        if not self.__check_pin(pin):
            return "неверный пин-код"
        
        if amount > self._balance:
            return "недостаточно денег"
        
        self._balance -= amount
        return f"оплачено {amount}. осталось: {self._balance}"

karta = credit_card("12345678", "123", "щаур водалаз", 5000, "0000")
print(karta.owner_name)
print(karta.pay(1000, "0000"))
print(karta.pay(5000, "0000"))
print(karta.pay(1000, "111661"))