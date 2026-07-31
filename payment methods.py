from abc import ABC, abstractmethod

# Abstract Class
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Child Class 1
class CreditCard(Payment):

    def pay(self, amount):
        print("Paid", amount, "using Credit Card")


# Child Class 2
class PayPal(Payment):

    def pay(self, amount):
        print("Paid", amount, "using PayPal")


# Child Class 3
class Bitcoin(Payment):

    def pay(self, amount):
        print("Paid", amount, "using Bitcoin")


# Main Program
p1 = CreditCard()
p1.pay(1000)

p2 = PayPal()
p2.pay(2000)

p3 = Bitcoin()
p3.pay(3000)