import sys
import imaplib
import getpass
import email
import re
import pprint


M = imaplib.IMAP4_SSL('imap.gmail.com')

try:
    # M.login('enhanceit.test@gmail.com', getpass.getpass())
    M.login('enhanceit.test@gmail.com', "Welcome2BB")
except imaplib.IMAP4.error:
    print("LOGIN FAILED!!! ")
rv, mailboxes = M.list()
# if rv == 'OK':
#     print("Mailboxes:")
#     print(mailboxes)
def process_mailbox(M):
  rv, data = M.search(None, "ALL") #"ALL" has to be switch with UNSEEN in order to see the json if it's working b/c it won't work after you run it the first time
  if rv != 'OK':
      print("No messages found!")
      return
  data_list = []
  for num in data[0].split():
      rv, data = M.fetch(num, '(RFC822)')
      if rv != 'OK':
          print("ERROR getting message", num)
          return
      dict_num = {}
      msg = email.message_from_string(data[0][1].decode('utf-8'))
      dict_num['From'] = msg['From'].replace(" <", ", <").split(",")
      dict_num["Message"] = msg['Subject']
      dict_num['Date:'] = msg['Date']
      #print(dict_num)

      if msg.is_multipart():
          # iterate over email parts
          for part in msg.walk():
              # extract content type of email
              content_type = part.get_content_type()
              content_disposition = str(part.get_content_disposition())
              try:
                  # get the email body
                  body = part.get_payload(decode=True).decode()
              except:
                  pass
              if content_type == "text/plain" and "attachment" not in content_disposition:
                  # print text/plain emails and skip attachments
                  newBody = body.replace("\r\n"," ").replace("*","").replace(" : ", ": ").replace("\u2022", "0.").replace('Responsibility',"Description")\
                                .replace("- ", "0.").replace("Tittle","Title").replace("Contract:","Type:")
                  phone = r"\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}"
                  dict_num['Phone Number'] = re.findall(phone, newBody)

                  regex_pattern = r"Title:\s\w+ \w+"
                  regex_pattern2 = r"Type: [a-zA-Z]\w+"
                  regex_pattern3 = r"Type:\s[0-9]\+ \w+"

                  job_title = re.findall(regex_pattern,newBody)
                  job_title = ":".join(job_title).split(":")
                  dict_num["Title"] = job_title[1]

                  emp_type = re.findall(regex_pattern2, newBody)
                  emp_type2 = re.findall(regex_pattern3, newBody)
                  job_type = emp_type + emp_type2
                  job_type = ":".join(job_type)
                  job_type = job_type.split(":")
                  dict_num["Employment Type"] = job_type[1]

                  b1,b2,b3 = newBody.partition('Description')
                  jobList1 = re.compile('(\s[\d]+\.)(.*?)(?=(\s[\d]+\.))')
                  dict_num['Job Description'] = re.findall(jobList1, b3)

                  # print(dict_num)
      data_list.append(dict_num)
  pprint.pprint(data_list, indent=4)


rv, data = M.select("\"INBOX\"")
if rv == 'OK':
    # print("Processing mailbox...\n")
    process_mailbox(M)
    M.close()
M.logout()

