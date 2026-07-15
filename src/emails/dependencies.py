from src.emails.services.emails import EmailService
from src.emails.providers.emails import EmailSender
from config.config import settings


def get_notification_service() -> EmailService:
    sender = EmailSender(settings.smtp)

    service = EmailService(sender=sender)

    return service
