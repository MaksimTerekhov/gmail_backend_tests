import random
import string

from attr import dataclass


def random_ascii_string(length: int = 8) -> str:
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


@dataclass
class MailboxFolders:
    INBOX = 'INBOX'
    SENT = '"[Gmail]/Sent Mail"'
    SPAM = '"[Gmail]/Spam"'
