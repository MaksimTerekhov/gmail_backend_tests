from helpers.imap_client import MailboxFolders


def test_send_correct_message(
    test_context
):
    message = test_context.message_helper.create_simple_text_message()
    test_context.message_helper.send(message)

    actual_message = test_context.imap_helper.get_folder_content_by_params(
        folder=MailboxFolders.INBOX,
        params={'test-id': message['test-id']}
    )

    assert actual_message['Subject'] == 'test'
