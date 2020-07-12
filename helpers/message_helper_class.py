from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from typing import List

from helpers.extra_helpers import random_ascii_string
from helpers.smtp_client import SmtpClient
from helpers.user_class import User


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
    ):
        msg = MIMEText(body)

        # TODO: create set_headers func
        msg.add_header('Subject', subject)
        msg.add_header('From', sender or self.sender.email)
        msg.add_header('test-id', random_ascii_string(12))
        msg.add_header('To', recipients or
                       ', '.join([usr.email for usr in recipients]))

        return msg

    def send(
            self,
            msg: MIMEBase,
            sender: User = None,
            recipients: User = None):
        self.smtp_client.send(
            message=msg,
            sender=sender or self.sender,
            recipients=recipients or self.recipient
        )
