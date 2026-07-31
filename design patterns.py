# Strategy Interface
class PaymentStrategy:
    def pay(self, amount):
        pass


# Concrete Strategy 1
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")


# Concrete Strategy 2
class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print("Paid", amount, "using PayPal")


# Concrete Strategy 3
class BitcoinPayment(PaymentStrategy):
    def pay(self, amount):
        print("Paid", amount, "using Bitcoin")


# Context Class
class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def make_payment(self, amount):
        self.strategy.pay(amount)


# Main Program
processor = PaymentProcessor(CreditCardPayment())
processor.make_payment(1000)

processor.set_strategy(PayPalPayment())
processor.make_payment(2000)

processor.set_strategy(BitcoinPayment())
processor.make_payment(3000)