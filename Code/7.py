from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str):
        pass

class EmailService(NotificationService):
    def send(self, recipient: str, message: str):
        print(f"Sending email to {recipient}: {message}")

class UserService:
    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service

    def notify_user(self, user_email: str, message: str):
        self.notification_service.send(user_email, message)

email_service = EmailService()
user_service = UserService(email_service)
user_service.notify_user("user@example.com", "Hello, User!")
