import imaplib, email, time
from email import policy
from email.parser import BytesParser


username = 'pdfirsttutors@gmail.com'
password = 'kjam xygw wvdc pveh'


mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(username, password)
mail.select(mailbox = 'FirstTutors', readonly = False)


status, data = mail.uid('search', None, '(FROM "patrick_davie@outlook.com")')

if status == 'OK':

    email_ids = data[0].split()
    email_id = email_ids[-1]
    print(email_id)
    """
    mail.uid('copy', email_ids, 'Handeled')
    mail.uid('store',email_ids, '+FLAGS', '(\\Deleted)')"""

    new_email = mail.uid('fetch', email_id, '(RFC822)')

    msg = BytesParser(policy=policy.default).parsebytes(new_email)

    print(msg)