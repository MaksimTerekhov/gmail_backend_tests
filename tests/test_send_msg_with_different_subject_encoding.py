from email.header import Header

import pytest

from helpers import (
    EmailHeaders,
    MailboxFolders,
    MessageTypes,
)

ascii_text_subject = 'test'


@pytest.mark.parametrize(
    ['encoding', 'msg_charset', 'expected_subject'], [
        ('utf8', 'utf-8', '=?utf8?q?test?='),
        ('utf16', 'utf-16', '=?utf16?b?//50AGUAcwB0AA==?='),
        ('utf32', 'utf-32', '=?utf32?b?//4AAHQAAABlAAAAcwAAAHQAAAA=?='),
        ('ascii', 'ascii', 'test'),
        ('utf8', 'windows-1251', '=?utf8?q?test?=')
    ], ids=[
        'utf-8',
        'utf-16',
        'utf-32',
        'ascii',
        'utf-8 header and windows-1251'
    ])
def test_send_msg_with_different_subject_encoding(
        test_context,
        encoding,
        msg_charset,
        expected_subject
):
    header_subject = Header(ascii_text_subject, encoding)

    message = test_context.message_helper.create_message(
        msg_type=MessageTypes.TEXT
    )
    test_context.message_helper.set_headers(
        message, {
            EmailHeaders.SUBJECT: header_subject,
            EmailHeaders.CONTENT_TYPE: f'text/plain; charset="{msg_charset}"'
        })
    test_context.message_helper.send(message)

    actual_message = test_context.imap_helper.get_message_from_mailbox_folder(
        folder=MailboxFolders.INBOX,
        msg=message
    )

    assert actual_message[EmailHeaders.SUBJECT] == expected_subject, 'Unexpected message subject'
