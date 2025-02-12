from abc import ABC, abstractmethod


# Interface para o Logger
class Logger(ABC):
    @abstractmethod
    def escrever_log(self, mensagem):
        pass


# Implementação concreta para Logger em arquivo
class LoggerArquivo(Logger):
    def escrever_log(self, mensagem):
        with open("log.txt", "a") as file:
            file.write(f"{mensagem} \n")


# Implementação concreta para Logger em banco de dados (exemplo)
class LoggerBancoDados(Logger):
    def escrever_log(self, mensagem):
        # Simulação de escrita no banco de dados
        print(f"Log gravado no banco de dados: {mensagem}")


# Implementação concreta para Logger em sistema de monitoramento (exemplo)
class LoggerMonitoramento(Logger):
    def escrever_log(self, mensagem):
        # Simulação de envio para sistema de monitoramento
        print(f"Log enviado para sistema de monitoramento: {mensagem}")


class Aplicacao:
    def __init__(self, logger: Logger):
        self.logger = logger

    def executar(self):
        self.logger.escrever_log("Aplicação iniciada")
        # Código da aplicação...
        self.logger.escrever_log("Aplicação finalizada")


# Exemplo de uso com LoggerArquivo
logger_arquivo = LoggerArquivo()
app_arquivo = Aplicacao(logger_arquivo)
app_arquivo.executar()

# Exemplo de uso com LoggerBancoDados
logger_banco = LoggerBancoDados()
app_banco = Aplicacao(logger_banco)
app_banco.executar()

# Exemplo de uso com LoggerMonitoramento
logger_monitoramento = LoggerMonitoramento()
app_monitoramento = Aplicacao(logger_monitoramento)
app_monitoramento.executar()
