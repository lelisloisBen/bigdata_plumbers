import email, getpass, imaplib, os, re
import sys
# import matplotlib.pyplot as plt

# detach_dir = "/home/consultant/Desktop/bigdata_plumbers/014_Gmail_scraping"

# imap_user = raw_input("samirbenzada@gmail.com")
# imap_password = getpass.getpass("toulouse.32")

# imap_server = "imap.gmail.com"


# m.login(user, pwd)

# m.select("Inbox")

conn = imaplib.IMAP4_SSL("imap.gmail.com")

try:
    (retcode, capabilities) = conn.login("samirbenzadaweb@gmail.com", "toulouse.32")
except:
    print sys.exc_info()[1]
    sys.exit(1)

conn.select(readonly=1) # Select inbox or default namespace

(retcode, messages) = conn.search(None, '(UNSEEN)')

print(messages)

# if retcode == 'OK':
#     for num in messages[0].split(' '):
#         print 'Processing :', messages
#         typ, data = conn.fetch(num,'(RFC822)')
#         msg = email.message_from_string(data[0][1])
#         typ, data = conn.store(num,'-FLAGS','\\Seen')
#         if ret == 'OK':
#             print data,'\n',30*'-'
#             print msg

conn.close()

