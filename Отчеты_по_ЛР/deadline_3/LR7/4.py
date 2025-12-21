from abc import ABC, abstractmethod

class PaymentSystem(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass
    
    @abstractmethod
    def refund(self, amount: float):
        pass

class CreditCardPayment(PaymentSystem):
    def pay(self, amount: float):
        print(f"оплата картой: {amount} руб.")
    
    def refund(self, amount: float):
        print(f"возврат на карту: {amount} руб.")

class PayPalPayment(PaymentSystem):
    def pay(self, amount: float):
        print(f"оплата через PayPal: {amount} руб.")
    
    def refund(self, amount: float):
        print(f"возврат через PayPal: {amount} руб.")

card_payment = CreditCardPayment()
paypal_payment = PayPalPayment()

card_payment.pay(1000)
card_payment.refund(500)

paypal_payment.pay(2000)
paypal_payment.refund(1000)