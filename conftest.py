import pytest

from configuration import TestSettings
from helpers.imap_client import ImapClient
from helpers.user_class import User


def pytest_addoption(parser):
    options = {
        '--recipient': {
            'help': 'Existing google user',
            'default': 'maks.denv.terehov@gmail.com'
        },
        '--recipient_password': {
            'help': 'Just user password',
        }
    }

    for k, v in options.items():
        parser.addoption(k, **v)


@pytest.fixture
def imap_client(request):
    imap_user = User(
        request.config.getoption('--recipient'),
        request.config.getoption('--recipient_password')
    )
    client = ImapClient(
        user=imap_user,
        imap_endpoint=TestSettings.imap_endpoint
    )
    client.login()

    yield client

    client.log_out()


@pytest.fixture
def test_context(
        imap_client: ImapClient
):
    pass
