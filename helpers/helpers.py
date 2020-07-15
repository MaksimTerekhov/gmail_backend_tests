import random
import string
from collections import namedtuple
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def random_ascii_string(length: int = 8) -> str:
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


class MailboxFolders:
    INBOX = 'INBOX'
    SENT = '"[Gmail]/Sent Mail"'
    SPAM = '"[Gmail]/Spam"'


class EmailHeaders:
    SUBJECT = 'Subject'
    FROM = 'From'
    TEST_ID = 'test-id'
    TO = 'To'


msg_settings = namedtuple('msg_settings', ['type', 'mime'])


class MessageTypes:
    TEXT = msg_settings(MIMEText, 'plain')
    HTML = msg_settings(MIMEText, 'html')
    MULTIPART = msg_settings(MIMEMultipart, 'mixed')
