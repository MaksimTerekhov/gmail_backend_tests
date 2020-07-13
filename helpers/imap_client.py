import email
from email.message import Message
from imaplib import IMAP4_SSL
from socket import gaierror
from typing import Dict

from attr import dataclass

from helpers.endpoint_class import Endpoint
from helpers.extra_helpers import waiter
from helpers.user_class import User


@dataclass
class MailboxFolders:
    INBOX = 'INBOX'
    SENT = '"[Gmail]/Sent Mail"'
    SPAM = '"[Gmail]/Spam"'


class MessageNotFoundError(Exception):
    message: str = 'Message was not found in mailbox by search args: {args}'

    def __init__(self, fields: Dict):
        super().__init__(self.message.format(args=fields))


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

    @staticmethod
    def _prepare_search_params(params: Dict) -> str:
        return ''.join([f'(HEADER {k} "{v}")' for k, v in params.items()])

    def _get_msg_id_from_folder_by_params(
            self,
            folder: str,
            params: Dict
    ) -> str:
        self.client.select(folder)
        prms = self._prepare_search_params(params)
        _, msg_ids = self.client.search(None, prms)

        if msg_ids != [b'']:
            return msg_ids[0]
        raise MessageNotFoundError(params)

    def get_folder_content_by_params(
            self,
            folder: str,
            params: Dict
    ) -> Message:
        msg_id = waiter(
            func=self._get_msg_id_from_folder_by_params,
            folder=folder,
            params=params,
            seconds=30,
            retry_exception=MessageNotFoundError
        )
        _, bytes_msg = self.client.fetch(msg_id, '(RFC822)')
        return email.message_from_bytes(bytes_msg[0][1])

    def log_out(self):
        self.mailbox_cleanup()
        self.client.logout()

    # TODO: func must delete only tests messages
    def mailbox_cleanup(self):
        pass
