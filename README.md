I created this repository just like a pet-project for testing my new knowledge.

***
**How tests basically work:**
 - Create message with different conditions
 - Send message from *mailbox_1* to *mailbox_2* (SMPT)
 - Get message from *mailbox_2* (IMAP)
 - Assert results
***

**How to set accounts.**  
There are two ways:
 1. After fork repository set email in conftest.py like default values
 2. Run tests with command below:  
```` python3 -m pytest --recipient=??? --recipient_password=??? --sender=??? --sender_password=???````  
Put your values instead of ```???```

Note: On both accounts need to checkbox on **gmail**: "enable IMAP" and "Unsafe applications allowed"