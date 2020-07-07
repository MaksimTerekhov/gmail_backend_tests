

def test_send_correct_message(
    test_context
):
    message = test_context.message_helper.create_simple_text_message()
    test_context.message_helper.send(message)
