from attr import dataclass

from helpers import Endpoint


@dataclass
class TestSettings:
    imap_endpoint = Endpoint('imap.gmail.com', 993)
    smtp_endpoint = Endpoint('smtp.gmail.com', 465)
