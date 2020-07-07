from imaplib import IMAP4_SSL
from socket import gaierror

from helpers.endpoint_class import Endpoint
from helpers.user_class import User


class ImapClient:
    def __init__(self, user: User, imap_endpoint: Endpoint):
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
        self.client.login(self.user.email, self.user.password)

    def log_out(self):
        self.mailbox_cleanup()
        self.client.logout()

    def mailbox_cleanup(self):
        pass
