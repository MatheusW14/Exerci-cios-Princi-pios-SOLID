class Notificacao:
    def enviar(self, mensagem):
        pass


class NotificacaoEmail(Notificacao):
    def __init__(self, email):
        self.email = email

    def enviar(self, mensagem):
        return f"Enviado '{mensagem}' via Email para {self.email}"


class NotificacaoSMS(Notificacao):
    def __init__(self, numero_telefone):
        self.numero_telefone = numero_telefone

    def enviar(self, mensagem):
        return f"Enviado '{mensagem}' via SMS para {self.numero_telefone}"


def validar_mensagem_sms(mensagem):
    if len(mensagem) > 160:
        raise ValueError("Mensagens SMS não podem exceder 160 caracteres")


def notificar_usuario(notificacao: Notificacao, mensagem):
    if isinstance(notificacao, NotificacaoSMS):
        validar_mensagem_sms(mensagem)
    return notificacao.enviar(mensagem)


notificacao_email = NotificacaoEmail("usuario@exemplo.com")
notificacao_sms = NotificacaoSMS("555-1234")

print(notificar_usuario(notificacao_email, "Old via Email"))
print(notificar_usuario(notificacao_sms, "Old via SMS"))
print(notificar_usuario(notificacao_sms, "A" * 200))  # Exceção: ValueError
