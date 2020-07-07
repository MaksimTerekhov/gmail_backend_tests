import pytest

from configuration import TestSettings
from helpers.imap_client import ImapClient
from helpers.message_helper_class import MessageHelper
from helpers.setup_test_helpers import TestContext, Configuration
from helpers.smtp_client import SmtpClient
from helpers.user_class import User


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
def setup_tests(request):
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

    return Configuration(
        recipient=recipient,
        sender=sender,
        imap_endpoint=imap_endpoint,
        smtp_endpoint=smtp_endpoint
    )


@pytest.fixture
def imap_client(setup_tests):
    client = ImapClient(
        user=setup_tests.recipient,
        imap_endpoint=setup_tests.imap_endpoint
    )
    client.login()

    yield client

    client.log_out()


@pytest.fixture
def smtp_client(setup_tests):
    client = SmtpClient(
        endpoint=setup_tests.smtp_endpoint,
        sender=setup_tests.sender
    )
    client.login()

    yield client

    client.close()


@pytest.fixture
def test_context(
        imap_client: ImapClient,
        smtp_client: SmtpClient,
        setup_tests
):
    return TestContext(
        imap_client=imap_client,
        message_helper=MessageHelper(
            smtp_client=smtp_client,
            sender=setup_tests.sender,
            recipient=[setup_tests.recipient]
        )
    )
