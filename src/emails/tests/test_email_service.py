# tests/modules/emails/services/test_email_service.py

from unittest.mock import AsyncMock

import pytest

from emails.services.emails import EmailService
from emails.schemas.emails import EmailPayload


@pytest.mark.asyncio
async def test_should_call_sender():
    sender = AsyncMock()

    service = EmailService(sender)

    payload = EmailPayload(
        to_email="user@test.com",
        to_first_name="Aroldo",
        subject="Hello",
        template_name="welcome.html",
        confirmation_url="https://example.com/confirm",
        context={"name": "Aroldo"},
    )

    await service.send_email(payload)

    sender.send.assert_awaited_once_with(payload)
