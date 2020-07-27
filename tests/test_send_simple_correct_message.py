from helpers import (
    EmailHeaders,
    MailboxFolders,
    MessageTypes,
)

test_body = 'just test message body'
test_subject = 'just test message subject'


def test_send_simple_correct_message(
    test_context
):
    message = test_context.message_helper.create_message(
        body=test_body,
        subject=test_subject,
        msg_type=MessageTypes.TEXT
    )
    test_context.message_helper.send(message)

    actual_message = test_context.imap_helper.get_message_from_mailbox_folder(
        folder=MailboxFolders.INBOX,
        msg=message
    )

    assert actual_message[EmailHeaders.SUBJECT] == test_subject
    assert test_body in actual_message.get_payload()
