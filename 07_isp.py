from abc import ABC, abstractmethod


class MetodoPagamento(ABC):
    pass


class PagamentoCartao(ABC):
    @abstractmethod
    def inserir_dados_cartao(self, numero_cartao, data_validade, cvv):
        pass


class PagamentoTransferencia(ABC):
    @abstractmethod
    def realizar_transferencia(self, banco, agencia, conta):
        pass


class PagamentoPayPal(ABC):
    @abstractmethod
    def autenticar_paypal(self, email, senha):
        pass


class CartaoCredito(PagamentoCartao):
    def inserir_dados_cartao(self, numero_cartao, data_validade, cvv):
        return f"Pagamento realizado com cartão {numero_cartao}"


class TransferenciaBancaria(PagamentoTransferencia):
    def realizar_transferencia(self, banco, agencia, conta):
        return f"Transferência realizada para conta {conta} no banco {banco}"


class PayPal(PagamentoPayPal):
    def autenticar_paypal(self, email, senha):
        return f"Pagamento realizado via PayPal para {email}"


# Exemplo de uso
cartao = CartaoCredito()
transferencia = TransferenciaBancaria()
paypal = PayPal()

print(cartao.inserir_dados_cartao("1234-5678-9012-3456", "12/25", "123"))
print(transferencia.realizar_transferencia("Banco A", "1234", "567890"))
print(paypal.autenticar_paypal("usuario@exemplo.com", "senha123"))
