import pytest

from configuration import TestSettings
from helpers import (
    SetupConfig,
    MessageHelper,
    TestContext,
)
from utils import (
    ImapClient,
    SmtpClient,
    User,
)


def pytest_addoption(parser):
    options = {
        '--recipient': {
            'help': 'Existing google user',
            'default': 'maks.denv.terehov@gmail.com'
        },
        '--recipient_password': {
            'help': 'Just user password',
        },
        '--sender': {
            'help': 'Existing google user',
            'default': 'mterekhov47@gmail.com'
        },
        '--sender_password': {
            'help': 'Just user password',
        }
    }

    for k, v in options.items():
        parser.addoption(k, **v)


@pytest.fixture
def setup_test_context(request):
    recipient = User(
        email=request.config.getoption('--recipient'),
        password=request.config.getoption('--recipient_password')
    )
    sender = User(
        email=request.config.getoption('--sender'),
        password=request.config.getoption('--sender_password')
    )
    imap_endpoint = TestSettings.imap_endpoint
    smtp_endpoint = TestSettings.smtp_endpoint

    return SetupConfig(
        recipient=recipient,
        sender=sender,
        imap_endpoint=imap_endpoint,
        smtp_endpoint=smtp_endpoint
    )


@pytest.fixture
def imap_client(setup_test_context):
    client = ImapClient(
        user=setup_test_context.recipient,
        imap_endpoint=setup_test_context.imap_endpoint
    )
    client.login()

    yield client

    client.log_out()


@pytest.fixture
def smtp_client(setup_test_context):
    client = SmtpClient(
        endpoint=setup_test_context.smtp_endpoint,
        sender=setup_test_context.sender
    )
    client.login()

    yield client

    client.close()


@pytest.fixture
def test_context(
        imap_client,
        smtp_client,
        setup_test_context
):
    return TestContext(
        imap_helper=imap_client,
        message_helper=MessageHelper(
            smtp_client=smtp_client,
            sender=setup_test_context.sender,
            recipient=[setup_test_context.recipient]
        )
    )
