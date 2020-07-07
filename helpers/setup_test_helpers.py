from attr import dataclass

from helpers.endpoint_class import Endpoint
from helpers.imap_client import ImapClient
from helpers.message_helper_class import MessageHelper
from helpers.user_class import User


@dataclass
class TestContext:
    imap_client: ImapClient
    message_helper: MessageHelper


@dataclass
class Configuration:
    recipient: User
    sender: User
    imap_endpoint: Endpoint
    smtp_endpoint: Endpoint
