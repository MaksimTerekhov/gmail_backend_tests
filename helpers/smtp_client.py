from email.mime.base import MIMEBase
from smtplib import SMTP_SSL
from typing import (
    Dict,
    List,
)

from helpers.endpoint_class import Endpoint
from helpers.user_class import User


class SmtpClient:
    def __init__(self, endpoint: Endpoint, sender: User):
        self.client = SMTP_SSL(endpoint.host, endpoint.port)
        self.sender = sender

    def login(self):
        self.client.login(self.sender.email, self.sender.password)

    def send(
            self,
            message: MIMEBase,
            sender: User,
            recipients: List[User]
    ) -> Dict:
        rcpts = [user.email for user in recipients]
        return self.client.send_message(message, sender.email, rcpts)

    def close(self):
        self.client.quit()
        self.client.close()
