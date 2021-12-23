# Repository with tests for gmail

### How tests basically work:
 - Create email message with different conditions
 - Send message from *sender* to *recipient* with SMTP protocol
 - Get message from *recipient mailbox* by IMAP protocol
 - Check results
***

### How run tests:
- Clone repository
- ``python -m pip install -r requirements.txt``
- `` python3 -m pytest --recipient=??? --recipient_password=??? --sender=??? --sender_password=???``
***

### Requirements:
Both accounts need turn on _"enable IMAP"_ and _"Unsafe applications allowed"_ in **gmail settings**

Also needed to unlock captcha visiting link _https://accounts.google.com/b/0/displayunlockcaptcha_
***

### CI:
Every push or merge branch to master triggers gitHub action with test run

- [Actions tab](https://github.com/MaksimTerekhov/gmail_backend_tests/actions)
- [File with CI scripts](https://github.com/MaksimTerekhov/gmail_backend_tests/blob/master/.github/workflows/main.yml)
