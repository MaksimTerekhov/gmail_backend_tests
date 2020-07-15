from attr import dataclass

from helpers import MessageHelper
from utils import (
    Endpoint,
    ImapClient,
    User,
)


@dataclass
class TestContext:
    imap_helper: ImapClient
    message_helper: MessageHelper


@dataclass
class SetupConfig:
    recipient: User
    sender: User
    imap_endpoint: Endpoint
    smtp_endpoint: Endpoint
