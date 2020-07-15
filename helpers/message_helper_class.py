from email.mime.base import MIMEBase
from typing import (
    Dict,
    List,
)

from utils import (
    SmtpClient,
    User,
)
from .helpers import (
    EmailHeaders,
    msg_settings,
    random_ascii_string,
)


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

    @staticmethod
    def set_headers(message: MIMEBase, headers: Dict[str, str]):
        for hdr_name, hdr_value in headers.items():
            if message[hdr_name]:
                message.replace_header(hdr_name, hdr_value)
            else:
                message.add_header(hdr_name, hdr_value)
        return message

    def create_message(
            self,
            msg_type: msg_settings,
            body: str = 'test',
            subject: str = 'test',
            sender: User = None,
            recipients: List[User] = None,
    ) -> MIMEBase:
        rcpt = ', '.join([usr.email for usr in recipients or self.recipient])
        headers = {
            EmailHeaders.SUBJECT: subject,
            EmailHeaders.FROM: sender or self.sender.email,
            EmailHeaders.TO: rcpt,
            EmailHeaders.TEST_ID: random_ascii_string(9)
        }

        msg = msg_type.type(body, msg_type.mime)
        self.set_headers(msg, headers)
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
