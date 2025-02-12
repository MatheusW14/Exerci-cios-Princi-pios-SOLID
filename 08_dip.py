from abc import ABC, abstractmethod


class EmailService(ABC):
    @abstractmethod
    def enviar_email(self, destinatario, mensagem):
        pass


class SMSService(ABC):
    @abstractmethod
    def enviar_sms(self, numero, mensagem):
        pass


class ConcreteEmailService(EmailService):
    def enviar_email(self, destinatario, mensagem):
        print(f"Enviando email para {destinatario}: {mensagem}")


class ConcreteSMSService(SMSService):
    def enviar_sms(self, numero, mensagem):
        print(f"Enviando SMS para {numero}: {mensagem}")


class Notificacao:
    def __init__(self, email_service: EmailService, sms_service: SMSService):
        self.email_service = email_service
        self.sms_service = sms_service

    def notificar_por_email(self, destinatario, mensagem):
        self.email_service.enviar_email(destinatario, mensagem)

    def notificar_por_sms(self, numero, mensagem):
        self.sms_service.enviar_sms(numero, mensagem)


# Exemplo de uso
email_service = ConcreteEmailService()
sms_service = ConcreteSMSService()

notificacao = Notificacao(email_service, sms_service)
notificacao.notificar_por_email("usuario@exemplo.com", "Bem-vindo!")
notificacao.notificar_por_sms("123456789", "Seu código é 4567")
