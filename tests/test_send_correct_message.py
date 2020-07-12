from helpers import MailboxFolders

test_body = 'just test message body'
test_subject = 'just test message subject'


def test_send_correct_message(
    test_context
):
    message = test_context.message_helper.create_simple_text_message(
        body=test_body,
        subject=test_subject
    )
    test_context.message_helper.send(message)

    actual_message = test_context.imap_helper.get_folder_content_by_params(
        folder=MailboxFolders.INBOX,
        params={'test-id': message['test-id']}
    )

    assert actual_message['Subject'] == test_subject
    assert test_body in actual_message.get_payload()
