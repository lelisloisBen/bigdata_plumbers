import email, getpass, imaplib, os, re

mylist = ['Delivered-To', 'Received', 'X-Google-Smtp-Source', 'X-Received', 'ARC-Seal', 'ARC-Message-Signature', 'ARC-Authentication-Results', 'Return-Path', 'Received', 'Received-SPF', 'Authentication-Results', 'Message-ID', 'DKIM-Signature', 'Received', 'Date', 'From', 'To', 'Subject', 'Content-Type', 'Feedback-ID', 'x-trackingcode']


mail = imaplib.IMAP4_SSL('imap.gmail.com')
(retcode, capabilities) = mail.login('email','password')
mail.list()
mail.select('inbox')

n=0
(retcode, messages) = mail.search(None, '(UNSEEN)')
if retcode == 'OK':

   for num in messages[0].split() :
      print 'Processing '
      n=n+1
      typ, data = mail.fetch(num,'(RFC822)')
      for response_part in data:
         if isinstance(response_part, tuple):
             original = email.message_from_string(response_part[1])

            #  print original['Date']
            #  print original['From']
            #  print original['Subject']
            #  print original['Content']
             for theKeys in mylist:
                 del original[theKeys]
            #  del original['Delivered-To']
            #  del original['x-trackingcode']
            #  print original.keys()
             print original
             typ, data = mail.store(num,'+FLAGS','\\Seen')

print n