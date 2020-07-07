from imaplib import IMAP4_SSL
from socket import gaierror

from helpers.user_class import User


class ImapEndpoint:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port


class ImapClient:
    def __init__(self, user: User, imap_endpoint: ImapEndpoint):
        self.user = user

        try:
            self.client = IMAP4_SSL(
                host=imap_endpoint.host,
                port=imap_endpoint.port
            )
        except gaierror:
            raise Exception(
                'Error with initialize imap client: '
                f'{imap_endpoint.host}:{imap_endpoint.port}')

    def login(self):
        self.client.login(
            user=self.user.email,
            password=self.user.password
        )

    def log_out(self):
        self.mailbox_cleanup()
        self.client.logout()

    def mailbox_cleanup(self):
        pass
