from abc import ABC, abstractmethod


# Classe base abstrata garantindo que todas as subclasses implementem process_payment corretamente
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


# Processador de pagamento via Cartão de Crédito
class CreditCardProcessor(PaymentProcessor):
    def __init__(self, card_number):
        self.card_number = card_number

    def process_payment(self, amount):
        return f"Processed {amount} using Credit Card {self.card_number}"


# Processador de pagamento via PIX
class PixProcessor(PaymentProcessor):
    def __init__(self, chave):
        self.chave = chave

    def process_payment(self, amount):
        return f"Processed {amount} using PIX key {self.chave}"


# Exemplo de uso:
cartao = CreditCardProcessor("1234-5678-9876-5432")
pix = PixProcessor("meuemail@example.com")

print(
    cartao.process_payment(100)
)  # Saída: Processed 100 using Credit Card 1234-5678-9876-5432
print(pix.process_payment(50))  # Saída: Processed 50 using PIX key meuemail@example.com
