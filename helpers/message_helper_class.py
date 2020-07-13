from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from typing import (
    Dict,
    List,
)

from helpers.extra_helpers import random_ascii_string
from helpers.smtp_client import SmtpClient
from helpers.user_class import User


# TODO: create other func for creating other messages with diff mime_types
class MessageHelper:
    def __init__(
            self,
            smtp_client: SmtpClient,
            sender: User,
            recipient: List[User]
    ):
        self.smtp_client = smtp_client
        self.sender = sender
        self.recipient = recipient

    def create_simple_text_message(
            self,
            body: str = 'test',
            subject: str = 'test',
            sender: User = None,
            recipients: List[User] = None
    ) -> MIMEText:
        msg = MIMEText(body)

        # TODO: create set_headers func
        msg.add_header('Subject', subject)
        msg.add_header('From', sender or self.sender.email)
        msg.add_header('test-id', random_ascii_string(12))

        rcpt = recipients or self.recipient
        msg.add_header('To', ', '.join([usr.email for usr in rcpt]))

        return msg

    def send(
            self,
            msg: MIMEBase,
            sender: User = None,
            recipients: List[User] = None
    ) -> Dict:
        return self.smtp_client.send(
            message=msg,
            sender=sender or self.sender,
            recipients=recipients or self.recipient
        )
