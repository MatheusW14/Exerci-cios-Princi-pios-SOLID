class User:
    """Classe que representa um usuário, responsável apenas pelos seus dados."""

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email


class UserRepository:
    """Classe responsável por salvar o usuário no banco de dados."""

    def save(self, user: User):
        """
        Saves the given user to the database.

        Args:
            user (User): The user object to be saved, containing user details.
        """
        print(f"Saving user {user.name} to the database.")


class EmailService:
    """Classe responsável por enviar e-mails."""

    def send_welcome_email(self, user: User):
        """
        Sends a welcome email to the specified user.

        Args:
            user (User): The user to whom the welcome email will be sent.
        """
        print(f"Sending welcome email to {user.email}.")


# Exemplo de uso
user = User("Alice", "alice@example.com")

user_repository = UserRepository()
email_service = EmailService()

user_repository.save(user)
email_service.send_welcome_email(user)
