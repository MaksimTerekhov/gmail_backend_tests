# Repository with tests for gmail

### How tests basically work:
 - Create email message with different conditions
 - Send message from *sender* to *recipient* with SMTP protocol
 - Get message from *recipient mailbox* by IMAP protocol
 - Check results
***

### How run tests:
After clone the repo just run a command:

```` python3 -m pytest --recipient=??? --recipient_password=??? --sender=??? --sender_password=???````
***

### Requirements:
Both accounts need turn on _"enable IMAP"_ and _"Unsafe applications allowed"_ in **gmail settings**
