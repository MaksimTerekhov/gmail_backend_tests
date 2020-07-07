from attr import dataclass

from helpers.imap_client import ImapEndpoint


@dataclass
class TestSettings:
    imap_endpoint = ImapEndpoint('imap.gmail.com', 993)
    smtp_endpoint = ''
