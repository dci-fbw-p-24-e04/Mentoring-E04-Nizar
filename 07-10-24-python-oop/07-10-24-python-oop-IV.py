from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    
    @abstractmethod
    def process_payment(self, amount):
        pass
    
class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount} dollars")
    
    def send_money(source,to,amount):
        pass
        
class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of {amount} dollars")
        
    def make_gift(self):
        pass
    
cc_processor = CreditCardProcessor()
pp_processor = PayPalProcessor()
cc_processor.process_payment(1000)
pp_processor.process_payment(500)